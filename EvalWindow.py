# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvalWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_EvalWindow(object):
    def setupUi(self, EvalWindow):
        EvalWindow.setObjectName("EvalWindow")
        EvalWindow.resize(530, 453)
        EvalWindow.setMinimumSize(QtCore.QSize(530, 453))
        self.centralwidget = QtWidgets.QWidget(EvalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.CB_team = QtWidgets.QComboBox(self.centralwidget)
        self.CB_team.setObjectName("CB_team")
        self.CB_team.addItem("")
        self.gridLayout.addWidget(self.CB_team, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 2, 1)
        self.CB_match = QtWidgets.QComboBox(self.centralwidget)
        self.CB_match.setObjectName("CB_match")
        self.CB_match.addItem("")
        self.CB_match.addItem("Match1")
        self.gridLayout.addWidget(self.CB_match, 0, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.te_val = QtWidgets.QLineEdit(self.centralwidget)
        self.te_val.setReadOnly(True)
        self.te_val.setObjectName("te_val")
        self.horizontalLayout.addWidget(self.te_val)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 3, 1, 1)
        self.pla_list = QtWidgets.QListWidget(self.centralwidget)
        self.pla_list.setObjectName("pla_list")
        self.gridLayout.addWidget(self.pla_list, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.val_list = QtWidgets.QListWidget(self.centralwidget)
        self.val_list.setObjectName("val_list")
        self.gridLayout.addWidget(self.val_list, 2, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.evlbtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.evlbtn.setFont(font)
        self.evlbtn.setObjectName("evlbtn")
        self.evlbtn.clicked.connect(self.addpla_n_pts)
        self.gridLayout.addWidget(self.evlbtn, 4, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 3, 1, 1)
        EvalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EvalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 18))
        self.menubar.setObjectName("menubar")
        EvalWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EvalWindow)
        self.statusbar.setObjectName("statusbar")
        EvalWindow.setStatusBar(self.statusbar)
        cricket=sqlite3.connect('MyCricket.db')
        curcri=cricket.cursor()
        curcri.execute("SELECT DISTINCT Name FROM Teams") 
        data = curcri.fetchall()
        for name in data:
            self.CB_team.addItem(str(name[0]))
        cricket.close()

        self.retranslateUi(EvalWindow)
        QtCore.QMetaObject.connectSlotsByName(EvalWindow)

    def retranslateUi(self, EvalWindow):
        _translate = QtCore.QCoreApplication.translate
        EvalWindow.setWindowTitle(_translate("EvalWindow", "MainWindow"))
        self.CB_team.setItemText(0, _translate("EvalWindow", "Select Team"))
        self.CB_match.setItemText(0, _translate("EvalWindow", "Select Match"))
        self.label.setText(_translate("EvalWindow", "Points"))
        self.evlbtn.setText(_translate("EvalWindow", "EVALUATE"))

    def addpla_n_pts(self):
        self.pla_list.clear()
        self.val_list.clear()
        cricket=sqlite3.connect('MyCricket.db')
        curcri=cricket.cursor()
        te_points=0
        item = self.CB_team.currentText()
        print(item)
        curcri.execute("SELECT Players FROM Teams WHERE Name='"+item+"'") 
        data = curcri.fetchall()
        for name in data:
            temp=str(name[0])
            self.pla_list.addItem(str(name[0]))
            mat = self.CB_match.currentText()
            curcri.execute("SELECT Points FROM "+mat+" WHERE Player ='"+temp+"'")
            pts = curcri.fetchone()
            self.val_list.addItem(str(pts[0]))
            poo=int(str(pts[0]))
            te_points=te_points+poo
        self.te_val.setText(str(te_points))
        cricket.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvalWindow = QtWidgets.QMainWindow()
    ui = Ui_EvalWindow()
    ui.setupUi(EvalWindow)
    EvalWindow.show()
    sys.exit(app.exec_())
