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
        mainwindow.resize(1235, 802)
        self.layoutWidget = QtWidgets.QWidget(mainwindow)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1201, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(10, 5, 10, 10)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.maxG1 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maxG1.setFont(font)
        self.maxG1.setObjectName("maxG1")
        self.gridLayout.addWidget(self.maxG1, 2, 2, 1, 1)
        self.x2D = QtWidgets.QLineEdit(self.layoutWidget)
        self.x2D.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x2D.setFont(font)
        self.x2D.setObjectName("x2D")
        self.gridLayout.addWidget(self.x2D, 3, 5, 1, 1)
        self.minG1 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.minG1.setFont(font)
        self.minG1.setObjectName("minG1")
        self.gridLayout.addWidget(self.minG1, 2, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 5, 3, 1, 1)
        self.minG2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.minG2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.minG2.setFont(font)
        self.minG2.setObjectName("minG2")
        self.gridLayout.addWidget(self.minG2, 3, 1, 1, 1)
        self.x4D = QtWidgets.QLineEdit(self.layoutWidget)
        self.x4D.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x4D.setFont(font)
        self.x4D.setObjectName("x4D")
        self.gridLayout.addWidget(self.x4D, 5, 5, 1, 1)
        self.x1F = QtWidgets.QLineEdit(self.layoutWidget)
        self.x1F.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x1F.setFont(font)
        self.x1F.setObjectName("x1F")
        self.gridLayout.addWidget(self.x1F, 2, 4, 1, 1)
        self.ShowMatrixF = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ShowMatrixF.setFont(font)
        self.ShowMatrixF.setObjectName("ShowMatrixF")
        self.gridLayout.addWidget(self.ShowMatrixF, 7, 4, 1, 1)
        self.x2F = QtWidgets.QLineEdit(self.layoutWidget)
        self.x2F.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x2F.setFont(font)
        self.x2F.setObjectName("x2F")
        self.gridLayout.addWidget(self.x2F, 3, 4, 1, 1)
        self.x4F = QtWidgets.QLineEdit(self.layoutWidget)
        self.x4F.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x4F.setFont(font)
        self.x4F.setObjectName("x4F")
        self.gridLayout.addWidget(self.x4F, 5, 4, 1, 1)
        self.minP1 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.minP1.setFont(font)
        self.minP1.setObjectName("minP1")
        self.gridLayout.addWidget(self.minP1, 4, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 0, 1, 1)
        self.numTasks = QtWidgets.QLineEdit(self.layoutWidget)
        self.numTasks.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.numTasks.setFont(font)
        self.numTasks.setObjectName("numTasks")
        self.gridLayout.addWidget(self.numTasks, 1, 8, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(236, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.maxP1 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maxP1.setFont(font)
        self.maxP1.setObjectName("maxP1")
        self.gridLayout.addWidget(self.maxP1, 4, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.CheckingF = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CheckingF.setFont(font)
        self.CheckingF.setObjectName("CheckingF")
        self.gridLayout.addWidget(self.CheckingF, 6, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 3, 1, 1)
        self.ShowMatrixD = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ShowMatrixD.setFont(font)
        self.ShowMatrixD.setObjectName("ShowMatrixD")
        self.gridLayout.addWidget(self.ShowMatrixD, 7, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 7, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 4, 1, 2)
        self.x1D = QtWidgets.QLineEdit(self.layoutWidget)
        self.x1D.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x1D.setFont(font)
        self.x1D.setObjectName("x1D")
        self.gridLayout.addWidget(self.x1D, 2, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 6, 1, 1)
        self.x3F = QtWidgets.QLineEdit(self.layoutWidget)
        self.x3F.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x3F.setFont(font)
        self.x3F.setObjectName("x3F")
        self.gridLayout.addWidget(self.x3F, 4, 4, 1, 1)
        self.x3D = QtWidgets.QLineEdit(self.layoutWidget)
        self.x3D.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x3D.setFont(font)
        self.x3D.setObjectName("x3D")
        self.gridLayout.addWidget(self.x3D, 4, 5, 1, 1)
        self.CheckingD = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CheckingD.setFont(font)
        self.CheckingD.setObjectName("CheckingD")
        self.gridLayout.addWidget(self.CheckingD, 6, 5, 1, 1)
        self.minP2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.minP2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.minP2.setFont(font)
        self.minP2.setObjectName("minP2")
        self.gridLayout.addWidget(self.minP2, 5, 1, 1, 1)
        self.timeM = QtWidgets.QLineEdit(self.layoutWidget)
        self.timeM.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeM.setFont(font)
        self.timeM.setText("")
        self.timeM.setObjectName("timeM")
        self.gridLayout.addWidget(self.timeM, 2, 8, 1, 1)
        self.maxP2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.maxP2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maxP2.setFont(font)
        self.maxP2.setObjectName("maxP2")
        self.gridLayout.addWidget(self.maxP2, 5, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 4, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 1, 5, 1, 1)
        self.maxG2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.maxG2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maxG2.setFont(font)
        self.maxG2.setObjectName("maxG2")
        self.gridLayout.addWidget(self.maxG2, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 7, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 8, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(236, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 8, 5, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 8, 4, 1, 1)
        self.DoModeling = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DoModeling.setFont(font)
        self.DoModeling.setObjectName("DoModeling")
        self.gridLayout.addWidget(self.DoModeling, 4, 7, 1, 2)
        self.label_7 = QtWidgets.QLabel(mainwindow)
        self.label_7.setGeometry(QtCore.QRect(10, 420, 291, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.linearF = QtWidgets.QTextEdit(mainwindow)
        self.linearF.setEnabled(False)
        self.linearF.setGeometry(QtCore.QRect(10, 450, 1201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.linearF.setFont(font)
        self.linearF.setObjectName("linearF")
        self.nonlinearF = QtWidgets.QTextEdit(mainwindow)
        self.nonlinearF.setEnabled(False)
        self.nonlinearF.setGeometry(QtCore.QRect(10, 540, 1201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nonlinearF.setFont(font)
        self.nonlinearF.setObjectName("nonlinearF")
        self.label_17 = QtWidgets.QLabel(mainwindow)
        self.label_17.setGeometry(QtCore.QRect(10, 510, 301, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_13 = QtWidgets.QLabel(mainwindow)
        self.label_13.setGeometry(QtCore.QRect(10, 610, 291, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_23 = QtWidgets.QLabel(mainwindow)
        self.label_23.setGeometry(QtCore.QRect(10, 700, 301, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.nonlinearD = QtWidgets.QTextEdit(mainwindow)
        self.nonlinearD.setEnabled(False)
        self.nonlinearD.setGeometry(QtCore.QRect(10, 730, 1201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nonlinearD.setFont(font)
        self.nonlinearD.setObjectName("nonlinearD")
        self.linearD = QtWidgets.QTextEdit(mainwindow)
        self.linearD.setEnabled(False)
        self.linearD.setGeometry(QtCore.QRect(10, 640, 1201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.linearD.setFont(font)
        self.linearD.setObjectName("linearD")

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)
        mainwindow.setTabOrder(self.minG1, self.maxG1)
        mainwindow.setTabOrder(self.maxG1, self.minG2)
        mainwindow.setTabOrder(self.minG2, self.maxG2)
        mainwindow.setTabOrder(self.maxG2, self.minP1)
        mainwindow.setTabOrder(self.minP1, self.maxP1)
        mainwindow.setTabOrder(self.maxP1, self.minP2)
        mainwindow.setTabOrder(self.minP2, self.maxP2)
        mainwindow.setTabOrder(self.maxP2, self.DoModeling)
        mainwindow.setTabOrder(self.DoModeling, self.x1F)
        mainwindow.setTabOrder(self.x1F, self.x2F)
        mainwindow.setTabOrder(self.x2F, self.x3F)
        mainwindow.setTabOrder(self.x3F, self.x4F)
        mainwindow.setTabOrder(self.x4F, self.CheckingF)
        mainwindow.setTabOrder(self.CheckingF, self.ShowMatrixF)
        mainwindow.setTabOrder(self.ShowMatrixF, self.x1D)
        mainwindow.setTabOrder(self.x1D, self.x2D)
        mainwindow.setTabOrder(self.x2D, self.x3D)
        mainwindow.setTabOrder(self.x3D, self.x4D)
        mainwindow.setTabOrder(self.x4D, self.CheckingD)
        mainwindow.setTabOrder(self.CheckingD, self.ShowMatrixD)
        mainwindow.setTabOrder(self.ShowMatrixD, self.numTasks)
        mainwindow.setTabOrder(self.numTasks, self.timeM)
        mainwindow.setTabOrder(self.timeM, self.linearF)
        mainwindow.setTabOrder(self.linearF, self.nonlinearF)
        mainwindow.setTabOrder(self.nonlinearF, self.linearD)
        mainwindow.setTabOrder(self.linearD, self.nonlinearD)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "mainwindow"))
        self.maxG1.setText(_translate("mainwindow", "2"))
        self.x2D.setText(_translate("mainwindow", "0"))
        self.minG1.setText(_translate("mainwindow", "1"))
        self.label_20.setText(_translate("mainwindow", "ОА (2 тип)"))
        self.label_24.setText(_translate("mainwindow", "x4"))
        self.minG2.setText(_translate("mainwindow", "1.5"))
        self.x4D.setText(_translate("mainwindow", "0"))
        self.x1F.setText(_translate("mainwindow", "0"))
        self.ShowMatrixF.setText(_translate("mainwindow", "Матрица"))
        self.x2F.setText(_translate("mainwindow", "0"))
        self.x4F.setText(_translate("mainwindow", "0"))
        self.minP1.setText(_translate("mainwindow", "3"))
        self.label_14.setText(_translate("mainwindow", "Интенсивность"))
        self.label_19.setText(_translate("mainwindow", "ОА (1 тип)"))
        self.numTasks.setText(_translate("mainwindow", "500"))
        self.label_3.setText(_translate("mainwindow", "Генератор №1"))
        self.maxP1.setText(_translate("mainwindow", "5"))
        self.label_11.setText(_translate("mainwindow", "          x1"))
        self.label_6.setText(_translate("mainwindow", "min"))
        self.CheckingF.setText(_translate("mainwindow", "Проверить"))
        self.label_12.setText(_translate("mainwindow", "x2"))
        self.ShowMatrixD.setText(_translate("mainwindow", "Матрица"))
        self.label_10.setText(_translate("mainwindow", "Количество заявок:"))
        self.label_18.setText(_translate("mainwindow", "Точка"))
        self.x1D.setText(_translate("mainwindow", "0"))
        self.x3F.setText(_translate("mainwindow", "0"))
        self.x3D.setText(_translate("mainwindow", "0"))
        self.CheckingD.setText(_translate("mainwindow", "Проверить"))
        self.minP2.setText(_translate("mainwindow", "3.5"))
        self.maxP2.setText(_translate("mainwindow", "4"))
        self.label_8.setText(_translate("mainwindow", "max"))
        self.label_15.setText(_translate("mainwindow", "x3"))
        self.label_22.setText(_translate("mainwindow", "ДФЭ"))
        self.maxG2.setText(_translate("mainwindow", "2.5"))
        self.label_5.setText(_translate("mainwindow", "Время моделирования:"))
        self.label_21.setText(_translate("mainwindow", "ПФЭ"))
        self.label_2.setText(_translate("mainwindow", "Генератор №2"))
        self.DoModeling.setText(_translate("mainwindow", "Моделировать"))
        self.label_7.setText(_translate("mainwindow", "Линейная зависимость для ПФЭ:"))
        self.label_17.setText(_translate("mainwindow", "Нелинейная зависимость для ПФЭ:"))
        self.label_13.setText(_translate("mainwindow", "Линейная зависимость для ДФЭ:"))
        self.label_23.setText(_translate("mainwindow", "Нелинейная зависимость для ДФЭ:"))