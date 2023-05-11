from math import floor

from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6 import QtGui

#custom classes
from gridPipe import GridPipe

class GridSquare(QGraphicsRectItem):
    def __init__(self, x, y, w, h, grid):
        super(GridSquare, self).__init__(x, y, w, h)

        # Coordinates are divided by the size of the box for easier readability, (1, 1) instead of (w, h)
        self.x = x / w
        self.y = y / h
        self.w = w
        self.h = h
        self.__empty = True
        self.__locked = False
        self.grid = grid
        self.pipe = GridPipe(self)

        # If the square is meant for start or end points, it will be colored light red and locked
        if self.x == 0 or self.x == floor(self.grid.width / w) - 1:
            self.setBrush(QtGui.QColor(255, 230, 230))  # Light red color
            self.__locked = True
        else:
            self.setBrush(QtGui.QColor(255, 255, 255))  # Default color

    def isEmpty(self):
        return self.__empty

    def setEmpty(self, empty):
        self.__empty = empty

    def isLocked(self):
        return self.__locked

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if self.isEmpty():
            self.grid.setPipe(self.pipe, self)  # Set the pipe for this square in the grid
            self.setEmpty(False)
        else:
            self.grid.removePipe(self.pipe)  # Remove the pipe from the grid
            self.setEmpty(True)

        if self.x == 0:
            self.grid.removeCalcPoint("start")
            self.grid.setPoint(self, '../Images/Start.png', "start")

        if self.x == floor(self.grid.width / self.w) - 1:
            self.grid.removeCalcPoint("end")
            self.grid.setPoint(self, '../Images/End.png', "end")

