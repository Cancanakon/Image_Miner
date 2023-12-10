# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Venv_projects/detection/package/ui/ui_image_miner.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_loadingBar = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_loadingBar.setGeometry(QtCore.QRect(350, 530, 691, 41))
        self.pb_loadingBar.setStyleSheet("QProgressBar\n"
"{\n"
"border: solid grey;\n"
"border-radius: 15px;\n"
"color: black;\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: #05B8CC;\n"
"border-radius :15px;\n"
"}     ")
        self.pb_loadingBar.setProperty("value", 0)
        self.pb_loadingBar.setAlignment(QtCore.Qt.AlignCenter)
        self.pb_loadingBar.setInvertedAppearance(False)
        self.pb_loadingBar.setObjectName("pb_loadingBar")
        self.btn_getData = QtWidgets.QPushButton(self.centralwidget)
        self.btn_getData.setGeometry(QtCore.QRect(570, 640, 220, 60))
        self.btn_getData.setStyleSheet("")
        self.btn_getData.setObjectName("btn_getData")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(400, 220, 511, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edt_keywords = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edt_keywords.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_keywords.sizePolicy().hasHeightForWidth())
        self.edt_keywords.setSizePolicy(sizePolicy)
        self.edt_keywords.setObjectName("edt_keywords")
        self.gridLayout.addWidget(self.edt_keywords, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.sb_imageNumber = QtWidgets.QSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_imageNumber.sizePolicy().hasHeightForWidth())
        self.sb_imageNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_imageNumber.setFont(font)
        self.sb_imageNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_imageNumber.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sb_imageNumber.setMaximum(20000)
        self.sb_imageNumber.setObjectName("sb_imageNumber")
        self.gridLayout.addWidget(self.sb_imageNumber, 1, 2, 1, 1)
        self.lbl_searchKeyword = QtWidgets.QLabel(self.centralwidget)
        self.lbl_searchKeyword.setGeometry(QtCore.QRect(260, 380, 801, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_searchKeyword.setFont(font)
        self.lbl_searchKeyword.setStyleSheet("color:orange;")
        self.lbl_searchKeyword.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_searchKeyword.setObjectName("lbl_searchKeyword")
        self.lbl_situation_live = QtWidgets.QLabel(self.centralwidget)
        self.lbl_situation_live.setGeometry(QtCore.QRect(350, 580, 641, 21))
        self.lbl_situation_live.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_situation_live.setObjectName("lbl_situation_live")
        self.lbl_situation = QtWidgets.QLabel(self.centralwidget)
        self.lbl_situation.setGeometry(QtCore.QRect(350, 470, 641, 21))
        self.lbl_situation.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_situation.setObjectName("lbl_situation")
        self.btn_question = QtWidgets.QPushButton(self.centralwidget)
        self.btn_question.setGeometry(QtCore.QRect(10, 10, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.btn_question.setFont(font)
        self.btn_question.setStyleSheet("border-color:black;\n"
"border-radius:20px;\n"
"background-color: green;\n"
"color:white;\n"
"")
        self.btn_question.setObjectName("btn_question")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Miner"))
        self.pb_loadingBar.setFormat(_translate("MainWindow", "%p %"))
        self.btn_getData.setText(_translate("MainWindow", "GET DATA"))
        self.label.setText(_translate("MainWindow", "Image Keyword :"))
        self.edt_keywords.setPlaceholderText(_translate("MainWindow", "2 word recommended"))
        self.label_2.setText(_translate("MainWindow", "Image Number :"))
        self.lbl_searchKeyword.setText(_translate("MainWindow", "CURRENT WORDS"))
        self.lbl_situation_live.setText(_translate("MainWindow", "None"))
        self.lbl_situation.setText(_translate("MainWindow", "Waiting for mission..."))
        self.btn_question.setText(_translate("MainWindow", "?"))

