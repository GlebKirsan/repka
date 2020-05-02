import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from tone_analyse import ToneAnalyse

class NameAuthor(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super().__init__()
        # Load the .ui file
        uic.loadUi('main.ui', self)
        
        self.analyse_btn = self.findChild(QtWidgets.QPushButton,
                                          'analyseButton')
        self.analyse_btn.clicked.connect(self.analyseButtonPressed)

        self.show() # Show the GUI
        
    def analyseButtonPressed(self):
        print("analyse button pressed")
        self.hide()
        self.open_new_dialog()
        #self.child_win = ChildWindow(self)
        #self.child_win.show()
        
    def open_new_dialog(self):
        self.nd = ToneAnalyse()
        self.nd.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = NameAuthor()
    window.show()
    sys.exit(app.exec_())