# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(984, 732)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 800, 800))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.inputWidget = InputWidget(self.scrollAreaWidgetContents)
        self.inputWidget.setGeometry(QtCore.QRect(0, 0, 800, 800))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputWidget.sizePolicy().hasHeightForWidth())
        self.inputWidget.setSizePolicy(sizePolicy)
        self.inputWidget.setText(_fromUtf8(""))
        self.inputWidget.setScaledContents(False)
        self.inputWidget.setObjectName(_fromUtf8("inputWidget"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.widget = QtGui.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(10, 40, 186, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.ppsSpin = QtGui.QSpinBox(self.widget)
        self.ppsSpin.setMinimum(10)
        self.ppsSpin.setMaximum(100)
        self.ppsSpin.setProperty("value", 50)
        self.ppsSpin.setObjectName(_fromUtf8("ppsSpin"))
        self.horizontalLayout.addWidget(self.ppsSpin)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 141, 141))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.opSlider = QtGui.QSlider(self.layoutWidget)
        self.opSlider.setMaximum(255)
        self.opSlider.setSliderPosition(255)
        self.opSlider.setOrientation(QtCore.Qt.Horizontal)
        self.opSlider.setObjectName(_fromUtf8("opSlider"))
        self.verticalLayout.addWidget(self.opSlider)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.szSlider = QtGui.QSlider(self.layoutWidget)
        self.szSlider.setMinimum(6)
        self.szSlider.setMaximum(255)
        self.szSlider.setSliderPosition(12)
        self.szSlider.setOrientation(QtCore.Qt.Horizontal)
        self.szSlider.setObjectName(_fromUtf8("szSlider"))
        self.verticalLayout.addWidget(self.szSlider)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.playBtn = QtGui.QPushButton(self.centralwidget)
        self.playBtn.setObjectName(_fromUtf8("playBtn"))
        self.gridLayout_3.addWidget(self.playBtn, 1, 2, 1, 1)
        self.vertZmSlider = QtGui.QSlider(self.centralwidget)
        self.vertZmSlider.setMinimum(100)
        self.vertZmSlider.setMaximum(1000)
        self.vertZmSlider.setSliderPosition(100)
        self.vertZmSlider.setOrientation(QtCore.Qt.Vertical)
        self.vertZmSlider.setObjectName(_fromUtf8("vertZmSlider"))
        self.gridLayout_3.addWidget(self.vertZmSlider, 0, 1, 1, 1)
        self.horzZmSlider = QtGui.QSlider(self.centralwidget)
        self.horzZmSlider.setMinimum(100)
        self.horzZmSlider.setMaximum(1000)
        self.horzZmSlider.setSliderPosition(100)
        self.horzZmSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horzZmSlider.setObjectName(_fromUtf8("horzZmSlider"))
        self.gridLayout_3.addWidget(self.horzZmSlider, 1, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setRowStretch(0, 5)
        self.gridLayout_3.setRowStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 25))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionOpacity = QtGui.QAction(MainWindow)
        self.actionOpacity.setObjectName(_fromUtf8("actionOpacity"))
        self.actionRadius = QtGui.QAction(MainWindow)
        self.actionRadius.setObjectName(_fromUtf8("actionRadius"))
        self.actionSnap_To_Pitch = QtGui.QAction(MainWindow)
        self.actionSnap_To_Pitch.setCheckable(True)
        self.actionSnap_To_Pitch.setChecked(True)
        self.actionSnap_To_Pitch.setObjectName(_fromUtf8("actionSnap_To_Pitch"))
        self.actionSnap_To_Tempo = QtGui.QAction(MainWindow)
        self.actionSnap_To_Tempo.setObjectName(_fromUtf8("actionSnap_To_Tempo"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuSettings.addAction(self.actionSnap_To_Pitch)
        self.menuSettings.addAction(self.actionSnap_To_Tempo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Other", None))
        self.label_3.setText(_translate("MainWindow", "pxl/sec", None))
        self.groupBox.setTitle(_translate("MainWindow", "Brush", None))
        self.label.setText(_translate("MainWindow", "Opacity", None))
        self.label_2.setText(_translate("MainWindow", "Size", None))
        self.playBtn.setText(_translate("MainWindow", "Play", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionOpacity.setText(_translate("MainWindow", "Opacity", None))
        self.actionRadius.setText(_translate("MainWindow", "Radius", None))
        self.actionSnap_To_Pitch.setText(_translate("MainWindow", "Snap To Pitch", None))
        self.actionSnap_To_Tempo.setText(_translate("MainWindow", "Snap To Tempo", None))

from InputWidget import InputWidget
