# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measure.ui'
#
# Created: Wed Sep 14 17:15:01 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(666, 461)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.portLineEdit = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)
        self.portLineEdit.setMaximumSize(QtCore.QSize(140, 16777215))
        self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
        self.horizontalLayout.addWidget(self.portLineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.connectPushButton = QtGui.QPushButton(self.widget)
        self.connectPushButton.setObjectName(_fromUtf8("connectPushButton"))
        self.horizontalLayout.addWidget(self.connectPushButton)
        self.verticalLayout.addWidget(self.widget)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.testSolutionWidget = QtGui.QWidget(self.centralwidget)
        self.testSolutionWidget.setObjectName(_fromUtf8("testSolutionWidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.testSolutionWidget)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.testSolutionWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.testSolutionComboBox = QtGui.QComboBox(self.testSolutionWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testSolutionComboBox.sizePolicy().hasHeightForWidth())
        self.testSolutionComboBox.setSizePolicy(sizePolicy)
        self.testSolutionComboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.testSolutionComboBox.setObjectName(_fromUtf8("testSolutionComboBox"))
        self.horizontalLayout_5.addWidget(self.testSolutionComboBox)
        spacerItem1 = QtGui.QSpacerItem(461, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.testSolutionWidget)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.coeffLEDWidget = QtGui.QWidget(self.centralwidget)
        self.coeffLEDWidget.setObjectName(_fromUtf8("coeffLEDWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.coeffLEDWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.coeffLEDWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.coefficientLineEdit = QtGui.QLineEdit(self.coeffLEDWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coefficientLineEdit.sizePolicy().hasHeightForWidth())
        self.coefficientLineEdit.setSizePolicy(sizePolicy)
        self.coefficientLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.coefficientLineEdit.setObjectName(_fromUtf8("coefficientLineEdit"))
        self.horizontalLayout_2.addWidget(self.coefficientLineEdit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(self.coeffLEDWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.LED0RadioButton = QtGui.QRadioButton(self.coeffLEDWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LED0RadioButton.sizePolicy().hasHeightForWidth())
        self.LED0RadioButton.setSizePolicy(sizePolicy)
        self.LED0RadioButton.setObjectName(_fromUtf8("LED0RadioButton"))
        self.horizontalLayout_2.addWidget(self.LED0RadioButton)
        self.LED1RadioButton = QtGui.QRadioButton(self.coeffLEDWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LED1RadioButton.sizePolicy().hasHeightForWidth())
        self.LED1RadioButton.setSizePolicy(sizePolicy)
        self.LED1RadioButton.setObjectName(_fromUtf8("LED1RadioButton"))
        self.horizontalLayout_2.addWidget(self.LED1RadioButton)
        self.LED2RadioButton = QtGui.QRadioButton(self.coeffLEDWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LED2RadioButton.sizePolicy().hasHeightForWidth())
        self.LED2RadioButton.setSizePolicy(sizePolicy)
        self.LED2RadioButton.setObjectName(_fromUtf8("LED2RadioButton"))
        self.horizontalLayout_2.addWidget(self.LED2RadioButton)
        self.LED3RadioButton = QtGui.QRadioButton(self.coeffLEDWidget)
        self.LED3RadioButton.setObjectName(_fromUtf8("LED3RadioButton"))
        self.horizontalLayout_2.addWidget(self.LED3RadioButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.coeffLEDWidget)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tableWidget = ColorimeterTableWidget(self.frame)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.frame)
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.widget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.samplesLineEdit = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samplesLineEdit.sizePolicy().hasHeightForWidth())
        self.samplesLineEdit.setSizePolicy(sizePolicy)
        self.samplesLineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.samplesLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.samplesLineEdit.setObjectName(_fromUtf8("samplesLineEdit"))
        self.horizontalLayout_3.addWidget(self.samplesLineEdit)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.calibratePushButton = QtGui.QPushButton(self.widget_3)
        self.calibratePushButton.setObjectName(_fromUtf8("calibratePushButton"))
        self.horizontalLayout_3.addWidget(self.calibratePushButton)
        self.clearPushButton = QtGui.QPushButton(self.widget_3)
        self.clearPushButton.setObjectName(_fromUtf8("clearPushButton"))
        self.horizontalLayout_3.addWidget(self.clearPushButton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.measurePushButton = QtGui.QPushButton(self.widget_3)
        self.measurePushButton.setObjectName(_fromUtf8("measurePushButton"))
        self.horizontalLayout_3.addWidget(self.measurePushButton)
        self.plotPushButton = QtGui.QPushButton(self.widget_3)
        self.plotPushButton.setObjectName(_fromUtf8("plotPushButton"))
        self.horizontalLayout_3.addWidget(self.plotPushButton)
        self.verticalLayout.addWidget(self.widget_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuInclude = QtGui.QMenu(self.menuOptions)
        self.menuInclude.setObjectName(_fromUtf8("menuInclude"))
        self.menuSignificantDigits = QtGui.QMenu(self.menuOptions)
        self.menuSignificantDigits.setObjectName(_fromUtf8("menuSignificantDigits"))
        self.menuSample_Units = QtGui.QMenu(self.menuOptions)
        self.menuSample_Units.setObjectName(_fromUtf8("menuSample_Units"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menuMode = QtGui.QMenu(self.menubar)
        self.menuMode.setObjectName(_fromUtf8("menuMode"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionReloadTestSolutions = QtGui.QAction(MainWindow)
        self.actionReloadTestSolutions.setObjectName(_fromUtf8("actionReloadTestSolutions"))
        self.actionIncludeUserTestSolutions = QtGui.QAction(MainWindow)
        self.actionIncludeUserTestSolutions.setCheckable(True)
        self.actionIncludeUserTestSolutions.setObjectName(_fromUtf8("actionIncludeUserTestSolutions"))
        self.actionIncludeDefaultTestSolutions = QtGui.QAction(MainWindow)
        self.actionIncludeDefaultTestSolutions.setCheckable(True)
        self.actionIncludeDefaultTestSolutions.setObjectName(_fromUtf8("actionIncludeDefaultTestSolutions"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionImportTestSolution = QtGui.QAction(MainWindow)
        self.actionImportTestSolution.setObjectName(_fromUtf8("actionImportTestSolution"))
        self.actionRemoveTestSolution = QtGui.QAction(MainWindow)
        self.actionRemoveTestSolution.setObjectName(_fromUtf8("actionRemoveTestSolution"))
        self.actionEditTestSolutions = QtGui.QAction(MainWindow)
        self.actionEditTestSolutions.setObjectName(_fromUtf8("actionEditTestSolutions"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSampleUnitsUM = QtGui.QAction(MainWindow)
        self.actionSampleUnitsUM.setCheckable(True)
        self.actionSampleUnitsUM.setObjectName(_fromUtf8("actionSampleUnitsUM"))
        self.actionSampleUnitsPPM = QtGui.QAction(MainWindow)
        self.actionSampleUnitsPPM.setCheckable(True)
        self.actionSampleUnitsPPM.setObjectName(_fromUtf8("actionSampleUnitsPPM"))
        self.actionStandardRGBLED = QtGui.QAction(MainWindow)
        self.actionStandardRGBLED.setCheckable(True)
        self.actionStandardRGBLED.setObjectName(_fromUtf8("actionStandardRGBLED"))
        self.actionCustomLEDVerB = QtGui.QAction(MainWindow)
        self.actionCustomLEDVerB.setCheckable(True)
        self.actionCustomLEDVerB.setObjectName(_fromUtf8("actionCustomLEDVerB"))
        self.actionSignificantDigits1 = QtGui.QAction(MainWindow)
        self.actionSignificantDigits1.setCheckable(True)
        self.actionSignificantDigits1.setObjectName(_fromUtf8("actionSignificantDigits1"))
        self.actionSignificantDigits2 = QtGui.QAction(MainWindow)
        self.actionSignificantDigits2.setCheckable(True)
        self.actionSignificantDigits2.setObjectName(_fromUtf8("actionSignificantDigits2"))
        self.actionSignificantDigits3 = QtGui.QAction(MainWindow)
        self.actionSignificantDigits3.setCheckable(True)
        self.actionSignificantDigits3.setObjectName(_fromUtf8("actionSignificantDigits3"))
        self.actionSignificantDigits4 = QtGui.QAction(MainWindow)
        self.actionSignificantDigits4.setCheckable(True)
        self.actionSignificantDigits4.setObjectName(_fromUtf8("actionSignificantDigits4"))
        self.actionCustomLEDVerC = QtGui.QAction(MainWindow)
        self.actionCustomLEDVerC.setCheckable(True)
        self.actionCustomLEDVerC.setObjectName(_fromUtf8("actionCustomLEDVerC"))
        self.actionSampleUnitsPH = QtGui.QAction(MainWindow)
        self.actionSampleUnitsPH.setCheckable(True)
        self.actionSampleUnitsPH.setObjectName(_fromUtf8("actionSampleUnitsPH"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuInclude.addAction(self.actionIncludeUserTestSolutions)
        self.menuInclude.addAction(self.actionIncludeDefaultTestSolutions)
        self.menuSample_Units.addAction(self.actionSampleUnitsUM)
        self.menuSample_Units.addAction(self.actionSampleUnitsPPM)
        self.menuSample_Units.addAction(self.actionSampleUnitsPH)
        self.menuOptions.addAction(self.menuSample_Units.menuAction())
        self.menuOptions.addAction(self.menuSignificantDigits.menuAction())
        self.menuOptions.addAction(self.menuInclude.menuAction())
        self.menuOptions.addAction(self.actionEditTestSolutions)
        self.menu_Help.addAction(self.actionAbout)
        self.menuMode.addAction(self.actionStandardRGBLED)
        self.menuMode.addAction(self.actionCustomLEDVerB)
        self.menuMode.addAction(self.actionCustomLEDVerC)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Colorimeter Measurement", None))
        self.label.setText(_translate("MainWindow", "Serial Port", None))
        self.connectPushButton.setText(_translate("MainWindow", "Connect", None))
        self.label_4.setText(_translate("MainWindow", "Test Solution", None))
        self.label_2.setText(_translate("MainWindow", "Coefficient", None))
        self.label_3.setText(_translate("MainWindow", "LED", None))
        self.LED0RadioButton.setText(_translate("MainWindow", "LED0", None))
        self.LED1RadioButton.setText(_translate("MainWindow", "LED1", None))
        self.LED2RadioButton.setText(_translate("MainWindow", "LED2", None))
        self.LED3RadioButton.setText(_translate("MainWindow", "LED3", None))
        self.label_5.setText(_translate("MainWindow", "Samples", None))
        self.calibratePushButton.setText(_translate("MainWindow", "Calibrate", None))
        self.clearPushButton.setText(_translate("MainWindow", "Clear", None))
        self.measurePushButton.setText(_translate("MainWindow", "Measure", None))
        self.plotPushButton.setText(_translate("MainWindow", "Plot", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuOptions.setTitle(_translate("MainWindow", "&Options", None))
        self.menuInclude.setTitle(_translate("MainWindow", "Include", None))
        self.menuSignificantDigits.setTitle(_translate("MainWindow", "Significant Digits", None))
        self.menuSample_Units.setTitle(_translate("MainWindow", "Sample Units", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        self.menuMode.setTitle(_translate("MainWindow", "&Mode", None))
        self.actionReloadTestSolutions.setText(_translate("MainWindow", "Reload Test Solutions", None))
        self.actionIncludeUserTestSolutions.setText(_translate("MainWindow", "User Test Solutions", None))
        self.actionIncludeDefaultTestSolutions.setText(_translate("MainWindow", "Default Test Solutions", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionImportTestSolution.setText(_translate("MainWindow", "Import Test Solution...", None))
        self.actionRemoveTestSolution.setText(_translate("MainWindow", "Remove Test Solution...", None))
        self.actionEditTestSolutions.setText(_translate("MainWindow", "Edit User Test Solutions...", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionSampleUnitsUM.setText(_translate("MainWindow", "uM", None))
        self.actionSampleUnitsPPM.setText(_translate("MainWindow", "ppm", None))
        self.actionStandardRGBLED.setText(_translate("MainWindow", "Standard RGB LED", None))
        self.actionCustomLEDVerB.setText(_translate("MainWindow", "One custom LED (Ver. B)", None))
        self.actionSignificantDigits1.setText(_translate("MainWindow", "1", None))
        self.actionSignificantDigits2.setText(_translate("MainWindow", "2", None))
        self.actionSignificantDigits3.setText(_translate("MainWindow", "3", None))
        self.actionSignificantDigits4.setText(_translate("MainWindow", "4", None))
        self.actionCustomLEDVerC.setText(_translate("MainWindow", "Two custom LEDs (Ver. C)", None))
        self.actionSampleUnitsPH.setText(_translate("MainWindow", "pH", None))

from colorimeter.table_widget import ColorimeterTableWidget
