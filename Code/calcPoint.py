from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap

class CalcPoint(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, square_size, image):
        super(CalcPoint, self).__init__()
        self.setPixmap(QPixmap(image).scaled(square_size - 1, square_size))