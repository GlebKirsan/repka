import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class ToneAnalyse(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(ToneAnalyse, self).__init__()
        # Load the .ui file
        uic.loadUi('tone.ui', self)
        print("ready to show tone")
        self.show() # Show the GUI

    def showChildWindow(self):
        self.child_win = ChildWindow(self)
        self.child_win.show()