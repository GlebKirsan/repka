# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tone.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ToneWindow(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        print("init tone_window")
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("Child Window!")
        ToneWindow = QtWidgets.QMainWindow()
        self.setupUi(ToneWindow)
        ToneWindow.show()

    def setupUi(self, ToneWindow):
        ToneWindow.setObjectName("ToneWindow")
        ToneWindow.resize(430, 300)
        self.centralwidget = QtWidgets.QWidget(ToneWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 392, 235))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        self.infoHorizontalLayout = QtWidgets.QHBoxLayout()
        self.infoHorizontalLayout.setObjectName("infoHorizontalLayout")
        self.imageLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.imageLabel.setMinimumSize(QtCore.QSize(0, 150))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.infoHorizontalLayout.addWidget(self.imageLabel)
        self.commonInfoVerticalLayout = QtWidgets.QVBoxLayout()
        self.commonInfoVerticalLayout.setObjectName("commonInfoVerticalLayout")
        self.yearHorizontalLayout = QtWidgets.QHBoxLayout()
        self.yearHorizontalLayout.setObjectName("yearHorizontalLayout")
        self.textYearLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.textYearLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.textYearLabel.setObjectName("textYearLabel")
        self.yearHorizontalLayout.addWidget(self.textYearLabel)
        self.yearLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.yearLabel.setText("")
        self.yearLabel.setObjectName("yearLabel")
        self.yearHorizontalLayout.addWidget(self.yearLabel)
        self.commonInfoVerticalLayout.addLayout(self.yearHorizontalLayout)
        self.authorHorizontalLayout = QtWidgets.QHBoxLayout()
        self.authorHorizontalLayout.setObjectName("authorHorizontalLayout")
        self.textAuthorLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.textAuthorLabel.setMaximumSize(QtCore.QSize(75, 16777215))
        self.textAuthorLabel.setObjectName("textAuthorLabel")
        self.authorHorizontalLayout.addWidget(self.textAuthorLabel)
        self.authorLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.authorLabel.setText("")
        self.authorLabel.setObjectName("authorLabel")
        self.authorHorizontalLayout.addWidget(self.authorLabel)
        self.commonInfoVerticalLayout.addLayout(self.authorHorizontalLayout)
        self.nameHorizontalLayout = QtWidgets.QHBoxLayout()
        self.nameHorizontalLayout.setObjectName("nameHorizontalLayout")
        self.textNameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.textNameLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.textNameLabel.setObjectName("textNameLabel")
        self.nameHorizontalLayout.addWidget(self.textNameLabel)
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setText("")
        self.nameLabel.setObjectName("nameLabel")
        self.nameHorizontalLayout.addWidget(self.nameLabel)
        self.commonInfoVerticalLayout.addLayout(self.nameHorizontalLayout)
        self.infoHorizontalLayout.addLayout(self.commonInfoVerticalLayout)
        self.mainVerticalLayout.addLayout(self.infoHorizontalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textMoodLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.textMoodLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.textMoodLabel.setObjectName("textMoodLabel")
        self.horizontalLayout.addWidget(self.textMoodLabel)
        self.moodLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.moodLabel.setText("")
        self.moodLabel.setObjectName("moodLabel")
        self.horizontalLayout.addWidget(self.moodLabel)
        self.mainVerticalLayout.addLayout(self.horizontalLayout)
        self.buttonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.buttonHorizontalLayout.setObjectName("buttonHorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonHorizontalLayout.addItem(spacerItem)
        self.moreButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.moreButton.setMinimumSize(QtCore.QSize(100, 0))
        self.moreButton.setObjectName("moreButton")
        self.buttonHorizontalLayout.addWidget(self.moreButton)
        self.mainVerticalLayout.addLayout(self.buttonHorizontalLayout)
        ToneWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ToneWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        ToneWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ToneWindow)
        self.statusbar.setObjectName("statusbar")
        ToneWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ToneWindow)
        QtCore.QMetaObject.connectSlotsByName(ToneWindow)

    def retranslateUi(self, ToneWindow):
        _translate = QtCore.QCoreApplication.translate
        ToneWindow.setWindowTitle(_translate("ToneWindow", "ToneWindow"))
        self.textYearLabel.setText(_translate("ToneWindow", "Год:"))
        self.textAuthorLabel.setText(_translate("ToneWindow", "Исполнитель:"))
        self.textNameLabel.setText(_translate("ToneWindow", "Название:"))
        self.textMoodLabel.setText(_translate("ToneWindow", "Общее настроение:"))
        self.moreButton.setText(_translate("ToneWindow", "Подробнее"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    ToneWindow = QtWidgets.QMainWindow()
#    ui = Ui_ToneWindow()
#    ui.setupUi(ToneWindow)
#    ToneWindow.show()
#    sys.exit(app.exec_())
