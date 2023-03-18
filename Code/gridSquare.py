from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6 import QtGui


class GridSquare(QGraphicsRectItem):
    def __init__(self, x, y, w, h):
        super(GridSquare, self).__init__(x, y, w, h)
        # coordinates are divided by the size of the box for easier readability, (1, 1) instead of (w, h)
        self.x = x / w
        self.y = y / h
        self.__empty = True # Initialize empty square
        self.setBrush(QtGui.QColor(255, 255, 255)) # Default color

    def isEmpty(self):
        return self.__empty

    def setPipe(self):
        self.__empty = False
        self.setBrush(QtGui.QColor(20, 20, 20))

    def removePipe(self):
        self.__empty = True
        self.setBrush(QtGui.QColor(255, 255, 255))

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if self.isEmpty():
            self.setPipe()
        else:
            self.removePipe()
