# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TicTacToe.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from typing import Text
from PyQt5 import QtCore, QtGui, QtWidgets
import random
Turn = [0, 1]
PlayerTurn = random.choice(Turn)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(231, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:#4634A7;\n"
"color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pb1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click_btn("pb1"))
        self.pb1.setGeometry(QtCore.QRect(10, 70, 71, 71))
        self.pb1.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#pb1{\n"
"   border: 0px solid gray;\n"
"}\n"
"#pb1:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.pb1.setFont(font)
        self.pb1.setText("")
        self.pb1.setFlat(False)
        self.pb1.setObjectName("pb1")
        self.pb2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click_btn("pb2"))
        self.pb2.setGeometry(QtCore.QRect(80, 70, 71, 71))
        self.pb2.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#pb2{\n"
"   border: 0px solid gray;\n"
"}\n"
"#pb2:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        self.pb2.setFont(font)
        self.pb2.setText("")
        self.pb2.setFlat(False)
        self.pb2.setObjectName("pb2")
        self.pb3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click_btn("pb3"))
        self.pb3.setGeometry(QtCore.QRect(150, 70, 71, 71))
        self.pb3.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#pb3{\n"
"   border: 0px solid gray;\n"
"}\n"
"#pb3:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        self.pb3.setText("")
        self.pb3.setFlat(False)
        self.pb3.setObjectName("pb3")
        self.pb3.setFont(font)
        self.pb5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click_btn("pb5"))
        self.pb5.setGeometry(QtCore.QRect(80, 140, 71, 71))
        self.pb5.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#pb5{\n"
"   border: 0px solid gray;\n"
"}\n"
"#pb5:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        self.pb5.setFont(font)
        self.pb5.setText("")
        self.pb5.setFlat(False)
        self.pb5.setObjectName("pb5")
        self.pb6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click_btn("pb6"))
        self.pb6.setGeometry(QtCore.QRect(150, 140, 71, 71))
        self.pb6.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#pb6{\n"
"   border: 0px solid gray;\n"
"}\n"
"#pb6:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        self.pb6.setFont(font)
        self.pb6.setText("")
        self.pb6.setFlat(False)
        self.pb6.setObjectName("pb6")
        self.pb4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click_btn("pb4"))
        self.pb4.setGeometry(QtCore.QRect(10, 140, 71, 71))
        self.pb4.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#pb4{\n"
"   border: 0px solid gray;\n"
"}\n"
"#pb4:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        self.pb4.setFont(font)
        self.pb4.setText("")
        self.pb4.setFlat(False)
        self.pb4.setObjectName("pb4")
        self.pb8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click_btn("pb8"))
        self.pb8.setGeometry(QtCore.QRect(80, 210, 71, 71))
        self.pb8.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#pb8{\n"
"   border: 0px solid gray;\n"
"}\n"
"#pb8:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        self.pb8.setFont(font)
        self.pb8.setText("")
        self.pb8.setFlat(False)
        self.pb8.setObjectName("pb8")
        self.pb9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click_btn("pb9"))
        self.pb9.setGeometry(QtCore.QRect(150, 210, 71, 71))
        self.pb9.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#pb9{\n"
"   border: 0px solid gray;\n"
"}\n"
"#pb9:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        self.pb9.setFont(font)
        self.pb9.setText("")
        self.pb9.setFlat(False)
        self.pb9.setObjectName("pb9")
        self.pb7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click_btn("pb7"))
        self.pb7.setGeometry(QtCore.QRect(10, 210, 71, 71))
        self.pb7.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#pb7{\n"
