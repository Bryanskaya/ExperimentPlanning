from typing import List, Tuple

import numpy as np

from Model import Model
from Distributions import ExponentGenerator, WeibullGenerator
from Generator import Generator
from Processor import Processor


class Experiment(object):
    numFactors = 2
    sizeMatr = 2 ** numFactors
    numModels = 10

    def __init__(self, generator: List[float], processor: List[float],
                 tasks: int, time: float):
        self.intGMin = generator[0]
        self.intGMax = generator[1]
        self.intPMin = processor[0]
        self.intPMax = processor[1]

        self.time = time
        self.numTasks = tasks
        self.a = None

    def run(self) -> Tuple[List[List[float]], List[float]]:
        matr0 = self.getInitMatr()
        matr = self.leastSquaresMethod(matr0)

        waitArr = self.scaleElements(matr0)
        matr0, self.a = self.calculate(matr0, waitArr, matr)
        return matr0, self.a

    def check(self, intG: float, intP: float):
        waitTime = 0
        intGN = self.scale(intG, self.intGMin, self.intGMax)
        intPN = self.scale(intP, self.intPMin, self.intPMax)

        for i in range(self.numModels):
            model = Model([Generator(ExponentGenerator(intGN))],
                          [Processor(WeibullGenerator(2, intPN))])
            info = model.doModeling(self.numTasks, self.time)
            waitTime += info['avgWait']
        waitTime /= self.numModels

        linRes = self.a[0] + self.a[1] * intG + self.a[2] * intP
        nonLinRes = self.a[0] + self.a[1] * intG + self.a[2] * intP + \
                    self.a[3] * intG * intP

        return {'intG': intG,
                'intP': intP,
                'waitAvg': waitTime,
                'lin': linRes,
                'nonLin': nonLinRes}

    def getZeroMatr(self) -> List[List[float]]:
        return [[0 for i in range(self.sizeMatr)] for i in range(self.sizeMatr)]

    def getInitMatr(self) -> List[List[float]]:
        matr = self.getZeroMatr()

        matr[0][0] = 1
        matr[1][0] = 1
        matr[2][0] = 1
        matr[3][0] = 1

        matr[0][1] = -1
        matr[1][1] = -1
        matr[2][1] = 1
        matr[3][1] = 1

        matr[0][2] = -1
        matr[1][2] = 1
        matr[2][2] = -1
        matr[3][2] = 1

        matr[0][3] = matr[0][1] * matr[0][2]
        matr[1][3] = matr[1][1] * matr[1][2]
        matr[2][3] = matr[2][1] * matr[2][2]
        matr[3][3] = matr[3][1] * matr[3][2]

        return matr

    def leastSquaresMethod(self, matr: List[List[float]]):
        transposedMatr = np.transpose(matr)  # транспонирование
        multMatrs = np.matmul(transposedMatr, matr)
        invMatr = np.linalg.inv(multMatrs)  # обратная матрица
        res = np.matmul(invMatr, transposedMatr)

        return self._ndarrayToListList(res)

    def scaleElements(self, matr0: List[List[float]]):
        waitArr = []
        for elem in matr0:
            intG = self.scale(elem[1], self.intGMin, self.intGMax)
            intP = self.scale(elem[2], self.intPMin, self.intPMax)

            waitTime = 0
            for i in range(self.numModels):
                model = Model([Generator(ExponentGenerator(intG))],
                              [Processor(WeibullGenerator(2, intP))])
                info = model.doModeling(self.numTasks, self.time)
                waitTime += info['avgWait']
            waitTime /= self.numModels

            waitArr.append(waitTime)

        return waitArr

    def calculate(self, matr0: List[List[float]], y: List[float], matr: List[List[float]]):
        a: List[float] = []
        for i in range(len(matr)):
            temp = 0
            for j in range(len(matr[i])):
                temp += matr[i][j] * y[j]
            a.append(temp)

        yLinear = []
        yNonlinear = []
        for i in range(len(matr0)):
            yLinear.append(self.linear(a, matr0[i]))
            yNonlinear.append(self.nonLinear(a, matr0[i]))

        for i in range(len(matr0)):
            matr0[i].append(y[i])
            matr0[i].append(yLinear[i])
            matr0[i].append(yNonlinear[i])
            matr0[i].append(abs(y[i] - yLinear[i]))
            matr0[i].append(abs(y[i] - yNonlinear[i]))

        return matr0, a

    def linear(self, a: List[float], x: List[float]) -> float:
        res = 0
        for i in range(self.sizeMatr - 1):
            res += a[i] * x[i]
        return max(res, 0)

    def nonLinear(self, a: List[float], x: List[float]) -> float:
        res = 0
        for i in range(len(a)):
            res += a[i] * x[i]
        return max(res, 0)

    def scale(self, elem: float, eMin: float, eMax: float):
        return eMin + (eMax - eMin) * (elem + 1) / 2

    def _ndarrayToListList(self, arr: np.ndarray) -> List[List[float]]:
        res = []
        for row in arr:
            res.append(row.tolist())
        return res
