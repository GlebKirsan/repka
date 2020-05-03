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
        self.name_line_edit = self.findChild(QtWidgets.QLineEdit,
                                             'nameLineEdit')
        self.author_line_edit = self.findChild(QtWidgets.QLineEdit,
                                               'authorLineEdit')
        self.show() # Show the GUI
        
    def analyseButtonPressed(self):
        print("analyse button pressed")
        self.hide()
        self.open_new_dialog()
        
    def open_new_dialog(self):
        self.nd = ToneAnalyse(self.name_line_edit.text(),
                              self.author_line_edit.text())
        
        self.nd.more_btn = self.nd.findChild(QtWidgets.QPushButton, 'moreButton')
        self.nd.more_btn.clicked.connect(self.moreButtonPressed)      
        self.nd.show()
        
    def moreButtonPressed(self):
        print("refreshing...")
        self.nd.close()
        self.nameLineEdit.clear()
        self.authorLineEdit.clear()
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = NameAuthor()
    window.show()
    sys.exit(app.exec_())