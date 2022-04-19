import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from itertools import combinations

from gui import Ui_mainwindow
from process import Experiment
from resTable import ExcelTable, PlanTable


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.experiment = None
        self.table = PlanTable('ОЦКП.xlsx')

        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)

        self.ui.minG1.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.minG1))
        self.ui.maxG1.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.maxG1))
        self.ui.minG2.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.minG2))
        self.ui.maxG2.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.maxG2))

        self.ui.minP1.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.minP1))
        self.ui.maxP1.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.maxP1))
        self.ui.minP2.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.minP2))
        self.ui.maxP2.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.maxP2))

        self.ui.x1.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x1))
        self.ui.x2.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x2))
        self.ui.x3.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x3))
        self.ui.x4.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x4))

        self.ui.timeM.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.timeM))
        self.ui.numTasks.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.numTasks))

        self.ui.DoModeling.clicked.connect(self.doModeling)
        self.ui.Checking.clicked.connect(self.doChecking)
        self.ui.ShowMatrix.clicked.connect(self.showMatrix)

        self.deactivateButton()

    def activateInput(self):
        self.ui.nonlinear.setEnabled(True)
        self.ui.a.setEnabled(True)
        self.ui.star.setEnabled(True)

    def activateButton(self):
        self.ui.Checking.setEnabled(True)
        self.ui.ShowMatrix.setEnabled(True)

    def deactivateInput(self):
        self.ui.nonlinear.setEnabled(False)
        self.ui.a.setEnabled(False)
        self.ui.star.setEnabled(False)

    def deactivateButton(self):
        self.ui.Checking.setEnabled(False)
        self.ui.ShowMatrix.setEnabled(False)

    def setEquations(self, strNonlin: str):
        self.ui.nonlinear.setText(strNonlin)

    def setStar(self, a):
        self.ui.star.setText(str('%.3f' % a))

    def setA(self, a):
        print('alpha ', a)
        self.ui.a.setText(str('%.3f' % a))

    def doModeling(self):
        try:
            intGMin1 = float(self.ui.minG1.text())
            intGMax1 = float(self.ui.maxG1.text())
            intGMin2 = float(self.ui.minG2.text())
            intGMax2 = float(self.ui.maxG2.text())

            intPMin1 = float(self.ui.minP1.text())
            intPMax1 = float(self.ui.maxP1.text())
            intPMin2 = float(self.ui.minP2.text())
            intPMax2 = float(self.ui.maxP2.text())

            try:
                numTasks = int(self.ui.numTasks.text())
            except:
                numTasks = None

            try:
                timeModeling = float(self.ui.timeM.text())
            except:
                timeModeling = None

            self.experiment = Experiment([intGMin1, intGMax1, intGMin2, intGMax2],
                                         [intPMin1, intPMax1, intPMin2, intPMax2],
                                         numTasks, timeModeling)

            self.matrFull, self.b, self.a, self.alpha = self.experiment.run()
            self.demonstrateRes()

            self.activateButton()
        except Exception as e:
            msg = QMessageBox()
            msg.setText('ОШИБКА!\n' + repr(e))
            msg.show()
            msg.exec()

    def doChecking(self):
        try:
            x1 = float(self.ui.x1.text())
            x2 = float(self.ui.x2.text())
            x3 = float(self.ui.x3.text())
            x4 = float(self.ui.x4.text())

            point = [x1, x2, x3, x4]
            res = self.experiment.check(point)

            self.show_check(res, self.table)
        except Exception as e:
            msg = QMessageBox()
            msg.setText('ОШИБКА!\n' + repr(e))
            msg.show()
            msg.exec()

    def demonstrateRes(self):
        nonLinFull = self.getString(self.b)

        self.activateInput()
        self.setEquations(nonLinFull)
        self.setStar(self.alpha)
        self.setA(self.a)
        self.deactivateInput()

        self.showMatrix()

    def getString(self, b):
        nonlinStr, val = self.getNonlinStr(b)
        nonlinStrT = (nonlinStr % tuple(val))

        return nonlinStrT

    def getNonlinStr(self, regr):
        x = []
        val = [regr[0]]
        for i in range(self.experiment.numFactors):
            x.append("x%d" % (i + 1))

        res_str = "y = %.3f"
        pos = 1
        for i in range(1, 3):
            for comb in combinations(x, i):
                cur_str = "%.3f"
                if regr[pos] < 0:
                    cur_str = " - " + cur_str
                    regr[pos] = abs(regr[pos])
                else:
                    cur_str = " + " + cur_str

                for item in comb:
                    cur_str += item
                res_str += cur_str
                val.append(regr[pos])
                pos += 1
        pos = 2 ** self.experiment.numFactors

        for i in range(1, self.experiment.numFactors + 1):
            cur_str = "%.3f"
            if i > 2:
                cur_str = " - " + cur_str
                regr[pos] = abs(regr[pos])
            else:
                cur_str = " + " + cur_str
            cur_str += x[i - 1] + "^2"
            res_str += cur_str
            val.append(regr[pos])
            pos += 1

        return res_str, val

    def show_check(self, res, widget):
        widget.addRow(res)

    def showMatrix(self):
        self.table.show(self.matrFull)


if __name__ == "__main__":
    app = QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
