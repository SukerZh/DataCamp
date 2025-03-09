import rampwf as rw

import pandas as pd
import numpy as np
import os

from sklearn.model_selection import StratifiedShuffleSplit

problem_title = 'Economic forecast based on machinery data'

_target_column_name = 'FILL HERE'

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

def _read_csv(path, f_name):
    return pd.read_csv(os.path.join(path, "data", f_name))

def _load_data(path):
    df_construction = _read_csv(path, "ConstructionTotalValueOutput.csv")
    df_gdp = _read_csv(path, "GrossDomesticProduct.csv")
    # df_industrial = _read_csv(path, "IndustrialVA_YonY.csv")
    df_crane = _read_csv(path, "crane_sum_quarterly.csv")
    df_excavator = _read_csv(path, "excavator_sum_quarterly.csv")
    df_roller = _read_csv(path, "roller_sum_quarterly.csv")
    arr_crane = df_crane.iloc[:, 1:].to_numpy().flatten()
    arr_excavator = df_excavator.iloc[:, 1:].to_numpy().flatten()
    arr_roller = df_roller.iloc[:, 1:].to_numpy().flatten()
    arr_construction = df_construction.iloc[:, 1:-1].to_numpy().flatten()

    X_arr_2d = np.array([arr_crane, arr_excavator, arr_roller, arr_construction])
    X_arr = X_arr_2d.T
    X_df = pd.DataFrame(X_arr, columns = ["crane", "excavator", "roller", "construction"])

    arr_gdp = df_gdp.iloc[:, 1:-1].to_numpy().flatten()
    Y_arr = arr_gdp

    return X_df, Y_arr #possibility: test / train split here and the read it with get_train_data and get_test_data

# TODO
def get_train_data(path="."):
    X, y = _load_data(path)
    return

#TODO
def get_test_data(path="."):
    X, y = _load_data(path)
    return
