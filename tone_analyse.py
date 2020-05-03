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
        self.author = author
        
        self.fillAuthor()
        self.fillName()
        # self.fillYear()
        self.fillArt()
        # self.getLyrics()
        
    def fillArt(self):
        print("filling art...")
        self.imageLabel = self.findChild(QtWidgets.QLabel, 'imageLabel')
        image = find_album_art(self.author, self.name)
        qimage = ImageQt.ImageQt(image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.imageLabel.setPixmap(pixmap)
        
    def fillYear(self):
        pass
    
    def fillAuthor(self):
        print("filling author...")
        self.authorLabel = self.findChild(QtWidgets.QLabel, 'authorLabel')
        self.authorLabel.setText(self.author)
    
    def fillName(self):
        print("filling name...")
        self.nameLabel = self.findChild(QtWidgets.QLabel, 'nameLabel')
        self.nameLabel.setText(self.name)
    
    def getLyrics(self):
        pass
