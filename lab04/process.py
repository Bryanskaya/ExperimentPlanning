from typing import List, Tuple
from itertools import combinations

import numpy as np
import math

from Model import Model
from Distributions import ExponentGenerator, WeibullGenerator
from Generator import Generator
from Processor import Processor


class Experiment(object):
    numFactors = 4
    N0 = 2 ** numFactors
    N = N0 + 2 * numFactors + 1
    alpha = None
    a = math.sqrt(N0 / N)

    k = 1
    numModels = 8

    def __init__(self, generator: List[float], processor: List[float],
                 tasks: int, time: float):
        self.intGMinArr = [generator[0], generator[2]]
        self.intGMaxArr = [generator[1], generator[3]]
        self.intPMinArr = [processor[0], processor[2]]
        self.intPMaxArr = [processor[1], processor[3]]

        self.time = time
        self.numTasks = tasks

        self.b = []
        self.alpha = None

    def run(self):
        self.getAlpha()
        matrFull = self.getMatrFull()
        yFull = self.calculateY(matrFull)
        self.b = self.expandFull(matrFull, yFull)

        return matrFull, self.b, self.a, self.alpha

    def getAlpha(self):
        self.alpha = math.sqrt(0.5 * (math.sqrt(self.N * self.N0) - self.N0))

    def getMatrFull(self):
        matr = self.getZeroMatr(self.N0 + self.numFactors, self.N)

        for i in range(self.N):
            x = []
            matr[i][0] = 1
            pos = self.N0

            if i < self.N0:
                for j in range(1, self.numFactors + 1):
                    if i // (2 ** (j - 1)) % 2 == 1:
                        matr[i][j] = 1
                    else:
                        matr[i][j] = -1
                    x.append(matr[i][j])

                matr[i][0] = 1

                pos = self.numFactors + 1
                for j in range(2, self.numFactors + 1):
                    for comb in combinations(x, j):
                        matr[i][pos] = 1
                        for item in comb:
                            matr[i][pos] *= item
                        pos += 1
            elif i != self.N - 1:
                j = int((i - self.N0) / 2) + 1
                k = -1 if i % 2 else 1
                matr[i][j] = self.alpha * k

            for j in range(self.numFactors):
                matr[i][pos] = matr[i][j + 1] ** 2 - self.a
                pos += 1
        return matr

    def check(self, point):
        waitTime = 0
        genInt, pInt = self.scaleData(point)

        for i in range(self.numModels):
            model = Model([Generator(ExponentGenerator(genInt[0])),
                           Generator(ExponentGenerator(genInt[1]))],
                          [Processor(WeibullGenerator(2, pInt[0])),
                           Processor(WeibullGenerator(2, pInt[1]))])
            info = model.doModeling(self.numTasks, self.time)
            waitTime += info['avgWait']
        waitTime /= self.numModels

        b = self.b

        nonlin = self.calculateNonPlan(point)
        nonlin_y = self.calcY(b, nonlin)
        res = nonlin + [waitTime, nonlin_y, abs(waitTime - nonlin_y)]

        return res

    def calculateNonPlan(self, point):
        comb_x = [1]
        pos = 1

        for i in range(1, 5):
            for comb in combinations(point, i):
                cur_comb = 1
                for item in comb:
                    cur_comb *= item
                comb_x.append(cur_comb)
                pos += 1

        for i in range(4):
            comb_x.append(point[i] ** 2 - self.a)
        return comb_x

    def getZeroMatr(self, n, m) -> List[List[float]]:
        return [[0 for _ in range(n)] for _ in range(m)]

    def calculateY(self, matr: List[List[float]]):
        yArr = []
        for experiment in matr:
            intGArr, intPArr = self.scaleData(experiment[1:(self.numFactors + 1)])

            waitTime = 0
            for i in range(self.numModels):
                model = Model([Generator(ExponentGenerator(intGArr[0])),
                               Generator(ExponentGenerator(intGArr[1]))],
                              [Processor(WeibullGenerator(2, intPArr[0])),
                               Processor(WeibullGenerator(2, intPArr[1]))])
                info = model.doModeling(self.numTasks, self.time)
                waitTime += info['avgWait']
            waitTime /= self.numModels

            yArr.append(waitTime)
        return yArr

    def calculateBFull(self, plan, y):
        b: List[float] = []
        for i in range(len(plan[0])):
            temp1, temp2 = 0, 0
            for j in range(len(plan)):
                temp1 += plan[j][i] * y[j]
                temp2 += plan[j][i] ** 2
            b.append(temp1 / temp2)
        return b

    def scaleData(self, x):
        genInt = []
        genInt.append(self.scale(x[0], self.intGMinArr[0], self.intGMaxArr[0]))
        genInt.append(self.scale(x[1], self.intGMinArr[1], self.intGMaxArr[1]))

        pInt = []
        pInt.append(self.scale(x[2], self.intPMinArr[0], self.intPMaxArr[0]))
        pInt.append(self.scale(x[3], self.intPMinArr[1], self.intPMaxArr[1]))

        return genInt, pInt

    def scale(self, elem: float, eMin: float, eMax: float):
        return eMin + (eMax - eMin) * (elem + 1) / 2

    def expandFull(self, plan, y):
        b = self.calculateBFull(plan, y)
        yNonLin = self.fillY(plan, b)
        self.fillPlan(plan, y, yNonLin)

        return b

    def fillY(self, plan, b):
        ynlin = list()
        for i in range(len(plan)):
            if len(plan[i]):
                ynlin.append(self.calcY(b, plan[i]))
        return ynlin

    def calcY(self, a: List[float], x: List[float]) -> float:
        res = 0
        for i in range(len(a)):
            res += a[i] * x[i]
        return max(res, 0)

    def fillPlan(self, plan, y, yNonLin):
        for i in range(len(plan)):
            if len(plan[i]):
                plan[i].append(y[i])
                plan[i].append(yNonLin[i])
                plan[i].append(abs(y[i] - yNonLin[i]))

    # def _ndarrayToListList(self, arr: np.ndarray) -> List[List[float]]:
    #     res = []
    #     for row in arr:
    #         res.append(row.tolist())
    #     return res
