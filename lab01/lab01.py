import sys
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

from gui import Ui_mainwindow
from Distributions import ExponentGenerator, WeibullGenerator
from Generator import Generator
from Processor import Processor
from Model import Model


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)

        self.ui.IG1.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.IG1))
        self.ui.IO1.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.IO1))
        self.ui.IG2.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.IG2))
        self.ui.IO2.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.IO2))
        self.ui.IG3.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.IG3))
        self.ui.IO3.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.IO3))

        self.ui.timeM.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.timeM))
        self.ui.num.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.num))

        self.ui.addIG2.clicked.connect(self.addIG2)
        self.ui.addIG3.clicked.connect(self.addIG3)

        self.ui.addIO2.clicked.connect(self.addIO2)
        self.ui.addIO3.clicked.connect(self.addIO3)

        self.ui.delIG2.clicked.connect(self.delIG2)
        self.ui.delIG3.clicked.connect(self.delIG3)

        self.ui.delIO2.clicked.connect(self.delIO2)
        self.ui.delIO3.clicked.connect(self.delIO3)

        self.ui.DoModeling.clicked.connect(self.doModeling)
        self.ui.DoGraph.clicked.connect(self.doGraph)

    def addIG2(self):
        self.ui.IG2.setEnabled(True)
        self.ui.addIG3.setEnabled(True)
        self.ui.delIG2.setEnabled(True)

    def addIG3(self):
        self.ui.IG3.setEnabled(True)
        self.ui.delIG3.setEnabled(True)

    def addIO2(self):
        self.ui.IO2.setEnabled(True)
        self.ui.addIO3.setEnabled(True)
        self.ui.delIO2.setEnabled(True)

    def addIO3(self):
        self.ui.IO3.setEnabled(True)
        self.ui.delIO3.setEnabled(True)

    def delIG2(self):
        self.ui.IG2.setEnabled(False)
        self.ui.addIG3.setEnabled(False)
        self.ui.delIG2.setEnabled(False)

    def delIG3(self):
        self.ui.IG3.setEnabled(False)
        self.ui.delIG3.setEnabled(False)

    def delIO2(self):
        self.ui.IO2.setEnabled(False)
        self.ui.addIO3.setEnabled(False)
        self.ui.delIO2.setEnabled(False)

    def delIO3(self):
        self.ui.IO3.setEnabled(False)
        self.ui.delIO3.setEnabled(False)

    def addToTable(self, row, col, val):
        item = QTableWidgetItem()
        item.setText(str(val))
        self.ui.tableWidget.setItem(row, col, item)

    def doModeling(self):
        genArr, procArr = [], []
        try:
            intGen1 = float(self.ui.IG1.text())
            intGenSum = intGen1
            genArr.append(Generator(ExponentGenerator(intGen1)))

            intProc1 = float(self.ui.IO1.text())
            intProcSum = intProc1
            procArr.append(Processor(WeibullGenerator(2, intProc1)))

            intGen2, intProc2 = None, None
            intGen3, intProc3 = None, None
            if self.ui.IG2.isEnabled():
                intGen2 = float(self.ui.IG2.text())
                intGenSum += intGen2
                genArr.append(Generator(ExponentGenerator(intGen2)))
            if self.ui.IO2.isEnabled():
                intProc2 = float(self.ui.IO2.text())
                intProcSum += intProc2
                procArr.append(Processor(WeibullGenerator(2, intProc2)))

            if self.ui.IG3.isEnabled():
                intGen3 = float(self.ui.IG2.text())
                intGenSum += intGen3
                genArr.append(Generator(ExponentGenerator(intGen3)))
            if self.ui.IO3.isEnabled():
                intProc3 = float(self.ui.IO2.text())
                intProcSum += intProc3
                procArr.append(Processor(WeibullGenerator(2, intProc3)))

            try:
                taskNum = int(self.ui.num.text())
            except:
                taskNum = None

            try:
                timeModeling = float(self.ui.timeM.text())
            except:
                timeModeling = None

            model = Model(genArr, procArr)
            res = model.doModeling(taskNum, timeModeling)

            pTeor = intGenSum / intProcSum

            self.addToTable(0, 0, round(pTeor, 3))
            self.addToTable(0, 1, round(res['timeLoad'], 4))
            '''self.addToTable(1, 0, "-----")
            self.addToTable(1, 1, round(res['endTime'], 3))
            self.addToTable(2, 0, "-----")
            self.addToTable(2, 1, res['sizeQMax'])
            self.addToTable(3, 0, "-----")
            self.addToTable(3, 1, round(res['avgWait'], 3))'''

        except Exception as e:
            msg = QMessageBox()
            msg.setText('ОШИБКА!\n' + repr(e))
            msg.show()
            msg.exec()

    def doGraph(self):
        i = 0.001
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
        plt.show()


if __name__ == "__main__":
    app = QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
