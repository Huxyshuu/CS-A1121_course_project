from math import floor

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsPixmapItem
from PyQt6 import QtGui

from gridPipe import GridPipe
from calcPoint import CalcPoint


class GridSquare(QGraphicsRectItem):
    def __init__(self, x, y, w, h, grid):
        super(GridSquare, self).__init__(x, y, w, h)
        # coordinates are divided by the size of the box for easier readability, (1, 1) instead of (w, h)
        self.x = x / w
        self.y = y / h
        self.w = w
        self.h = h
        self.__empty = True
        self.__locked = False
        self.grid = grid
        self.pipe = GridPipe(self)
        if self.x == 0 or self.x == floor(self.grid.width/w) - 1:
            self.setBrush(QtGui.QColor(255, 230, 230))
            self.__locked = True
        else:
            self.setBrush(QtGui.QColor(255, 255, 255)) # Default color

    def isEmpty(self):
        return self.__empty

    def setEmpty(self, empty):
        self.__empty = empty

    def isLocked(self):
        return self.__locked

    def getHeightPosition(self):
        return 10 - self.y

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if self.isEmpty():
            self.grid.setPipe(self.pipe, self)
            self.setEmpty(False)
        else:
            self.grid.removePipe(self.pipe)
            self.setEmpty(True)
