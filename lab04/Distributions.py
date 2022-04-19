import numpy.random as nr
from scipy.stats import weibull_min
import math


class ExponentGenerator:
    def __init__(self, paramLambda):
        self.paramLambda = paramLambda

    def getTime(self):
        return nr.exponential(1/self.paramLambda)


class WeibullGenerator:
    def __init__(self, k, paramLambda):
        self.k = k
        self.paramLambda = (1 / paramLambda) * math.log(2, math.e) ** (-1 / self.k)

    def getTime(self):
        return weibull_min.rvs(self.k, loc=0, scale=self.paramLambda)
