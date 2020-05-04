from PyQt5 import QtGui, QtWidgets, uic
from PIL import ImageQt

from album_art_finder import find_album_art

from tone_getter import get_tone
from tones import all_tones

from threading import Thread


class ToneAnalyse(QtWidgets.QMainWindow):
    def __init__(self, name, author):
        self.parent = self
        # Call the inherited classes __init__ method
        super().__init__()
        # Load the .ui file
        uic.loadUi('tone.ui', self)

        print("ready to show tone")
        self.show()  # Show the GUI
        self.name = name
        self.author = author

        self.fillAuthor()
        self.fillName()
        self.parallelize()

    def parallelize(self):
        thread1 = Thread(target=self.fillArt)
        thread2 = Thread(target=self.analyseTone)
        thread1.start()
        thread2.start()

    def fillArt(self):
        print("filling art...")
        imageLabel = self.findChild(QtWidgets.QLabel, 'imageLabel')
        image = find_album_art(self.author, self.name)
        qimage = ImageQt.ImageQt(image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        imageLabel.setPixmap(pixmap)

    def fillAuthor(self):
        print("filling author...")
        authorLabel = self.findChild(QtWidgets.QLabel, 'authorLabel')
        authorLabel.setText(self.author)

    def fillName(self):
        print("filling name...")
        nameLabel = self.findChild(QtWidgets.QLabel, 'nameLabel')
        nameLabel.setText(self.name)

    def analyseTone(self):
        print("analysing tone...")
        screen, scores = get_tone(self.author, self.name)

        score_values = scores.values()
        if score_values:
            max_value = max(score_values)
            tone_by_score = list(scores.keys())[list(scores.values()).index(max_value)]
            tone_russian = all_tones[tone_by_score]
            common_tone_info = tone_russian if max_value > 0.3 else "отсутствует"
        else:
            common_tone_info = "отсутствует"
        moodLabel = self.findChild(QtWidgets.QLabel, 'moodLabel')
        moodLabel.setText(common_tone_info)

        scoresLabel = self.findChild(QtWidgets.QLabel, 'scoresLabel')
        scores_info = [f'{all_tones[sc_name]}: {int(sc_value * 100)}%'
                       for sc_name, sc_value in scores.items()]
        joined = '\n'.join(scores_info)
        scoresLabel.setText(joined)

        print("start pic")
        screenLabel = self.findChild(QtWidgets.QLabel, 'screenLabel')
        score_height = screen.size[1]
        label_width = screenLabel.geometry().width()
        screen.thumbnail((label_width, score_height))
        qimage = ImageQt.ImageQt(screen)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        screenLabel.setPixmap(pixmap)
        print("finish pic")
