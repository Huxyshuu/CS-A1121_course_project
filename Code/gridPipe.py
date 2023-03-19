from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6 import QtWidgets, QtGui


class GridPipe(QGraphicsPixmapItem):
    def __init__(self, gridSquare):
        super(GridPipe, self).__init__()
        self.gridSquare = gridSquare

    def remove(self):
        self.gridSquare.setEmpty(True)