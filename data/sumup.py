import pandas as pd
from functools import reduce
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def process_machine_file(file, machine_name, read_encoding="utf-8-sig"):
    df = pd.read_csv(file, encoding=read_encoding)
    df = df.rename(columns=lambda col: f"{machine_name}_{col}" if col != "Provinces" else col)
    df["Provinces"] = df["Provinces"].replace({"吉林省": "吉林"})
    return df

def combine_machine_files(file_list, machine_names, read_encoding="utf-8-sig"):
    dfs = [process_machine_file(f, name, read_encoding) for f, name in zip(file_list, machine_names)]
    df_combined = reduce(lambda left, right: pd.merge(left, right, on="Provinces", how="outer"), dfs)
    for col in df_combined.columns:
        if any(name in col for name in machine_names) and "2023Q3" in col:
            df_combined[col] = df_combined[col] * 1.5
    return df_combined

def process_construction_file(file, read_encoding="gb18030"):
    df = pd.read_csv(file, encoding=read_encoding)
    def rename_construction_columns(col):
        if col == "Provinces":
            return col
        try:
            year, month, _ = col.split("/")
            quarter = (int(month) - 1) // 3 + 1
            return f"ConstVA_{year}Q{quarter}"
        except:
            return col
    df = df.rename(columns=rename_construction_columns)
    return df

def merge_machine_construction(machine_df, construction_df):
    province_order = construction_df["Provinces"].tolist()
    machine_df = machine_df[machine_df["Provinces"].isin(province_order)]
    machine_df = machine_df.set_index("Provinces").reindex(province_order).reset_index()
    merged = pd.merge(machine_df, construction_df, on="Provinces", how="inner")
    return merged

def wide_to_long(wide_df):
    df_long = wide_df.melt(id_vars=["Provinces"], var_name="Indicator_Time", value_name="Value")
    df_long[["Indicator", "Time"]] = df_long["Indicator_Time"].str.split("_", n=1, expand=True)
    df_long = df_long[["Time", "Indicator", "Provinces", "Value"]]
    return df_long

def split_train_test_long(long_df, province_encoding='onehot', test_size=0.2, random_state=42):
    df_pivot = long_df.pivot(index=["Time", "Provinces"], columns="Indicator", values="Value").reset_index()
    df_pivot = df_pivot[df_pivot["Time"] != "2023Q4"]
    df_pivot["Year"] = df_pivot["Time"].str[:4].astype(int)
    df_pivot["Quarter"] = df_pivot["Time"].str[-1].astype(int)
    if province_encoding == 'onehot':
        encoder = OneHotEncoder(sparse_output=False, drop="first")
        province_ohe = encoder.fit_transform(df_pivot[["Provinces"]])
        ohe_cols = encoder.get_feature_names_out(["Provinces"])
        df_ohe = pd.DataFrame(province_ohe, columns=ohe_cols, index=df_pivot.index)
        features = pd.concat([df_pivot[["Crane", "Roller", "Excavator", "Year", "Quarter"]], df_ohe], axis=1)
    elif province_encoding == 'target':
        province_mean = df_pivot.groupby("Provinces")["ConstVA"].mean()
        df_pivot["ProvinceEnc"] = df_pivot["Provinces"].map(province_mean)
        features = df_pivot[["Crane", "Roller", "Excavator", "Year", "Quarter", "ProvinceEnc"]]
    else:
        raise ValueError("province_encoding must be 'onehot' or 'target'")
    X = features
    y = df_pivot["ConstVA"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def main_pipeline():
    machine_files = ["crane_sum_quarterly.csv", "roller_sum_quarterly.csv", "excavator_sum_quarterly.csv"]
    machine_names = ["Crane", "Roller", "Excavator"]
    machine_df = combine_machine_files(machine_files, machine_names)
    
    constr_df = process_construction_file("ConstructionTotalValueOutput.csv")
    
    merged_wide = merge_machine_construction(machine_df, constr_df)
    
    long_df = wide_to_long(merged_wide)
    
    X_train, X_test, y_train, y_test = split_train_test_long(long_df, province_encoding='onehot')
    return X_train, X_test, y_train, y_test
