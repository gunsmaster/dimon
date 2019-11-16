import sys
from random import choice

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from untitled import Ui_MainWindow

a = []
for i in range(50):
    a.append(i)
b = []
for i in range(256):
    b.append(i)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pusButton.clicked.connect(self.ad)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.recta(qp)
        qp.end()

    def recta(self, qp):
        qp.setBrush(QColor(choice(b), choice(b), choice(b)))
        qp.drawEllipse(10, 50, choice(a), choice(a))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
