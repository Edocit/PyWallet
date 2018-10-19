# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputTest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import time
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import platform as pltf
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(1238, 685)
        Window.setMinimumSize(QtCore.QSize(1238, 685))
        Window.setMaximumSize(QtCore.QSize(1238, 685))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("wal.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        Window.setAutoFillBackground(False)
        Window.setStyleSheet("background-color:gray;")
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{color:#dbac4e}")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.nome = QtWidgets.QLineEdit(self.centralwidget)
        self.nome.setEnabled(True)
        self.nome.setGeometry(QtCore.QRect(200, 30, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.nome.setPalette(palette)
        self.nome.setAutoFillBackground(False)
        self.nome.setStyleSheet("border:none;\n"
"background:transparent;\n"
"color:#ffffff;\n"
"")
        self.nome.setObjectName("nome")
        self.importo = QtWidgets.QLineEdit(self.centralwidget)
        self.importo.setGeometry(QtCore.QRect(200, 80, 141, 31))
        self.importo.setStyleSheet("border:none;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.importo.setText("")
        self.importo.setObjectName("importo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#dbac4e")
        self.label_2.setObjectName("label_2")
        self.addBtt = QtWidgets.QPushButton(self.centralwidget)
        self.addBtt.setGeometry(QtCore.QRect(190, 180, 131, 31))
        self.addBtt.setStyleSheet("background-color:green;\n"
"border-radius:10px;")
        self.addBtt.setObjectName("addBtt")
        self.removeBtt = QtWidgets.QPushButton(self.centralwidget)
        self.removeBtt.setGeometry(QtCore.QRect(40, 180, 121, 31))
        self.removeBtt.setStyleSheet("background-color:red;\n"
"text:white;\n"
"border-radius:10px;")
        self.removeBtt.setObjectName("removeBtt")
        self.listaSpese = QtWidgets.QListWidget(self.centralwidget)
        self.listaSpese.setGeometry(QtCore.QRect(30, 270, 500, 381))
        self.listaSpese.setMinimumSize(QtCore.QSize(500, 381))
        self.listaSpese.setMaximumSize(QtCore.QSize(411, 16777215))
        self.listaSpese.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listaSpese.setFont(font)
        self.listaSpese.setStyleSheet("background:transparent;\n"
"color:#ffffff;")
        self.listaSpese.setObjectName("listaSpese")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#dbac4e")
        self.label_3.setObjectName("label_3")
        self.dataSpesa = QtWidgets.QDateEdit(self.centralwidget)
        self.dataSpesa.setGeometry(QtCore.QRect(200, 130, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dataSpesa.setFont(font)
        self.dataSpesa.setStyleSheet("background:transparent;\n"
"color:#ffffff;")
        self.dataSpesa.setObjectName("dataSpesa")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 220, 581, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#dbac4e")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 60, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#dbac4e")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 90, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#dbac4e")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 120, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#dbac4e")
        self.label_8.setObjectName("label_8")
        self.yearGrandTotal = QtWidgets.QLabel(self.centralwidget)
        self.yearGrandTotal.setGeometry(QtCore.QRect(500, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yearGrandTotal.setFont(font)
        self.yearGrandTotal.setStyleSheet("border:none;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.yearGrandTotal.setText("")
        self.yearGrandTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearGrandTotal.setObjectName("yearGrandTotal")
        self.monthTotal = QtWidgets.QLabel(self.centralwidget)
        self.monthTotal.setGeometry(QtCore.QRect(510, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.monthTotal.setFont(font)
        self.monthTotal.setStyleSheet("border:none;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.monthTotal.setText("")
        self.monthTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.monthTotal.setObjectName("monthTotal")
        self.monthAvg = QtWidgets.QLabel(self.centralwidget)
        self.monthAvg.setGeometry(QtCore.QRect(530, 90, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.monthAvg.setFont(font)
        self.monthAvg.setStyleSheet("border:none;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.monthAvg.setText("")
        self.monthAvg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.monthAvg.setObjectName("monthAvg")
        self.yearAvg = QtWidgets.QLabel(self.centralwidget)
        self.yearAvg.setGeometry(QtCore.QRect(520, 120, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yearAvg.setFont(font)
        self.yearAvg.setStyleSheet("border:none;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.yearAvg.setText("")
        self.yearAvg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearAvg.setObjectName("yearAvg")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(630, 20, 41, 651))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(730, 50, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#dbac4e")
        self.label_9.setObjectName("label_9")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(340, 20, 20, 191))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.graphView = QtWidgets.QLabel(self.centralwidget)
        self.graphView.setGeometry(QtCore.QRect(690, 160, 521, 461))
        self.graphView.setMinimumSize(QtCore.QSize(521, 461))
        self.graphView.setMaximumSize(QtCore.QSize(521, 461))
        self.graphView.setFrameShape(QtWidgets.QFrame.Box)
        self.graphView.setText("")
        self.graphView.setObjectName("graphView")
        self.label.raise_()
        self.nome.raise_()
        self.importo.raise_()
        self.label_2.raise_()
        self.addBtt.raise_()
        self.removeBtt.raise_()
        self.label_3.raise_()
        self.listaSpese.raise_()
        self.dataSpesa.raise_()
        self.line.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.yearGrandTotal.raise_()
        self.monthTotal.raise_()
        self.monthAvg.raise_()
        self.yearAvg.raise_()
        self.line_2.raise_()
        self.label_9.raise_()
        self.line_3.raise_()
        self.graphView.raise_()
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)



        self.platform = pltf.system()
        self.nome.setText("")
        self.importo.setText("")
        self.restoreStatementAndHistory()
        self.yearTotal()
        self.monthGrandTotal()
        self.avgMonth()
        self.avgYear()
        self.monthList = [31,28,31,30,31,30,31,31,30,31,30,31] #lunghezza mesi 
        self.graphView = self.printGraph()
        self.addBtt.clicked.connect(self.addEntry)



    def restoreStatementAndHistory(self):
        conn = sqlite3.connect("Wallet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Spese")
        dataSet = cursor.fetchall()
        for el in dataSet:
            self.listaSpese.addItem(str(el[1]) + "    " + str(el[2])+" €")

    def addEntry(self):
        if str(self.nome.text()) != "" and str(self.importo.text()) != "":
            conn = sqlite3.connect("Wallet.db")
            cursor = conn.cursor()

            print(self.dataSpesa.text())

            if (str(self.dataSpesa.text()) == "01/01/2000" or str(self.dataSpesa.text()) == "01/01/00"):
                if "," in str(self.importo.text()):
                    self.importo.setText(str(self.importo.text()).replace(',', '.'))
                    if(str(self.platform) == "Linux"):
                        cursor.execute('''INSERT INTO Spese(Oggetto,Prezzo,Data) Values (?,?,?)''',
                               (str(self.nome.text()), str(self.importo.text()), str(time.strftime("%x"))))
                else:
                    cursor.execute('''INSERT INTO Spese(Oggetto,Prezzo,Data) Values (?,?,?)''',
                           (str(self.nome.text()), str(self.importo.text()), str(time.strftime("%d/%m/%Y"))))
            else:
                if "," in str(self.importo.text()):
                    self.importo.setText(str(self.importo.text()).replace(',', '.'))
                cursor.execute('''INSERT INTO Spese(Oggetto,Prezzo,Data) Values (?,?,?)''',
                               (str(self.nome.text()), str(self.importo.text()), str(self.dataSpesa.text())))
        conn.commit()
        conn.close()
        self.listaSpese.addItem(self.nome.text() + "    " + self.importo.text()+" €")
        self.nome.setText("")
        self.importo.setText("")
        self.yearTotal()
        self.monthGrandTotal()



    def deleteInsertion(self):
    	pass



    def yearTotal(self):
        total = 0
        conn = sqlite3.connect("Wallet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Spese")
        dataSet = cursor.fetchall()
        for cost in dataSet :
            op = cost[3].split('/')
            if (op[2] == str(time.strftime("%Y"))):
                total = total + float(cost[2])
        self.yearGrandTotal.setText(str(format(total,".2f"))+" €")

    def monthGrandTotal(self):
        total = 0
        conn = sqlite3.connect("Wallet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Spese")
        dataSet = cursor.fetchall()
        for cost in dataSet:
            op = cost[3].split('/')
            if op[1] == str(time.strftime("%m")) and op[2] == str(time.strftime("%Y")):
                total = total + float(cost[2])
        self.monthTotal.setText(str(format(total,".2f"))+" €")

    def avgMonth(self):
        total = 0
        count = 0
        conn = sqlite3.connect("Wallet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Spese")
        dataSet = cursor.fetchall()
        for cost in dataSet:
            if(str(cost[3].split("/")[1]) == str(time.strftime("%m"))  ):
                total += float(cost[2])
                count += 1
            else:
                count = 1
        try:
            self.monthAvg.setText(str(format((total/count),".2f"))+" €")
        except:
            self.monthAvg.setText("0 €")


    def avgYear(self):
        total = 0
        count = 0
        conn = sqlite3.connect("Wallet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Spese")
        dataSet = cursor.fetchall()
        for cost in dataSet:
            if(cost[3].split("/")[2] == str(time.strftime("%Y"))  ):
                total += float(cost[2])
                count += 1
        try:
            self.yearAvg.setText(str(format(total/count,".2f"))+" €")
        except:
            self.yearAvg.setText("0 €")


    def printGraph(self):
        month_len = 0
        month_import_list = []
        x_axis = []
        max_import = 0
        plt.xlabel("Data")
        plt.ylabel("Importo speso")
        current_year = int(time.strftime("%d/%m/%Y").split("/")[2])


        if(int(time.strftime("%d/%m/%Y").split("/")[1]) == 2):
            if(((current_year % 4 == 0 and current_year % 100 != 0) or current_year % 400 == 0)):
                month_len = self.monthList[int(time.strftime("%d/%m/%Y").split("/")[1])-1] + 1 #anno bisestile
        else:
            month_len = self.monthList[int(time.strftime("%d/%m/%Y").split("/")[1])-1]

        conn = sqlite3.connect("Wallet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Spese")
        dataSet = cursor.fetchall()

        #inizialmente la spesa di ogni giorno è 0
        for i in range(month_len):
            month_import_list.append(0.0)

        #creo la lista per l'asse X col tempo espresso in giorni 
        for i in range(1,(month_len + 1)):
            x_axis.append(i)

        for period in dataSet:
            if(str(period[3].split("/")[1]) == str(time.strftime("%d/%m/%Y").split("/")[1])):
                month_import_list[int(period[3].split("/")[0])-1] = float(period[2])
                if(month_import_list[int(period[3].split("/")[0])-1] > max_import):
                    max_import = month_import_list[int(period[3].split("/")[0])-1]



        #ora i dati sono pronti e normalizzati per poter essere stampati nel grafo x = [lista_giorni] y = [lista_importi_normalizzata]
        fig = plt.figure()
        plt.axis([0,month_len+1,0,max_import+10])
        plt.plot(x_axis,month_import_list)
        fig.savefig('.graph.png',dpi=fig.dpi)
        pixmap = QPixmap('.graph.png')
        pixmap= pixmap.scaled(521,461)
        self.graphView.setPixmap(pixmap)






        ##################






    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "PyWallet"))
        self.label.setText(_translate("Window", "Oggetto comprato "))
        self.nome.setPlaceholderText(_translate("Window", "Scrivi qui cosa hai comprato..."))
        self.importo.setPlaceholderText(_translate("Window", "Scrivi qui quanto hai speso..."))
        self.label_2.setText(_translate("Window", "Importo speso"))
        self.addBtt.setText(_translate("Window", "Aggiungi"))
        self.removeBtt.setText(_translate("Window", "Rimuovi"))
        self.label_3.setText(_translate("Window", "Data spesa"))
        self.label_5.setText(_translate("Window", "Totale anno"))
        self.label_6.setText(_translate("Window", "Totale mese"))
        self.label_7.setText(_translate("Window", "Media mensile"))
        self.label_8.setText(_translate("Window", "Media annuale"))
        self.label_9.setText(_translate("Window", "Grafico Spese"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

