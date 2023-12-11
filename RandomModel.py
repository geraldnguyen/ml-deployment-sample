import numpy as np

class RandomModel:
    def fit(self, X, y):
        pass

    def predict(self, X):
        return np.random.choice([0, 1], size=(X.shape[0],), p=[0.5, 0.5])