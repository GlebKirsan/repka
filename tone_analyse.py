import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PIL import ImageQt
# from name_author import NameAuthor
from album_art_finder import find_album_art
from lyrics_finder import get_lyrics
from tone_getter import get_tone
from tones import all_tones


class ToneAnalyse(QtWidgets.QMainWindow):
    def __init__(self, name, author):
        self.parent = self
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
        self.fillArt()        
        self.analyseTone()
        
    def fillArt(self):
        print("filling art...")
        self.imageLabel = self.findChild(QtWidgets.QLabel, 'imageLabel')
        image = find_album_art(self.author, self.name)
        qimage = ImageQt.ImageQt(image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.imageLabel.setPixmap(pixmap)

    def fillAuthor(self):
        print("filling author...")
        self.authorLabel = self.findChild(QtWidgets.QLabel, 'authorLabel')
        self.authorLabel.setText(self.author)
    
    def fillName(self):
        print("filling name...")
        self.nameLabel = self.findChild(QtWidgets.QLabel, 'nameLabel')
        self.nameLabel.setText(self.name)
    
    def analyseTone(self):
        print("analysing tone...")
        screen, self.scores = get_tone(self.author, self.name)
        
        score_values = self.scores.values()
        max_value = 0
        if (score_values):
            max_value = max(score_values)
        tone_by_score = list(self.scores.keys())[list(self.scores.values()).index(max_value)]
        tone_russian = all_tones[tone_by_score]
        common_tone_info = tone_russian if max_value > 0.3 else "отсутствует"
        self.moodLabel = self.findChild(QtWidgets.QLabel, 'moodLabel')
        self.moodLabel.setText(common_tone_info)
        
        self.scoresLabel = self.findChild(QtWidgets.QLabel, 'scoresLabel')
        scores_info = ""
        for sc_name, sc_value in self.scores.items():
            scores_info += all_tones[sc_name] + ": " + str(int(sc_value*100)) + "%\n"
        print(scores_info)
        self.scoresLabel.setText(scores_info)
        
        print("start pic")
        self.screenLabel = self.findChild(QtWidgets.QLabel, 'screenLabel')
        sc_label_width = self.screenLabel.geometry().width()
        sc_size = screen.size
        sc_size_first = sc_size[0]
        sc_size_second = sc_size[1]
        xx = sc_size_first / sc_label_width
        sc_size = (sc_label_width, int(sc_size_second / xx))
        screen = screen.resize(sc_size)
        qimage = ImageQt.ImageQt(screen)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.screenLabel.setPixmap(pixmap)
        print ("finish pic")
        
        
        

        
    
