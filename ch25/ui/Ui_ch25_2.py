# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Course_Region\Python_Course_Example\ch25\ui\ch25_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.QLCD_Num = QtWidgets.QLCDNumber(self.centralwidget)
        self.QLCD_Num.setObjectName("QLCD_Num")
        self.verticalLayout.addWidget(self.QLCD_Num)
        self.QPB_Start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.QPB_Start.setFont(font)
        self.QPB_Start.setObjectName("QPB_Start")
        self.verticalLayout.addWidget(self.QPB_Start)
        self.QPB_Stop = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.QPB_Stop.setFont(font)
        self.QPB_Stop.setObjectName("QPB_Stop")
        self.verticalLayout.addWidget(self.QPB_Stop)
        self.QPB_Reset = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.QPB_Reset.setFont(font)
        self.QPB_Reset.setObjectName("QPB_Reset")
        self.verticalLayout.addWidget(self.QPB_Reset)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QPB_Start.setText(_translate("MainWindow", "開始"))
        self.QPB_Stop.setText(_translate("MainWindow", "停止"))
        self.QPB_Reset.setText(_translate("MainWindow", "歸零"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
