# ml_model.py
from sklearn.linear_model import LinearRegression

class SimpleModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)
        return self.model.coef_.tolist(), self.model.intercept_

    def predict(self, X):
        return self.model.predict(X)
