import numpy as np
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

class LinearRegression:
    def __init__(
            self,
            fit_intercept: bool=True) -> None:
        self.n_features = None
        self.fit_intercept = fit_intercept 

        self.w = None
        self.b = None

class AnalyticalRegressor:
    pass


class BaggedRegressor:
    pass


class BoostedRegressor:
    pass


class AdaBoostedRegressor:
    pass

