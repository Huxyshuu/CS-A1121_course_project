from math import floor

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsView, QGraphicsLineItem, QGraphicsScene, QGraphicsRectItem

from gridSquare import GridSquare


class Grid(QGraphicsView):
    def __init__(self, width, height, square_size):
        super(Grid, self).__init__()
        # whitespace_x and _y remove empty space between the grid and the border
        whitespace_x = width % square_size
        whitespace_y = height % square_size
        self.setFixedSize(width - whitespace_x, height-whitespace_y)

        self.scene = QGraphicsScene()
        # (1, 1) in the beginning position the center of the grid so that the sides are not visible
        self.scene.setSceneRect(1, 1, width-square_size, height-square_size)

        # Line for testing purposes
        self.line = QGraphicsLineItem()
        self.line.setLine(0, 0, 100, 100)

        self.scene.addItem(self.line)

        # Creates a GridSquare object for every position in the grid
        for x in range(floor(width/square_size)):
            for y in range(floor(height/square_size)):
                sq = GridSquare(x * square_size, y * square_size, square_size, square_size, self.scene)
                self.scene.addItem(sq)

        self.setScene(self.scene)
        self.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)