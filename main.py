from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
import random
import sys
from Main.init import Ui_MainWindow


class Main_1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_)
        self.DRAW = False

    def paintEvent(self, event):
        if self.DRAW:
            p = QPainter()
            p.begin(self)
            self.draw(p)
            p.end()

    def draw_(self):
        self.DRAW = True
        self.repaint()

    def draw(self, p):
        for i in range(random.randint(1, 100)):
            p.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            r = random.randint(1, 500)
            p.drawEllipse(random.randint(1, 800), random.randint(1, 600), r, r)


app = QApplication(sys.argv)
main = Main_1()
main.show()
sys.exit(app.exec())
