from typing import List, Tuple
from itertools import combinations

import numpy as np

from Model import Model
from Distributions import ExponentGenerator, WeibullGenerator
from Generator import Generator
from Processor import Processor

CHECK_FULL = 1
CHECK_PART = 0


class Experiment(object):
    numFactors = 4
    k = 1
    sizeMatr = 2 ** numFactors
    sizePart = 2 ** (numFactors - k)
    numPartK = 11
    numModels = 8

    def __init__(self, generator: List[float], processor: List[float],
                 tasks: int, time: float):
        self.intGMinArr = [generator[0], generator[2]]
        self.intGMaxArr = [generator[1], generator[3]]
        self.intPMinArr = [processor[0], processor[2]]
        self.intPMaxArr = [processor[1], processor[3]]

        self.time = time
        self.numTasks = tasks

        self.bFull = []
        self.bPart = []

    def run(self) -> Tuple[List[float], List[float], List[List[float]], List[List[float]]]:
        matrFull = self.getMatrFull()
        matrPart = self.getMatrPart()

        yFull = self.calculateY(matrFull)
        yPart = self.calculateY(matrPart)

        self.bFull = self.expandFull(matrFull, yFull)
        self.bPart = self.expandPart(matrPart, yPart)

        return self.bFull, self.bPart, matrFull, matrPart

    def getMatrFull(self):
        matr = self.getZeroMatr(self.numPartK, self.sizeMatr)

        for i in range(self.sizeMatr):
            x = []
            for j in range(1, self.numFactors + 1):
                if i // (2 ** (j - 1)) % 2 == 1:
                    matr[i][j] = 1
                else:
                    matr[i][j] = -1
                x.append(matr[i][j])

            matr[i][0] = 1

            pos = self.numFactors + 1
            for j in range(2, 3):
                for comb in combinations(x, j):
                    matr[i][pos] = 1
                    for item in comb:
                        matr[i][pos] *= item
                    pos += 1
        return matr

    def getMatrPart(self):
        matr = self.getZeroMatr(self.numPartK, self.sizePart)

        for i in range(self.sizePart):
            for j in range(1, self.numFactors):
                index = j
                if i // (2 ** (j - 1)) % 2 == 1:
                    matr[i][index] = 1
                else:
                    matr[i][index] = -1

            matr[i][4] = matr[i][1] * matr[i][2] * matr[i][3]

            matr[i][0] = 1

            matr[i][5] = matr[i][1] * matr[i][2]
            matr[i][6] = matr[i][1] * matr[i][3]
            matr[i][7] = matr[i][1] * matr[i][4]
            matr[i][8] = matr[i][2] * matr[i][3]
            matr[i][9] = matr[i][2] * matr[i][4]
            matr[i][10] = matr[i][3] * matr[i][4]

        return matr

    def check(self, point, mode):
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

        b = []
        if mode == CHECK_FULL:
            b = self.bFull
        else:
            b = self.bPart

        nonlin = self.calculateNonPlan(point)
        lin_y = self.calcY(b[:(self.numFactors + 1)], [1] + point)
        nonlin_y = self.calcY(b, nonlin)
        res = nonlin + [waitTime, lin_y, nonlin_y, abs(waitTime - lin_y), abs(waitTime - nonlin_y)]

        return res

    def calculateNonPlan(self, point):
        comb_x = [1]
        pos = 1

        for i in range(1, 3):
            for comb in combinations(point, i):
                cur_comb = 1
                for item in comb:
                    cur_comb *= item
                comb_x.append(cur_comb)
                pos += 1
        return comb_x

    def getZeroMatr(self, n, m) -> List[List[float]]:
        return [[0 for i in range(n)] for i in range(m)]

    def leastSquaresMethod(self, matr: List[List[float]]):
        transposedMatr = np.transpose(matr)  # транспонирование
        multMatrs = np.matmul(transposedMatr, matr)
        invMatr = np.linalg.inv(multMatrs)  # обратная матрица
        res = np.matmul(invMatr, transposedMatr)

        return self._ndarrayToListList(res)

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
            temp = 0
            for j in range(len(plan)):
                temp += plan[j][i] * y[j]
            b.append(temp / len(plan))
        return b

    def calculateBPart(self, plan, y):
        b = list()
        for i in range(int(np.log2(len(plan))) + 2):
            b_cur = 0
            for j in range(len(plan)):
                b_cur += plan[j][i] * y[j]
            b.append(b_cur / len(plan))
        for i in range(int(np.log2(len(plan))) + 2, len(plan[0])):
            b_cur = 0
            for j in range(len(plan)):
                b_cur += plan[j][i] * y[j]
            b.append(b_cur / len(plan) / 4)
        return b

    def calcY(self, a: List[float], x: List[float]) -> float:
        res = 0
        for i in range(len(a)):
            res += a[i] * x[i]
        return max(res, 0)

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
        yLin, yNonLin = self.fillY(plan, b[:int(np.log2(len(b))) + 1], b)
        self.fillPlan(plan, y, yLin, yNonLin)

        return b

    def expandPart(self, plan, y):
        b = self.calculateBPart(plan, y)
        yLin, yNonLin = self.fillY(plan, b[:int(np.log2(len(b))) + 1], b)
        self.fillPlan(plan, y, yLin, yNonLin)

        return b

    def fillY(self, plan, b1, b2):
        ylin, ynlin = list(), list()
        for i in range(len(plan)):
            if len(plan[i]):
                ylin.append(self.calcY(b1, plan[i]))
                ynlin.append(self.calcY(b2, plan[i]))
        return ylin, ynlin

    def fillPlan(self, plan, y, yLin, yNonLin):
        for i in range(len(plan)):
            if len(plan[i]):
                plan[i].append(y[i])
                plan[i].append(yLin[i])
                plan[i].append(yNonLin[i])
                plan[i].append(abs(y[i] - yLin[i]))
                plan[i].append(abs(y[i] - yNonLin[i]))

    def _ndarrayToListList(self, arr: np.ndarray) -> List[List[float]]:
        res = []
        for row in arr:
            res.append(row.tolist())
        return res
