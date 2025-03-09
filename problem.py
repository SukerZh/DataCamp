import rampwf as rw

import pandas as pd
import numpy as np
import os

from sklearn.model_selection import StratifiedShuffleSplit

problem_title = 'Economic forecast based on machinery data'

_target_column_name = 'GDP'

# A type (class) which will be used to create wrapper objects for y_pred
Predictions = rw.prediction_types.make_regression(label_names=[_target_column_name])

# An object implementing the workflow
workflow = rw.workflows.Estimator()

score_types = [
    rw.score_types.Accuracy(name='accuracy', precision=4),
]


def get_cv(X, y):
    cv = StratifiedShuffleSplit(n_splits=8, test_size=0.2, random_state=57)
    return cv.split(X, y)

def _process_csv(path, f_name, col_name):
    df = pd.read_csv(os.path.join(path, "data", f_name))
    return df.melt(id_vars="Provinces", var_name="year_quarter", value_name=col_name)

def _convert_dates(df):
    df["year_quarter"] = pd.to_datetime(df['year_quarter'], format='%Y/%m/%d')
    df["year_quarter"] = df['year_quarter'].dt.to_period('Q').astype(str)
    return df

def _load_data(path):
    df_crane = _process_csv(path, "crane_sum_quarterly.csv", "crane")
    df_excavator = _process_csv(path, "excavator_sum_quarterly.csv", "excavator")
    df_roller = _process_csv(path, "roller_sum_quarterly.csv", "roller")

    df_construction = _process_csv(path, "ConstructionTotalValueOutput.csv", "construction")
    df_construction = _convert_dates(df_construction)

    df_gdp = _process_csv(path, "GrossDomesticProduct.csv", "GDP")
    df_gdp = _convert_dates(df_gdp)

    df = pd.merge(df_crane, df_excavator, on=["Provinces", "year_quarter"])
    df = pd.merge(df, df_roller, on=["Provinces", "year_quarter"])
    df = pd.merge(df, df_construction, on=["Provinces", "year_quarter"])
    df = pd.merge(df, df_gdp, on=["Provinces", "year_quarter"])

    return df #possibility: test / train split here and the read it with get_train_data and get_test_data

_test_quarters = ["2020Q3", "2021Q2", "2022Q1", "2022Q4", "2023Q3"]  

def get_train_data(path="."):
    df = _load_data(path)
    df = df[~df.apply(lambda row: row['year_quarter'] in _test_quarters, axis=1)]
    y_array = df[_target_column_name].values
    X_df = df.drop([_target_column_name], axis=1)
    return X_df, y_array


def get_test_data(path="."):
    df = _load_data(path)
    df = df[df.apply(lambda row: row['year_quarter'] in _test_quarters, axis=1)]
    y_array = df[_target_column_name].values
    X_df = df.drop([_target_column_name], axis=1)
    return X_df, y_array
