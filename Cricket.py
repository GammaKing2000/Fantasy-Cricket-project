
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 
import sqlite3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OpenDlg(QtWidgets.QDialog):

    def __init__(self):
        super(OpenDlg, self).__init__()

        self.normal = QtWidgets.QLineEdit()
        self.normal.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout = QtWidgets.QFormLayout()
        layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        layout.addRow('Team Name', self.normal)
        layout.addWidget(self.button_box)

        self.setLayout(layout)
        self.setWindowTitle("Open Team")
        self.setMinimumWidth(350)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Ui_MainWindow(object):
    batnum=0
    bownum=0
    arnum=0
    wknum=0
    flag=0
    check=1
    WKT=0
    kya=0
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bat = QtWidgets.QLineEdit(self.centralwidget)
        self.bat.setMaxLength(1)
        self.bat.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.bat.setReadOnly(True)
        self.bat.setObjectName("bat")
        self.horizontalLayout.addWidget(self.bat)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.bow = QtWidgets.QLineEdit(self.centralwidget)
        self.bow.setMaxLength(1)
        self.bow.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.bow.setReadOnly(True)
        self.bow.setObjectName("bow")
        self.horizontalLayout.addWidget(self.bow)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.ar = QtWidgets.QLineEdit(self.centralwidget)
        self.ar.setMaxLength(1)
        self.ar.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ar.setReadOnly(True)
        self.ar.setObjectName("ar")
        self.horizontalLayout.addWidget(self.ar)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.wk = QtWidgets.QLineEdit(self.centralwidget)
        self.wk.setMaxLength(1)
        self.wk.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.wk.setReadOnly(True)
        self.wk.setObjectName("wk")
        self.horizontalLayout.addWidget(self.wk)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.pt_avail = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_avail.setInputMask("")
        self.pt_avail.setMaxLength(4)
        self.pt_avail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.pt_avail.setReadOnly(True)
        self.pt_avail.setObjectName("pt_avail")
        self.gridLayout.addWidget(self.pt_avail, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rb1.setFont(font)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_3.addWidget(self.rb1)
        self.rb1.toggled.connect(self.change)
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rb2.setFont(font)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_3.addWidget(self.rb2)
        self.rb2.toggled.connect(self.change)
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rb3.setFont(font)
        self.rb3.setObjectName("rb3")
        self.rb3.toggled.connect(self.change)
        self.horizontalLayout_3.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rb4.setFont(font)
        self.rb4.setObjectName("rb4")
        self.rb4.toggled.connect(self.change)
        self.horizontalLayout_3.addWidget(self.rb4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.te_name = QtWidgets.QLineEdit(self.centralwidget)
        self.te_name.setObjectName("te_name")
        self.te_name.setText("***")
        self.horizontalLayout_5.addWidget(self.te_name)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 2, 1, 2)
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.itemDoubleClicked.connect(self.addList)
        self.list1.setObjectName("list1")
        self.gridLayout.addWidget(self.list1, 5, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.pt_used = QtWidgets.QLineEdit(self.centralwidget)
        self.pt_used.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.pt_used.setReadOnly(True)
        self.pt_used.setObjectName("pt_used")
        self.gridLayout.addWidget(self.pt_used, 2, 3, 1, 1)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setObjectName("list2")
        self.list2.itemDoubleClicked.connect(self.remList)
        self.gridLayout.addWidget(self.list2, 5, 2, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_team = QtWidgets.QAction(MainWindow)
        self.actionNEW_team.setObjectName("actionNEW_team")
        self.actionOPEN_team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_team.setObjectName("actionOPEN_team")
        self.actionSAVE_team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_team.setObjectName("actionSAVE_team")
        self.actionEVALUATE_team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_team.setObjectName("actionEVALUATE_team")
        self.menuManage_Teams.addAction(self.actionNEW_team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOPEN_team)
        self.menuManage_Teams.addAction(self.actionSAVE_team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEVALUATE_team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.label_3.setBuddy(self.bat)
        self.label_4.setBuddy(self.bow)
        self.label_2.setBuddy(self.ar)
        self.label.setBuddy(self.wk)
        self.label_6.setBuddy(self.pt_avail)
        self.label_7.setBuddy(self.te_name)
        self.label_5.setBuddy(self.pt_used)

        self.retranslateUi(MainWindow)
        self.wk.inputRejected.connect(self.list2.clearSelection)
        self.pt_avail.inputRejected.connect(self.list2.clearSelection)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.starter)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Batsman (BAT)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.label_2.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.label.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.label_6.setText(_translate("MainWindow", "Points Available"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOW"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.label_7.setText(_translate("MainWindow", "Team Name"))
        self.label_5.setText(_translate("MainWindow", "Points Used"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_team.setText(_translate("MainWindow", "NEW team"))
        self.actionOPEN_team.setText(_translate("MainWindow", "OPEN team"))
        self.actionSAVE_team.setText(_translate("MainWindow", "SAVE team"))
        self.actionEVALUATE_team.setText(_translate("MainWindow", "EVALUATE team"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    def starter(self, action):
        if (action.text())=='NEW team':
            self.list1.clear()
            self.list2.clear()
            self.te_name.setText("***")
            self.pt_avail.setText('1000')
            self.pt_used.setText('0')
            self.bat.setText('0')
            self.bow.setText('0')
            self.ar.setText('0')
            self.wk.setText('0')
            Ui_MainWindow.flag=1
            self.te_name.setReadOnly(False)
            cricket=sqlite3.connect('MyCricket.db')
            curcri=cricket.cursor()
            planame="SELECT Player FROM Stats"
            curcri.execute(planame)
            data = curcri.fetchall()
            for name in data:
                self.list1.addItem(str(name[0]))
            cricket.close()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if (action.text())=="OPEN team":
            self.list1.clear()
            self.list2.clear()
            Ui_MainWindow.batnum=0
            Ui_MainWindow.bownum=0
            Ui_MainWindow.arnum=0
            Ui_MainWindow.wknum=0
            Ui_MainWindow.flag=1
            print("**********************************************************************")
            print("DO NOT EXIT WITHOUT SAVING THE TEAM. LOSS OF DATA WILL OCCUR")
            print("**********************************************************************")
            cricket=sqlite3.connect('MyCricket.db')
            curcri=cricket.cursor()
            curcri.execute("SELECT DISTINCT Name FROM Teams") 
            data = curcri.fetchall()
            k=1
            for name in data: 
                print(k, ". ", str(name[0]))
                k=k+1
            cricket.close()
            print("Select one team from the above list")
            print("**********************************************************************")
            login = OpenDlg()
            if login.exec_():
                self.te_name.setText(login.normal.text())
            self.te_name.setReadOnly(True)
            tename = self.te_name.text()
            cricket=sqlite3.connect('MyCricket.db')
            curcri=cricket.cursor()
            curcri.execute("SELECT Players FROM Teams WHERE Name='"+tename+"'") 
            data = curcri.fetchall()
            for name in data:
                self.list2.addItem(str(name[0]))
            total_pts_used=0
            total_pts_avail=0
            for i in range(self.list2.count()):
                curcri.execute("SELECT Value FROM Stats WHERE Player='"+self.list2.item(i).text()+"';")
                num = curcri.fetchone()
                inum=int(str(num[0]))
                total_pts_used=total_pts_used+inum
            total_pts_avail=1000-total_pts_used
            self.pt_avail.setText(str(total_pts_avail))
            self.pt_used.setText(str(total_pts_used))
            for i in range(self.list2.count()):
                curcri.execute("SELECT CTG FROM Stats WHERE Player='"+self.list2.item(i).text()+"';")
                old_ctg=curcri.fetchone()
                if str(old_ctg[0])=='BAT':
                    Ui_MainWindow.batnum=Ui_MainWindow.batnum+1    
                if str(old_ctg[0])=='BWL':
                    Ui_MainWindow.bownum=Ui_MainWindow.bownum+1                       
                if str(old_ctg[0])=='AR':
                    Ui_MainWindow.arnum= Ui_MainWindow.arnum +1    
                if str(old_ctg[0])=='WK':
                    Ui_MainWindow.WKT+=1
                    Ui_MainWindow.wknum=Ui_MainWindow.wknum+ 1
            self.bat.setText(str(Ui_MainWindow.batnum))
            self.bow.setText(str(Ui_MainWindow.bownum))
            self.ar.setText(str(Ui_MainWindow.arnum))
            self.wk.setText(str(Ui_MainWindow.wknum))
            Ui_MainWindow.check=12
            cricket.close()
            opening=sqlite3.connect('MyCricket.db')
            opencri=opening.cursor()
            planame="SELECT Player FROM Stats"
            opencri.execute(planame)
            data = opencri.fetchall()
            for name in data:
                self.list1.addItem(str(name[0]))
            opening.close()
            Ui_MainWindow.kya=0
            deleting=sqlite3.connect('MyCricket.db')
            delcri=deleting.cursor()
            team_name = self.te_name.text()
            delcri.execute("DELETE FROM Teams WHERE Name='"+team_name+"'")
            deleting.commit()
            deleting.close()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if (action.text())=="SAVE team":
            if Ui_MainWindow.kya==0:
                if Ui_MainWindow.check==12:
                    for i in range(self.list2.count()):
                        team_name = self.te_name.text()
                        cricket=sqlite3.connect('MyCricket.db')
                        curcri=cricket.cursor()
                        curcri.execute("SELECT Points FROM Match1 WHERE Player ='"+self.list2.item(i).text()+"';")
                        pts = curcri.fetchone()
                        
                        ipts=int(str(pts[0]))
                        curcri.execute("INSERT INTO Teams (Name, Players, Value) VALUES(?,?,?);", (team_name, self.list2.item(i).text(), ipts))
                        cricket.commit()
                    cricket.close()
                    msg6=QMessageBox()
                    msg6.setWindowTitle("YAY!!")
                    msg6.setText("Team Saved")
                    msg6.setIcon(QMessageBox.Information)
                    x6=msg6.exec_()
                    print("**********************************************************************")
                else:
                    msg5 = QMessageBox()
                    msg5.setWindowTitle("ERROR!!!")
                    msg5.setText("You need to select 11 players to complete the team and save")
                    msg5.setIcon(QMessageBox.Critical)
                    x5=msg5.exec_()
            if Ui_MainWindow.kya==1:
                if Ui_MainWindow.check==12:
                    for i in range(self.list2.count()):
                        cricket=sqlite3.connect('MyCricket.db')
                        curcri=cricket.cursor()
                        curcri.execute("SELECT Points FROM Match1 WHERE Player ='"+self.list2.item(i).text()+"';")
                        pts = curcri.fetchone()
                        ipts=int(str(pts[0]))
                        curcri.execute("INSERT INTO Teams (Name, Players, Value) VALUES(?,?,?);", (team_name, self.list2.item(i).text(), ipts))
                        print(self.list2.item(i).text())                        
                        print(i, self.list2.item(i).text())
                        curcri.commit()
                    cricket.close()
                    msg6=QMessageBox()
                    msg6.setWindowTitle("YAY!!")
                    msg6.setText("Team Saved")
                    msg6.setIcon(QMessageBox.Information)
                    x6=msg6.exec_()
                    print("**********************************************************************")
                else:
                    msg5 = QMessageBox()
                    msg5.setWindowTitle("ERROR!!!")
                    msg5.setText("You need to select 11 players to complete the team and save")
                    msg5.setIcon(QMessageBox.Critical)
                    x5=msg5.exec_()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if (action.text())=="EVALUATE team":
            from EvalWindow import Ui_EvalWindow
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_EvalWindow()
            self.ui.setupUi(self.window)
            self.window.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def change(self):
        if Ui_MainWindow.flag==1:
            if self.rb1.isChecked()==True:
                self.list1.clear()
                cricket=sqlite3.connect('MyCricket.db')
                curcri=cricket.cursor()
                bat="SELECT Player FROM Stats WHERE CTG='BAT'"
                curcri.execute(bat)
                data=curcri.fetchall()
                for name in data:
                    self.list1.addItem(str(name[0]))
                cricket.close()
            if self.rb2.isChecked()==True:
                self.list1.clear()
                cricket=sqlite3.connect('MyCricket.db')
                curcri=cricket.cursor()
                bat="SELECT Player FROM Stats WHERE CTG='BWL'"
                curcri.execute(bat)
                data=curcri.fetchall()
                for name in data:
                    self.list1.addItem(str(name[0]))
                cricket.close()
            if self.rb3.isChecked()==True:
                self.list1.clear()
                cricket=sqlite3.connect('MyCricket.db')
                curcri=cricket.cursor()
                bat="SELECT Player FROM Stats WHERE CTG='AR'"
                curcri.execute(bat)
                data=curcri.fetchall()
                for name in data:
                    self.list1.addItem(str(name[0]))
                cricket.close()
            if self.rb4.isChecked()==True:
                self.list1.clear()
                cricket=sqlite3.connect('MyCricket.db')
                curcri=cricket.cursor()
                bat="SELECT Player FROM Stats WHERE CTG='WK'"
                curcri.execute(bat)
                data=curcri.fetchall()
                for name in data:
                    self.list1.addItem(str(name[0]))
                cricket.close()
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def addList(self, item):
        if self.te_name.text()!='***':
            if Ui_MainWindow.check<=11:
                self.list1.takeItem(self.list1.row(item))
                name=item.text()
                cricket=sqlite3.connect('MyCricket.db')
                curcri=cricket.cursor()
                data="SELECT Value FROM Stats WHERE Player='"+name+"';"
                curcri.execute(data)
                check=curcri.fetchone()
                val= str(check[0])
                cow=int(val)
                pts=int(self.pt_avail.text()) 
                temp=int(self.pt_used.text())
                used = pts-cow
                temp = cow + temp
                if used>=0:
                    self.pt_avail.setText(str(used))
                    self.pt_used.setText(str(temp))
                    data ="SELECT CTG FROM Stats WHERE Player='"+name+"';"
                    curcri.execute(data)
                    ctg=curcri.fetchone()
                    if str(ctg[0])=='BAT':
                        Ui_MainWindow.batnum=Ui_MainWindow.batnum+1
                        self.bat.setText(str(Ui_MainWindow.batnum))
                        self.list2.addItem(item.text())
                        Ui_MainWindow.check+=1
                        print(Ui_MainWindow.check-1, '. ', name, ' ', self.te_name.text())
                    if str(ctg[0])=='BWL':
                        Ui_MainWindow.bownum=Ui_MainWindow.bownum+1
                        self.bow.setText(str(Ui_MainWindow.bownum))
                        self.list2.addItem(item.text())
                        Ui_MainWindow.check+=1
                        print(Ui_MainWindow.check-1, '. ', name, ' ', self.te_name.text())                    
                    if str(ctg[0])=='AR':
                        Ui_MainWindow.arnum= Ui_MainWindow.arnum +1
                        self.ar.setText(str(Ui_MainWindow.arnum))
                        self.list2.addItem(item.text())
                        Ui_MainWindow.check+=1
                        temp=str(item.text())
                        print(Ui_MainWindow.check-1, '. ', name, ' ', self.te_name.text())
                    if str(ctg[0])=='WK':
                        Ui_MainWindow.WKT+=1
                        if Ui_MainWindow.WKT==1:
                            Ui_MainWindow.wknum=Ui_MainWindow.wknum+ 1
                            self.wk.setText(str(Ui_MainWindow.wknum))
                            self.list2.addItem(item.text())
                            Ui_MainWindow.check+=1
                            print(Ui_MainWindow.check-1, '. ', name, ' ', self.te_name.text())                        
                        else:
                            self.list1.addItem(item.text())
                            msg1 = QMessageBox()
                            msg1.setWindowTitle("ERROR!!!")
                            msg1.setText("You can't enter more than one wicket keeper")
                            msg1.setIcon(QMessageBox.Critical)
                            x1=msg1.exec_()
                            used = used + cow
                            temp = temp - cow
                            self.pt_avail.setText(str(used))
                            self.pt_used.setText(str(temp))
                else:
                    msg2 = QMessageBox()
                    msg2.setWindowTitle("ERROR!!!")
                    msg2.setText("You cannot use more than 1000 points")
                    msg2.setIcon(QMessageBox.Critical)
                    x2=msg2.exec_()
                    self.list1.addItem(item.text())
                cricket.close()
            else:
                msg3 = QMessageBox()
                msg3.setWindowTitle("ERROR!!!")
                msg3.setText("You can't enter more players. PLEASE REMOVE PLAYERS FOR CHANGES")
                msg3.setIcon(QMessageBox.Critical)
                x3=msg3.exec_()
        else:
            msg4 = QMessageBox()
            msg4.setWindowTitle("ERROR!!!")
            msg4.setText("Please Enter team name first")
            msg4.setIcon(QMessageBox.Critical)
            x4=msg4.exec_()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            
    def remList(self, item):
        self.list2.takeItem(self.list2.row(item))
        name=item.text()
        cricket=sqlite3.connect('MyCricket.db')
        curcri=cricket.cursor()
        data="SELECT Value FROM Stats WHERE Player='"+name+"';"
        curcri.execute(data)
        check=curcri.fetchone()
        val= str(check[0])
        cow=int(val)
        pts=int(self.pt_avail.text()) 
        temp=int(self.pt_used.text())
        used = pts+cow
        temp = temp-cow
        if used>0:
            Ui_MainWindow.check=Ui_MainWindow.check-1
            self.pt_avail.setText(str(used))
            self.pt_used.setText(str(temp))
            data ="SELECT CTG FROM Stats WHERE Player='"+name+"';"
            curcri.execute(data)
            ctg=curcri.fetchone()
            if str(ctg[0])=='BAT':
                Ui_MainWindow.batnum=Ui_MainWindow.batnum-1
                self.bat.setText(str(Ui_MainWindow.batnum))
                self.list1.addItem(item.text())
                print("Player removed")
            if str(ctg[0])=='BWL':
                Ui_MainWindow.bownum=Ui_MainWindow.bownum-1
                self.bow.setText(str(Ui_MainWindow.bownum))
                self.list1.addItem(item.text())
                print("Player removed")                    
            if str(ctg[0])=='AR':
                Ui_MainWindow.arnum= Ui_MainWindow.arnum -1
                self.ar.setText(str(Ui_MainWindow.arnum))
                self.list1.addItem(item.text())
                temp=str(item.text())
                print("Player removed")
            if str(ctg[0])=='WK':
                Ui_MainWindow.WKT=0
                Ui_MainWindow.wknum=Ui_MainWindow.wknum- 1
                self.wk.setText(str(Ui_MainWindow.wknum))
                self.list1.addItem(item.text())
                print("Player removed")                        
            cricket.close()
    
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
