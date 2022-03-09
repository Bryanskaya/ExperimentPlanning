import sys
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from typing import List

from gui import Ui_mainwindow
from process import Experiment
from resTable import ExcelTable


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.experiment = None

        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)

        self.ui.minG.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.minG))
        self.ui.maxG.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.maxG))
        self.ui.minP.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.minP))
        self.ui.maxP.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.maxP))
        self.ui.x1.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.x1))
        self.ui.x2.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.x2))
        self.ui.timeM.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.timeM))
        self.ui.numTasks.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.numTasks))

        self.ui.DoModeling.clicked.connect(self.doModeling)
        self.ui.Checking.clicked.connect(self.doChecking)

    def activateInput(self):
        self.ui.linear.setEnabled(True)
        self.ui.nonlinear.setEnabled(True)

    def deactivateInput(self):
        self.ui.linear.setEnabled(False)
        self.ui.nonlinear.setEnabled(False)

    def setEquations(self, strLin: str, strNonlin: str):
        self.ui.linear.setText(strLin)
        self.ui.nonlinear.setText(strNonlin)

    def doModeling(self):
        try:
            intGMin = float(self.ui.minG.text())
            intGMax = float(self.ui.maxG.text())
            intPMin = float(self.ui.minP.text())
            intPMax = float(self.ui.maxP.text())

            try:
                numTasks = int(self.ui.numTasks.text())
            except:
                numTasks = None

            try:
                timeModeling = float(self.ui.timeM.text())
            except:
                timeModeling = None

            self.experiment = Experiment([intGMin, intGMax], [intPMin, intPMax],
                                         numTasks, timeModeling)

            matr, a = self.experiment.run()
            self.demonstrateRes(matr, a)

        except Exception as e:
            msg = QMessageBox()
            msg.setText('ОШИБКА!\n' + repr(e))
            msg.show()
            msg.exec()

    def doChecking(self):
        pass
        '''i = 0.001
        avgArr = [0]
        xArr = [0]
        while i <= 1.01:
            tempArr = []
            for j in range(30):
                generator = Generator(ExponentGenerator(i))
                processor = Processor(WeibullGenerator(2, 1))
                model = Model([generator], [processor])
                avgTemp = model.doModeling(300, None)['avgWait']
                tempArr.append(avgTemp)
            if sum(tempArr) / len(tempArr) > avgArr[-1]:
                xArr.append(i)
                avgArr.append(sum(tempArr) / len(tempArr))
                i += 0.05
            print(i)

        plt.plot(xArr, avgArr)
        plt.grid(True)
        plt.title("I: Экспоненциальный закон; II: Вейбулла с парам.2")
        plt.ylabel('Среднее время ожидания заявки')
        plt.xlabel('Загрузка системы')
        plt.show()'''

    def demonstrateRes(self, matr: List[List[float]], a: List[float]):
        strLin = "y = %.3f + %.3fx1 + %.3fx2" % (a[0], a[1], a[2])
        strNonlin = "y = %.3f + %.3fx1 + %.3fx2 + %.3fx1x2" % (a[0], a[1], a[2], a[3])

        self.activateInput()
        self.setEquations(strLin, strNonlin)
        self.deactivateInput()

        self.tableExcel = ExcelTable('results.xlsx')
        self.tableExcel.create(matr)
        self.tableExcel.open()


if __name__ == "__main__":
    app = QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
