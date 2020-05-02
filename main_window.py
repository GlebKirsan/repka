# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from tone_window import Ui_ToneWindow


class Ui_MainWindow(QtWidgets.QWidget):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 392, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.mainVerticalLayout.addWidget(self.label)
        self.nameHorizontalLayout = QtWidgets.QHBoxLayout()
        self.nameHorizontalLayout.setObjectName("nameHorizontalLayout")
        self.nameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nameLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameHorizontalLayout.addWidget(self.nameLineEdit)
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.nameHorizontalLayout.addWidget(self.nameLabel)
        self.mainVerticalLayout.addLayout(self.nameHorizontalLayout)
        self.authorHorizontalLayout = QtWidgets.QHBoxLayout()
        self.authorHorizontalLayout.setObjectName("authorHorizontalLayout")
        self.authorLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.authorLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.authorLineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.authorHorizontalLayout.addWidget(self.authorLineEdit)
        self.authorLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.authorLabel.setObjectName("authorLabel")
        self.authorHorizontalLayout.addWidget(self.authorLabel)
        self.mainVerticalLayout.addLayout(self.authorHorizontalLayout)
        self.buttonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.buttonHorizontalLayout.setObjectName("buttonHorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonHorizontalLayout.addItem(spacerItem)
        
        self.analyseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.analyseButton.setMinimumSize(QtCore.QSize(100, 0))
        self.analyseButton.setObjectName("analyseButton")
        self.analyseButton.pressed.connect(self.create_new_window)
        
        self.buttonHorizontalLayout.addWidget(self.analyseButton)
        self.mainVerticalLayout.addLayout(self.buttonHorizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
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
        self.label.setText(_translate("MainWindow", "Для анализа эмоциональной окраски музыкального произведения\n"
" введите название и исполнителя и нажмите \"Анализировать\""))
        self.nameLabel.setText(_translate("MainWindow", "Название"))
        self.authorLabel.setText(_translate("MainWindow", "Исполнитель"))
        self.analyseButton.setText(_translate("MainWindow", "Анализировать"))
        
    def create_new_window(self):
        print("open tone window")
        self.child_win = Ui_ToneWindow(self)
        self.child_win.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
