from math import floor
from random import choice, shuffle

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QGraphicsView, QGraphicsLineItem, QGraphicsScene, QGraphicsRectItem, QGraphicsPixmapItem, \
    QLabel

from gridSquare import GridSquare
from gridPipe import GridPipe
from calcPoint import CalcPoint


class Grid(QGraphicsView):
    def __init__(self, width, height, square_size):
        super(Grid, self).__init__()

        self.width = width
        self.height = height

        self.pipeType = "../Images/StraightPipe.png"
        self.pipeRotation = 0
        self.square_size = square_size

        # whitespace_x and _y remove empty space between the grid and the border
        whitespace_x = width % square_size
        whitespace_y = height % square_size
        self.setFixedSize(width - whitespace_x, height-whitespace_y)

        self.scene = QGraphicsScene()
        # (1, 1) in the beginning position the center of the grid so that the sides are not visible
        self.scene.setSceneRect(1, 1, width-square_size, height-square_size)

        startPoint = []
        endPoint = []
        self.squares = []

        # Creates a GridSquare object for every position in the grid
        for x in range(floor(width/square_size)):
            for y in range(floor(height/square_size)):
                sq = GridSquare(x * square_size, y * square_size, square_size, square_size, self)
                self.scene.addItem(sq)
                self.squares.append(sq)
                if x == 0:
                    startPoint.append(sq)
                if x == floor(self.width / square_size) - 1:
                    endPoint.append(sq)


        # randomly picks start and end points from the grid using random.choice()
        self.setPoint(choice(startPoint), '../Images/Start.png')
        self.setPoint(choice(endPoint), '../Images/End.png')


        self.setScene(self.scene)
        self.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)


    def setPipe(self, pipe, square):
        if not square.isLocked():
            pipe.setPixmap(QPixmap(self.pipeType).scaled(self.square_size - 1, self.square_size))
            pipe.setOffset(square.x * self.square_size + 1, square.y * self.square_size)
            print(pipe.transformOriginPoint())

            #Handle rotation
            pipe.setRotation(self.pipeRotation)
            pipe.setTransformOriginPoint(square.x * square.w + square.w / 2, square.y * square.h + square.h / 2)

            self.scene.addItem(pipe)

    def removePipe(self, pipe):
        self.scene.removeItem(pipe)

    def setType(self, image):
        self.pipeType = image

    def rotate(self):
        if self.pipeRotation == 0:
            self.pipeRotation = 90
        elif self.pipeRotation == 90:
            self.pipeRotation = 180
        elif self.pipeRotation == 180:
            self.pipeRotation = 270
        elif self.pipeRotation == 270:
            self.pipeRotation = 0


    def setPoint(self, square, image):
        point = CalcPoint(self.square_size, image)
        point.setOffset(square.x * self.square_size, square.y * self.square_size)
        self.scene.addItem(point)

    def pickNSquares(self, n):
        #For testing
        pickList = self.squares.copy()
        shuffle(pickList)
        wanted = []
        if n <= len(self.squares):
            while len(wanted) < n:
                # Checks if the square in the pickList is one of the border squares
                # where the start or end point is supposed to go, and ignores those squares.
                if pickList[0].x != 0 and pickList[0].x != floor(self.width / self.square_size) - 1:
                    wanted.append(pickList.pop(0))
                else:
                    pickList.pop(0)


        return wanted
