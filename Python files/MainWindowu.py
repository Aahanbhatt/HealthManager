# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Body_fat import Ui_Bodyfat
from bmi import Ui_Bmi
from Weight import Ui_Weight
from Login_widget import Login

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):


    def __init__(self,parent=None):
        super(Ui_MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.actionBody_Fat_Percentage.triggered.connect(self.handleBodyfat)
        self.actionBody_Mass_Index.triggered.connect(self.handleBmi)
        self.actionWeight.triggered.connect(self.handleWeight)
        self.actionUserLogin.triggered.connect(self.handleLogin)     

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(797, 608)
        MainWindow.setMaximumSize(QtCore.QSize(797, 608))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/window_icon/health-app-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(2.0)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(:/back/ARK4.png);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMedical_ID = QtGui.QMenu(self.menubar)
        self.menuMedical_ID.setObjectName(_fromUtf8("menuMedical_ID"))
        self.menuHealth_Data = QtGui.QMenu(self.menubar)
        self.menuHealth_Data.setObjectName(_fromUtf8("menuHealth_Data"))
        self.menuSleep = QtGui.QMenu(self.menuHealth_Data)
        self.menuSleep.setObjectName(_fromUtf8("menuSleep"))
        self.menuVitals = QtGui.QMenu(self.menuHealth_Data)
        self.menuVitals.setObjectName(_fromUtf8("menuVitals"))
        self.menuBody_Measurements = QtGui.QMenu(self.menuHealth_Data)
        self.menuBody_Measurements.setObjectName(_fromUtf8("menuBody_Measurements"))
        self.menuFitness = QtGui.QMenu(self.menuHealth_Data)
        self.menuFitness.setObjectName(_fromUtf8("menuFitness"))
        self.menuDietary_Intake = QtGui.QMenu(self.menuHealth_Data)
        self.menuDietary_Intake.setObjectName(_fromUtf8("menuDietary_Intake"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionBody_Measurements = QtGui.QAction(MainWindow)
        self.actionBody_Measurements.setObjectName(_fromUtf8("actionBody_Measurements"))
        self.actionNew_user = QtGui.QAction(MainWindow)
        self.actionNew_user.setObjectName(_fromUtf8("actionNew_user"))
        self.actionSleep_Analysis = QtGui.QAction(MainWindow)
        self.actionSleep_Analysis.setObjectName(_fromUtf8("actionSleep_Analysis"))
        self.actionBlood_Pressure = QtGui.QAction(MainWindow)
        self.actionBlood_Pressure.setObjectName(_fromUtf8("actionBlood_Pressure"))
        self.actionBody_Temperature = QtGui.QAction(MainWindow)
        self.actionBody_Temperature.setObjectName(_fromUtf8("actionBody_Temperature"))
        self.actionHeart_Rate = QtGui.QAction(MainWindow)
        self.actionHeart_Rate.setObjectName(_fromUtf8("actionHeart_Rate"))
        self.actionRespiratory_Rate = QtGui.QAction(MainWindow)
        self.actionRespiratory_Rate.setObjectName(_fromUtf8("actionRespiratory_Rate"))
        self.actionBody_Fat_Percentage = QtGui.QAction(MainWindow)
        self.actionBody_Fat_Percentage.setObjectName(_fromUtf8("actionBody_Fat_Percentage"))
        self.actionBody_Mass_Index = QtGui.QAction(MainWindow)
        self.actionBody_Mass_Index.setObjectName(_fromUtf8("actionBody_Mass_Index"))
        self.actionHeight = QtGui.QAction(MainWindow)
        self.actionHeight.setObjectName(_fromUtf8("actionHeight"))
        self.actionLean_Body_Mass = QtGui.QAction(MainWindow)
        self.actionLean_Body_Mass.setObjectName(_fromUtf8("actionLean_Body_Mass"))
        self.actionWeight = QtGui.QAction(MainWindow)
        self.actionWeight.setObjectName(_fromUtf8("actionWeight"))
        self.actionActive_Energy = QtGui.QAction(MainWindow)
        self.actionActive_Energy.setObjectName(_fromUtf8("actionActive_Energy"))
        self.actionCycling_Distance = QtGui.QAction(MainWindow)
        self.actionCycling_Distance.setObjectName(_fromUtf8("actionCycling_Distance"))
        self.actionFlights_Climbed = QtGui.QAction(MainWindow)
        self.actionFlights_Climbed.setObjectName(_fromUtf8("actionFlights_Climbed"))
        self.actionResting_Energy = QtGui.QAction(MainWindow)
        self.actionResting_Energy.setObjectName(_fromUtf8("actionResting_Energy"))
        self.actionStand_Hours = QtGui.QAction(MainWindow)
        self.actionStand_Hours.setObjectName(_fromUtf8("actionStand_Hours"))
        self.actionSteps = QtGui.QAction(MainWindow)
        self.actionSteps.setObjectName(_fromUtf8("actionSteps"))
        self.actionWalking_Running_Distance = QtGui.QAction(MainWindow)
        self.actionWalking_Running_Distance.setObjectName(_fromUtf8("actionWalking_Running_Distance"))
        self.actionWorkouts = QtGui.QAction(MainWindow)
        self.actionWorkouts.setObjectName(_fromUtf8("actionWorkouts"))
        self.actionCalcium = QtGui.QAction(MainWindow)
        self.actionCalcium.setObjectName(_fromUtf8("actionCalcium"))
        self.actionCarbohydrates = QtGui.QAction(MainWindow)
        self.actionCarbohydrates.setObjectName(_fromUtf8("actionCarbohydrates"))
        self.actionCalcium_2 = QtGui.QAction(MainWindow)
        self.actionCalcium_2.setObjectName(_fromUtf8("actionCalcium_2"))
        self.actionDietary_Calories = QtGui.QAction(MainWindow)
        self.actionDietary_Calories.setObjectName(_fromUtf8("actionDietary_Calories"))
        self.actionDietary_Cholestrol = QtGui.QAction(MainWindow)
        self.actionDietary_Cholestrol.setObjectName(_fromUtf8("actionDietary_Cholestrol"))
        self.actionDietary_Sugar = QtGui.QAction(MainWindow)
        self.actionDietary_Sugar.setObjectName(_fromUtf8("actionDietary_Sugar"))
        self.actionFibre = QtGui.QAction(MainWindow)
        self.actionFibre.setObjectName(_fromUtf8("actionFibre"))
        self.actionProtein = QtGui.QAction(MainWindow)
        self.actionProtein.setObjectName(_fromUtf8("actionProtein"))
        self.actionVitamins = QtGui.QAction(MainWindow)
        self.actionVitamins.setObjectName(_fromUtf8("actionVitamins"))
        self.actionWater = QtGui.QAction(MainWindow)
        self.actionWater.setObjectName(_fromUtf8("actionWater"))
        self.actionUserLogin = QtGui.QAction(MainWindow)
        self.actionUserLogin.setObjectName(_fromUtf8("actionUserLogin"))
        self.menuMedical_ID.addAction(self.actionUserLogin)
        self.menuSleep.addAction(self.actionSleep_Analysis)
        self.menuVitals.addAction(self.actionBlood_Pressure)
        self.menuVitals.addAction(self.actionBody_Temperature)
        self.menuVitals.addAction(self.actionHeart_Rate)
        self.menuVitals.addAction(self.actionRespiratory_Rate)
        self.menuBody_Measurements.addAction(self.actionBody_Fat_Percentage)
        self.menuBody_Measurements.addAction(self.actionBody_Mass_Index)
        self.menuBody_Measurements.addAction(self.actionHeight)
        self.menuBody_Measurements.addAction(self.actionLean_Body_Mass)
        self.menuBody_Measurements.addAction(self.actionWeight)
        self.menuFitness.addAction(self.actionActive_Energy)
        self.menuFitness.addAction(self.actionCycling_Distance)
        self.menuFitness.addAction(self.actionFlights_Climbed)
        self.menuFitness.addAction(self.actionResting_Energy)
        self.menuFitness.addAction(self.actionStand_Hours)
        self.menuFitness.addAction(self.actionSteps)
        self.menuFitness.addAction(self.actionWalking_Running_Distance)
        self.menuFitness.addAction(self.actionWorkouts)
        self.menuDietary_Intake.addAction(self.actionCarbohydrates)
        self.menuDietary_Intake.addAction(self.actionCalcium_2)
        self.menuDietary_Intake.addAction(self.actionDietary_Calories)
        self.menuDietary_Intake.addAction(self.actionDietary_Cholestrol)
        self.menuDietary_Intake.addAction(self.actionDietary_Sugar)
        self.menuDietary_Intake.addAction(self.actionFibre)
        self.menuDietary_Intake.addAction(self.actionProtein)
        self.menuDietary_Intake.addAction(self.actionVitamins)
        self.menuDietary_Intake.addAction(self.actionWater)
        self.menuHealth_Data.addAction(self.menuBody_Measurements.menuAction())
        self.menuHealth_Data.addAction(self.menuFitness.menuAction())
        self.menuHealth_Data.addAction(self.menuSleep.menuAction())
        self.menuHealth_Data.addAction(self.menuVitals.menuAction())
        self.menuHealth_Data.addAction(self.menuDietary_Intake.menuAction())
        self.menubar.addAction(self.menuMedical_ID.menuAction())
        self.menubar.addAction(self.menuHealth_Data.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Health Kit", None))
        self.menuMedical_ID.setTitle(_translate("MainWindow", "Medical ID", None))
        self.menuHealth_Data.setTitle(_translate("MainWindow", "Health Data", None))
        self.menuSleep.setTitle(_translate("MainWindow", "Sleep", None))
        self.menuVitals.setTitle(_translate("MainWindow", "Vitals", None))
        self.menuBody_Measurements.setTitle(_translate("MainWindow", "Body Measurements", None))
        self.menuFitness.setTitle(_translate("MainWindow", "Fitness", None))
        self.menuDietary_Intake.setTitle(_translate("MainWindow", "Dietary Intake", None))
        self.actionBody_Measurements.setText(_translate("MainWindow", "Body Measurements", None))
        self.actionNew_user.setText(_translate("MainWindow", "New user", None))
        self.actionSleep_Analysis.setText(_translate("MainWindow", "Sleep Analysis", None))
        self.actionBlood_Pressure.setText(_translate("MainWindow", "Blood Pressure", None))
        self.actionBody_Temperature.setText(_translate("MainWindow", "Body Temperature", None))
        self.actionHeart_Rate.setText(_translate("MainWindow", "Heart Rate", None))
        self.actionRespiratory_Rate.setText(_translate("MainWindow", "Respiratory Rate", None))
        self.actionBody_Fat_Percentage.setText(_translate("MainWindow", "Body Fat Percentage", None))
        self.actionBody_Mass_Index.setText(_translate("MainWindow", "Body Mass Index", None))
        self.actionHeight.setText(_translate("MainWindow", "Height", None))
        self.actionLean_Body_Mass.setText(_translate("MainWindow", "Lean Body Mass", None))
        self.actionWeight.setText(_translate("MainWindow", "Weight", None))
        self.actionActive_Energy.setText(_translate("MainWindow", "Active Energy", None))
        self.actionCycling_Distance.setText(_translate("MainWindow", "Cycling Distance", None))
        self.actionFlights_Climbed.setText(_translate("MainWindow", "Flights Climbed", None))
        self.actionResting_Energy.setText(_translate("MainWindow", "Resting Energy", None))
        self.actionStand_Hours.setText(_translate("MainWindow", "Stand Hours", None))
        self.actionSteps.setText(_translate("MainWindow", "Steps", None))
        self.actionWalking_Running_Distance.setText(_translate("MainWindow", "Walking+Running Distance", None))
        self.actionWorkouts.setText(_translate("MainWindow", "Workouts", None))
        self.actionCalcium.setText(_translate("MainWindow", "Calcium", None))
        self.actionCarbohydrates.setText(_translate("MainWindow", "Carbohydrates", None))
        self.actionCalcium_2.setText(_translate("MainWindow", "Calcium", None))
        self.actionDietary_Calories.setText(_translate("MainWindow", "Dietary Calories", None))
        self.actionDietary_Cholestrol.setText(_translate("MainWindow", "Dietary Cholestrol", None))
        self.actionDietary_Sugar.setText(_translate("MainWindow", "Dietary Sugar", None))
        self.actionFibre.setText(_translate("MainWindow", "Fibre", None))
        self.actionProtein.setText(_translate("MainWindow", "Protein", None))
        self.actionVitamins.setText(_translate("MainWindow", "Vitamins", None))
        self.actionWater.setText(_translate("MainWindow", "Water", None))
        self.actionUserLogin.setText(_translate("MainWindow", "UserLogin", None))

    def handleBodyfat(self):
        ob=Ui_Bodyfat(self)
        ob.show()

    def handleBmi(self):
        obj=Ui_Bmi(self)
        obj.show()

    def handleWeight(self):
        o=Ui_Weight(self)
        o.show()

    def handleLogin(self):
        o=Login(self)
        o.show()

import test_rc
import window_icon_rc
import sys

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    obj=Ui_MainWindow()
    obj.show()
    sys.exit(app.exec_())