"   border: 0px solid gray;\n"
"}\n"
"#pb7:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        self.pb7.setFont(font)
        self.pb7.setText("")
        self.pb7.setFlat(False)
        self.pb7.setObjectName("pb7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 70, 1, 210))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(150, 70, 1, 210))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 140, 211, 1))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 210, 211, 1))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.reset_btn_click())
        self.reset_btn.setGeometry(QtCore.QRect(10, 290, 211, 31))
        self.reset_btn.setStyleSheet("/* Digits 0-9 Stylesheet */\n"
"#reset_btn{\n"
"   border: 1px solid gray;\n"
"}\n"
"#reset_btn:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* End Digits 0-9 Stylesheet */")
        self.reset_btn.setObjectName("reset_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 330, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(14, 18, 108);\n"
"color:white;")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 370, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgb(14, 18, 108);\n"
"color:white;")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if PlayerTurn == 1:
            self.label_2.setText("X's Turn")
        else:
            self.label_2.setText("O's Turn")
    def disable_btn(self):
        self.pb1.setEnabled(False)
        self.pb2.setEnabled(False)
        self.pb3.setEnabled(False)
        self.pb4.setEnabled(False)
        self.pb5.setEnabled(False)
        self.pb6.setEnabled(False)
        self.pb7.setEnabled(False)
        self.pb8.setEnabled(False)
        self.pb9.setEnabled(False)
    def win_check(self):
        if (self.pb1.text() == self.pb2.text() == self.pb3.text() == "O"):
            self.label_3.setText("O is the winner")
            self.disable_btn()
        elif (self.pb1.text() == self.pb4.text() == self.pb7.text() == "O"):
            self.label_3.setText("O is the winner")
            self.disable_btn()
        elif (self.pb1.text() == self.pb5.text() == self.pb9.text() == "O"):
            self.label_3.setText("O is the winner")
            self.disable_btn()
        elif (self.pb4.text() == self.pb5.text() == self.pb6.text() == "O"):
            self.label_3.setText("O is the winner")
            self.disable_btn()
        elif (self.pb7.text() == self.pb8.text() == self.pb9.text() == "O"):
            self.label_3.setText("O is the winner")
            self.disable_btn()
        elif (self.pb2.text() == self.pb5.text() == self.pb8.text() == "O"):
            self.label_3.setText("O is the winner")
            self.disable_btn()
        elif (self.pb3.text() == self.pb6.text() == self.pb9.text() == "O"):
            self.label_3.setText("O is the winner")
            self.disable_btn()
        elif (self.pb3.text() == self.pb5.text() == self.pb7.text() == "O"):
            self.label_3.setText("O is the winner")
            self.disable_btn()

        elif (self.pb1.text() == self.pb2.text() == self.pb3.text() == "X"):
            self.label_3.setText("X is the winner")
            self.disable_btn()
        elif (self.pb1.text() == self.pb4.text() == self.pb7.text() == "X"):
            self.label_3.setText("X is the winner")
            self.disable_btn()
        elif (self.pb1.text() == self.pb5.text() == self.pb9.text() == "X"):
            self.label_3.setText("X is the winner")
            self.disable_btn()
        elif (self.pb4.text() == self.pb5.text() == self.pb6.text() == "X"):
            self.label_3.setText("X is the winner")
            self.disable_btn()
        elif (self.pb7.text() == self.pb8.text() == self.pb9.text() == "X"):
            self.label_3.setText("X is the winner")
            self.disable_btn()
        elif (self.pb2.text() == self.pb5.text() == self.pb8.text() == "X"):
            self.label_3.setText("X is the winner")
            self.disable_btn()
        elif (self.pb3.text() == self.pb6.text() == self.pb9.text() == "X"):
            self.label_3.setText("X is the winner")
            self.disable_btn()
        elif (self.pb3.text() == self.pb5.text() == self.pb7.text() == "X"):
            self.label_3.setText("X is the winner")
            self.disable_btn()
        else:
            if(
                (self.pb1.text() != "") and
                (self.pb2.text() != "") and
                (self.pb3.text() != "") and
                (self.pb4.text() != "") and
                (self.pb5.text() != "") and
                (self.pb6.text() != "") and
                (self.pb7.text() != "") and
                (self.pb8.text() != "") and
                (self.pb9.text() != "")):
                self.label_3.setText("Match Tie")
    def click_btn(self, btn):
        global PlayerTurn
        if PlayerTurn == 0:
            if btn == "pb1":
                self.pb1.setText("O")
                self.pb1.setEnabled(False)
                PlayerTurn = 1
                self.win_check()
                self.label_2.setText("X's Turn")
            elif btn == "pb2":
                self.pb2.setText("O")
                self.pb2.setEnabled(False)
                PlayerTurn = 1
                self.win_check()
                self.label_2.setText("X's Turn")
            elif btn == "pb3":
                self.pb3.setText("O")
                self.pb3.setEnabled(False)
                PlayerTurn = 1
                self.win_check()
                self.label_2.setText("X's Turn")
            elif btn == "pb4":
                self.pb4.setText("O")
                self.pb4.setEnabled(False)
                PlayerTurn = 1
                self.win_check()
                self.label_2.setText("X's Turn")
            elif btn == "pb5":
                self.pb5.setText("O")
                self.pb5.setEnabled(False)
                PlayerTurn = 1
                self.win_check()
                self.label_2.setText("X's Turn")
            elif btn == "pb6":
                self.pb6.setText("O")
                self.pb6.setEnabled(False)
                PlayerTurn = 1
                self.win_check()
                self.label_2.setText("X's Turn")
            elif btn == "pb7":
                self.pb7.setText("O")
                self.pb7.setEnabled(False)
                PlayerTurn = 1
                self.win_check()
                self.label_2.setText("X's Turn")
            elif btn == "pb8":
                self.pb8.setText("O")
                self.pb8.setEnabled(False)
                PlayerTurn = 1
                self.win_check()
                self.label_2.setText("X's Turn")
            elif btn == "pb9":
                self.pb9.setText("O")
                self.pb9.setEnabled(False)
                PlayerTurn = 1
                self.win_check()
                self.label_2.setText("X's Turn")
        elif PlayerTurn == 1:
            if btn == "pb1":
                self.pb1.setText("X")
                self.pb1.setEnabled(False)
                PlayerTurn = 0
                self.win_check()
                self.label_2.setText("O's Turn")
            elif btn == "pb2":
                self.pb2.setText("X")
                self.pb2.setEnabled(False)
                PlayerTurn = 0
                self.win_check()
                self.label_2.setText("O's Turn")
            elif btn == "pb3":
                self.pb3.setText("X")
                self.pb3.setEnabled(False)
                PlayerTurn = 0
                self.win_check()
                self.label_2.setText("O's Turn")
            elif btn == "pb4":
                self.pb4.setText("X")
                self.pb4.setEnabled(False)
                PlayerTurn = 0
                self.win_check()
                self.label_2.setText("O's Turn")
            elif btn == "pb5":
                self.pb5.setText("X")
                self.pb5.setEnabled(False)
                PlayerTurn = 0
                self.win_check()
                self.label_2.setText("O's Turn")
            elif btn == "pb6":
                self.pb6.setText("X")
                self.pb6.setEnabled(False)
                PlayerTurn = 0
                self.win_check()
                self.label_2.setText("O's Turn")
            elif btn == "pb7":
                self.pb7.setText("X")
                self.pb7.setEnabled(False)
                PlayerTurn = 0
                self.win_check()
                self.label_2.setText("O's Turn")
            elif btn == "pb8":
                self.pb8.setText("X")
                self.pb8.setEnabled(False)
                PlayerTurn = 0
                self.win_check()
                self.label_2.setText("O's Turn")
            elif btn == "pb9":
                self.pb9.setText("X")
                self.pb9.setEnabled(False)
                PlayerTurn = 0
                self.win_check()
                self.label_2.setText("O's Turn")
    def reset_btn_click(self):
        global PlayerTurn
        self.pb1.setText("")
        self.pb1.setEnabled(True)
        self.pb2.setText("")
        self.pb2.setEnabled(True)
        self.pb3.setText("")
        self.pb3.setEnabled(True)
        self.pb4.setText("")
        self.pb4.setEnabled(True)
        self.pb5.setText("")
        self.pb5.setEnabled(True)
        self.pb6.setText("")
        self.pb6.setEnabled(True)
        self.pb7.setText("")
        self.pb7.setEnabled(True)
        self.pb8.setText("")
        self.pb8.setEnabled(True)
        self.pb9.setText("")
        self.pb9.setEnabled(True)
        self.label_3.setText("")
        Turn = [0, 1]
        PlayerTurn = random.choice(Turn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TIC TAC TOE"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
