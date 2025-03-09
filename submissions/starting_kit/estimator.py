from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR


class Estimator:
    def __init__(self):
        self.model = SVR()
        self.scalerX = StandardScaler()
        self.scalerY = StandardScaler()
    
    def fit(self, X, y):
        X_train = self.scalerX.fit_transform(X_train)
        y_train = self.scalerY.fit_transform(y)
        self.model.fit(X_train, y_train)
        return self

    def predict(self, X):
        y_pred_scaled = self.model.predict(X)
        return self.scalerY.inverse_transform(y_pred_scaled)