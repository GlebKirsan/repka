import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PIL import ImageQt
# from name_author import NameAuthor
from album_art_finder import find_album_art
from lyrics_finder import get_lyrics


class ToneAnalyse(QtWidgets.QMainWindow):
    def __init__(self, name, author):
        self.parent = self
        # Call the inherited classes __init__ method
        super().__init__()
        # Load the .ui file
        uic.loadUi('tone.ui', self)
        
        self.need_be_open = True
        
        self.more_btn = self.findChild(QtWidgets.QPushButton, 'moreButton')
        self.more_btn.clicked.connect(self.moreButtonPressed)      
        
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
    
    def moreButtonPressed(self):
        print("more button pressed")
        self.need_be_open = False
        # self.hide()
        # self.open_new_dialog()
        
    def open_new_dialog(self):
        # self.webview.go_back()
        # self.parent.show()
        pass
