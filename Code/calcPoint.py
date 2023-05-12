from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap

class CalcPoint(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, image, gridSquare):
        super(CalcPoint, self).__init__()
        # Initialize the start or end point with the correct image (A or B)

        self.gridSquare = gridSquare
        self.gridSquare.setEmpty(False)
        self.setPixmap(QPixmap(image).scaled(self.gridSquare.w - 1, self.gridSquare.w))

    def removePoint(self):
        self.gridSquare.setEmpty(True)

    def getHeightPosition(self):
        GRID_HEIGHT = 10
        return GRID_HEIGHT - self.gridSquare.y

    def getSquare(self):
        return self.gridSquare

