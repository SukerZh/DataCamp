import pandas as pd

def process_file(input_file, output_file, read_encoding="gb18030", write_encoding="utf-8-sig"):
    df = pd.read_csv(input_file, encoding=read_encoding)
    
    date_cols = df.columns.drop(["Provinces", "Cities"])
    
    df_melted = df.melt(
        id_vars=["Provinces", "Cities"],
        value_vars=date_cols,
        var_name="Date",
        value_name="Value"
    )
    
    df_melted["Date"] = pd.to_datetime(df_melted["Date"], errors="coerce")
    
    df_melted = df_melted[(df_melted["Date"] >= "2020-01-01") & (df_melted["Date"] <= "2023-08-31")]
    
    df_melted["Month"] = df_melted["Date"].dt.to_period("M").astype(str)
    
    pivot_table = df_melted.pivot_table(
        index="Provinces",
        columns="Month",
        values="Value",
        aggfunc="sum"
    )
    
    pivot_table = pivot_table.reset_index()
    pivot_table.columns.name = None
    
    month_columns = sorted([col for col in pivot_table.columns if col != "Provinces"])
    pivot_table = pivot_table[["Provinces"] + month_columns]
    
    pivot_table.to_csv(output_file, index=False, encoding=write_encoding)
    print(f"Pivot table saved to '{output_file}'.")

file_names = ["crane", "roller", "excavator"]
for name in file_names:
    process_file(f"{name}.csv", f"{name}_sum_monthly.csv")