import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from itertools import combinations

from gui import Ui_mainwindow
from process import Experiment, CHECK_FULL, CHECK_PART
from resTable import ExcelTable, PlanTable


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.experiment = None
        self.tableFull = PlanTable('ПФЭ.xlsx')
        self.tablePart = PlanTable('ДФЭ.xlsx')

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

        self.ui.x1F.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x1F))
        self.ui.x2F.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x2F))
        self.ui.x3F.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x3F))
        self.ui.x4F.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x4F))

        self.ui.x1D.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x1D))
        self.ui.x2D.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x2D))
        self.ui.x3D.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x3D))
        self.ui.x4D.setValidator(QRegExpValidator(QRegExp("[0-9.-]*"), self.ui.x4D))

        self.ui.timeM.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.timeM))
        self.ui.numTasks.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.numTasks))

        self.ui.DoModeling.clicked.connect(self.doModeling)
        self.ui.CheckingF.clicked.connect(self.doCheckingFull)
        self.ui.CheckingD.clicked.connect(self.doCheckingD)
        self.ui.ShowMatrixF.clicked.connect(self.showFull)
        self.ui.ShowMatrixD.clicked.connect(self.showPart)

        self.deactivateButton()

    def activateInput(self):
        self.ui.linearF.setEnabled(True)
        self.ui.nonlinearF.setEnabled(True)
        self.ui.linearD.setEnabled(True)
        self.ui.nonlinearD.setEnabled(True)

    def activateButton(self):
        self.ui.CheckingF.setEnabled(True)
        self.ui.ShowMatrixF.setEnabled(True)
        self.ui.CheckingD.setEnabled(True)
        self.ui.ShowMatrixD.setEnabled(True)

    def deactivateInput(self):
        self.ui.linearF.setEnabled(False)
        self.ui.nonlinearF.setEnabled(False)
        self.ui.linearD.setEnabled(False)
        self.ui.nonlinearD.setEnabled(False)

    def deactivateButton(self):
        self.ui.CheckingF.setEnabled(False)
        self.ui.ShowMatrixF.setEnabled(False)
        self.ui.CheckingD.setEnabled(False)
        self.ui.ShowMatrixD.setEnabled(False)

    def setEquations(self, strLinF: str, strNonlinF: str,
                     strLinD: str, strNonlinD: str):
        self.ui.linearF.setText(strLinF)
        self.ui.nonlinearF.setText(strNonlinF)
        self.ui.linearD.setText(strLinD)
        self.ui.nonlinearD.setText(strNonlinD)

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

            self.bFull, self.bPart, self.matrFull, self.matrPart = self.experiment.run()
            self.demonstrateRes()

            self.activateButton()
        except Exception as e:
            msg = QMessageBox()
            msg.setText('ОШИБКА!\n' + repr(e))
            msg.show()
            msg.exec()

    def doCheckingFull(self):
        try:
            x1 = float(self.ui.x1D.text())
            x2 = float(self.ui.x2D.text())
            x3 = float(self.ui.x3D.text())
            x4 = float(self.ui.x4D.text())

            point = [x1, x2, x3, x4]
            res = self.experiment.check(point, CHECK_FULL)

            self.show_check(res, self.tableFull)
        except Exception as e:
            msg = QMessageBox()
            msg.setText('ОШИБКА!\n' + repr(e))
            msg.show()
            msg.exec()

    def doCheckingD(self):
        try:
            x1 = float(self.ui.x1D.text())
            x2 = float(self.ui.x2D.text())
            x3 = float(self.ui.x3D.text())
            x4 = float(self.ui.x4D.text())

            point = [x1, x2, x3, x4]
            res = self.experiment.check(point, CHECK_PART)

            self.show_check(res, self.tableFull)
        except Exception as e:
            msg = QMessageBox()
            msg.setText('ОШИБКА!\n' + repr(e))
            msg.show()
            msg.exec()

    def demonstrateRes(self):
        linFull, nonLinFull = self.getString(self.bFull, 2)
        linPart, nonLinPart = self.getString(self.bPart, 2)

        self.activateInput()
        self.setEquations(linFull, nonLinFull, linPart, nonLinPart)
        self.deactivateInput()

        self.showFull()
        self.showPart()

    def getString(self, b, factorsNum):
        nonlinStr = self.getNonlinStr(b, factorsNum)
        nonlinStrT = (nonlinStr % tuple(b))

        lin_regr_list = b[:(self.experiment.numFactors + 1)]
        pos = nonlinStr.find("x%d" % self.experiment.numFactors) + 2
        lin_regr_format_str = nonlinStr[:pos]
        lin_regr_str = (lin_regr_format_str % tuple(lin_regr_list))

        return lin_regr_str, nonlinStrT

    def getNonlinStr(self, regr, factors_number):
        x = []
        for i in range(self.experiment.numFactors):
            x.append("x%d" % (i + 1))

        res_str = "y = %.3f"
        pos = 1
        for i in range(1, factors_number + 1):
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
                pos += 1

        return res_str

    def show_check(self, res, widget):
        widget.addRow(res)

    def showFull(self):
        self.tableFull.show(self.matrFull)

    def showPart(self):
        self.tablePart.show(self.matrPart)


if __name__ == "__main__":
    app = QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
