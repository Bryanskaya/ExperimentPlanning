import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

from gui import Ui_mainwindow


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)

        self.ui.IG1.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.IG1))
        self.ui.IO1.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.IO1))
        self.ui.IG2.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.IG2))
        self.ui.IO2.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.IO2))
        self.ui.IG3.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.IG3))
        self.ui.IO3.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.IO3))

        self.ui.timeM.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.timeM))
        self.ui.num.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]*"), self.ui.num))

        self.ui.addI2.clicked.connect(self.addI2)
        self.ui.addI3.clicked.connect(self.addI3)
        self.ui.delI2.clicked.connect(self.delI2)
        self.ui.delI3.clicked.connect(self.delI3)

        self.ui.DoModeling.clicked.connect(self.doModeling)
        self.ui.DoGraph.clicked.connect(self.doGraph)

    def addI2(self):
        self.ui.IG2.setEnabled(True)
        self.ui.IO2.setEnabled(True)
        self.ui.addI3.setEnabled(True)
        self.ui.delI2.setEnabled(True)

    def delI2(self):
        self.ui.IG2.setEnabled(False)
        self.ui.IO2.setEnabled(False)
        self.ui.addI3.setEnabled(False)
        self.ui.delI2.setEnabled(False)

    def addI3(self):
        self.ui.IG3.setEnabled(True)
        self.ui.IO3.setEnabled(True)
        self.ui.delI3.setEnabled(True)

    def delI3(self):
        self.ui.IG3.setEnabled(False)
        self.ui.IO3.setEnabled(False)
        self.ui.delI3.setEnabled(False)

    def addToTable(self, row, col, val):
        item = QTableWidgetItem()
        item.setText(str(val))
        self.ui.tableWidget.setItem(row, col, item)

    def doModeling(self):
        try:
            intGen1 = int(self.ui.IG1.text())
            intGenSum = intGen1
            intProc1 = int(self.ui.IO1.text())
            intProcSum = intProc1

            intGen2, intProc2 = None, None
            intGen3, intProc3 = None, None
            genNum = 1
            if self.ui.IG2.isEnabled():
                intGen2 = int(self.ui.IG2.text())
                intGenSum += intGen2
                intProc2 = int(self.ui.IO2.text())
                intProcSum += intProc2

                genNum += 1

            if self.ui.IG3.isEnabled():
                intGen3 = int(self.ui.IG2.text())
                intGenSum += intGen3
                intProc3 = int(self.ui.IO2.text())
                intProcSum += intProc3

                genNum += 1

            timeModeling = int(self.ui.timeM.text())
            taskNum = int(self.ui.num.text())

            

            pTeor = float(intGenSum / intProcSum)

            self.addToTable(1, 0, round(pTeor, 3))

        except Exception as e:
            msg = QMessageBox()
            msg.setText('ОШИБКА!\n' + repr(e))
            msg.show()
            msg.exec()

    def doGraph(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
