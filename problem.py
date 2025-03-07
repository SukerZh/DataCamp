import rampwf as rw

import pandas as pd
from pathlib import Path

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


#TODO: CHECK HERE
def load_data(path='.', file='X_train.csv'):
    path = Path(path) / "data"
    X_df = pd.read_csv(path / file)

    y = X_df[_target_column_name]
    X_df = X_df.drop(columns=[_target_column_name])

    return X_df, y


# READ DATA
def get_train_data(path='.'):
    file = 'X_train.csv'
    return load_data(path, file)


def get_test_data(path='.'):
    file = 'X_test.csv'
    return load_data(path, file)
