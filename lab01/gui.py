# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(800, 600)
        self.layoutWidget = QtWidgets.QWidget(mainwindow)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 550, 279))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(10, 5, 10, 10)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 2)
        self.addI3 = QtWidgets.QPushButton(self.layoutWidget)
        self.addI3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.addI3.setFont(font)
        self.addI3.setIconSize(QtCore.QSize(16, 16))
        self.addI3.setObjectName("addI3")
        self.gridLayout.addWidget(self.addI3, 2, 3, 1, 1)
        self.delI3 = QtWidgets.QPushButton(self.layoutWidget)
        self.delI3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.delI3.setFont(font)
        self.delI3.setIconSize(QtCore.QSize(16, 16))
        self.delI3.setObjectName("delI3")
        self.gridLayout.addWidget(self.delI3, 3, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 3)
        self.delI2 = QtWidgets.QPushButton(self.layoutWidget)
        self.delI2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.delI2.setFont(font)
        self.delI2.setIconSize(QtCore.QSize(16, 16))
        self.delI2.setObjectName("delI2")
        self.gridLayout.addWidget(self.delI2, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.IG1 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IG1.setFont(font)
        self.IG1.setText("")
        self.IG1.setObjectName("IG1")
        self.gridLayout.addWidget(self.IG1, 1, 1, 1, 1)
        self.IO1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.IO1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IO1.setFont(font)
        self.IO1.setText("")
        self.IO1.setObjectName("IO1")
        self.gridLayout.addWidget(self.IO1, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(236, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.IG2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.IG2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IG2.setFont(font)
        self.IG2.setText("")
        self.IG2.setObjectName("IG2")
        self.gridLayout.addWidget(self.IG2, 2, 1, 1, 1)
        self.IG3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.IG3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IG3.setFont(font)
        self.IG3.setText("")
        self.IG3.setObjectName("IG3")
        self.gridLayout.addWidget(self.IG3, 3, 1, 1, 1)
        self.IO2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.IO2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IO2.setFont(font)
        self.IO2.setText("")
        self.IO2.setObjectName("IO2")
        self.gridLayout.addWidget(self.IO2, 2, 2, 1, 1)
        self.IO3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.IO3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IO3.setFont(font)
        self.IO3.setText("")
        self.IO3.setObjectName("IO3")
        self.gridLayout.addWidget(self.IO3, 3, 2, 1, 1)
        self.addI2 = QtWidgets.QPushButton(self.layoutWidget)
        self.addI2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.addI2.setFont(font)
        self.addI2.setIconSize(QtCore.QSize(16, 16))
        self.addI2.setObjectName("addI2")
        self.gridLayout.addWidget(self.addI2, 1, 3, 1, 1)
        self.timeM = QtWidgets.QLineEdit(self.layoutWidget)
        self.timeM.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeM.setFont(font)
        self.timeM.setText("")
        self.timeM.setObjectName("timeM")
        self.gridLayout.addWidget(self.timeM, 4, 3, 1, 1)
        self.num = QtWidgets.QLineEdit(self.layoutWidget)
        self.num.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.num.setFont(font)
        self.num.setObjectName("num")
        self.gridLayout.addWidget(self.num, 5, 3, 1, 1)
        self.DoModeling = QtWidgets.QPushButton(mainwindow)
        self.DoModeling.setGeometry(QtCore.QRect(610, 90, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DoModeling.setFont(font)
        self.DoModeling.setObjectName("DoModeling")
        self.DoGraph = QtWidgets.QPushButton(mainwindow)
        self.DoGraph.setGeometry(QtCore.QRect(610, 150, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DoGraph.setFont(font)
        self.DoGraph.setObjectName("DoGraph")
        self.label_7 = QtWidgets.QLabel(mainwindow)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 131, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(mainwindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 370, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(52)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "mainwindow"))
        self.label_4.setText(_translate("mainwindow", "Время моделирования:"))
        self.addI3.setText(_translate("mainwindow", "+"))
        self.delI3.setText(_translate("mainwindow", "×"))
        self.label_5.setText(_translate("mainwindow", "Количество обрабатываемых заявок:"))
        self.delI2.setText(_translate("mainwindow", "×"))
        self.label_3.setText(_translate("mainwindow", "Интенсивность:"))
        self.label.setText(_translate("mainwindow", "Генератор"))
        self.label_2.setText(_translate("mainwindow", "ОА"))
        self.addI2.setText(_translate("mainwindow", "+"))
        self.num.setText(_translate("mainwindow", "1000"))
        self.DoModeling.setText(_translate("mainwindow", "Моделировать"))
        self.DoGraph.setText(_translate("mainwindow", "График tож(ρ)"))
        self.label_7.setText(_translate("mainwindow", "Итог:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("mainwindow", "Загрузка системы"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("mainwindow", "Что-то ещё"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainwindow", "Теор."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainwindow", "Факт."))