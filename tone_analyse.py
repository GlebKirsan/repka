import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PIL import ImageQt
from album_art_finder import find_album_art
from lyrics_finder import get_lyrics

class ToneAnalyse(QtWidgets.QMainWindow):
    def __init__(self, name, author):
        # Call the inherited classes __init__ method
        super().__init__()
        # Load the .ui file
        uic.loadUi('tone.ui', self)
        print("ready to show tone")
        self.show() # Show the GUI
        self.name = name
        print(self.name)
        self.author = author
        print(self.author)
        
        self.fillAuthor()
        self.fillName()
        # self.fillYear()
        # self.fillArt()
        # self.getLyrics()
        
    def fillArt(self):
        print("fill art")
        self.imageLabel = self.findChild(QtWidgets.QLabel, 'imageLabel')
        image = find_album_art(self.author, self.name)
        qimage = ImageQt(image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.imageLabel.detPixmap(pixmap)
        
    def fillYear(self):
        pass
    
    def fillAuthor(self):
        print("fill author")
        self.authorLabel = self.findChild(QtWidgets.QLabel, 'authorLabel')
        self.authorLabel.setText(self.author)
    
    def fillName(self):
        print("fill name")
        self.nameLabel = self.findChild(QtWidgets.QLabel, 'nameLabel')
        self.nameLabel.setText(self.name)
    
    def getLyrics(self):
        pass

    def showChildWindow(self):
        self.child_win = ChildWindow(self)
        self.child_win.show()