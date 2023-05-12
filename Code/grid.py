from math import floor
from random import choice, shuffle

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene

from gridSquare import GridSquare
from calcPoint import CalcPoint


class Grid(QGraphicsView):

    pipeType = "../Images/StraightPipe.png"
    pipeRotation = 0

    def __init__(self, width, height, square_size):
        super(Grid, self).__init__()

        self.width = width
        self.height = height
        self.square_size = square_size

        # Start and end points are stored here
        self.currentStart = ""
        self.currentEnd = ""

        # whitespace_x and _y remove empty space between the grid and the border
        whitespace_x = width % square_size
        whitespace_y = height % square_size
        self.setFixedSize(width - whitespace_x, height-whitespace_y)

        self.scene = QGraphicsScene()
        # Positions the center of the grid so that the sides are not visible
        self.scene.setSceneRect(1, 1, width-square_size, height-square_size)

        self.startPoints = []
        self.endPoints = []
        self.squares = []

        # Creates a GridSquare object for every position in the grid
        for x in range(floor(width/square_size)):
            for y in range(floor(height/square_size)):
                self.sq = GridSquare(x * square_size, y * square_size, square_size, square_size, self)
                self.scene.addItem(self.sq)
                self.squares.append(self.sq)

                # check if the square is meant for start or end points
                if x == 0:
                    self.startPoints.append(self.sq)
                if x == floor(self.width / square_size) - 1:
                    self.endPoints.append(self.sq)

        # randomly picks start and end points from the grid using random.choice()
        self.setPoint(choice(self.startPoints), '../Images/Start.png', "start")
        self.setPoint(choice(self.endPoints), '../Images/End.png', "end")

        self.setScene(self.scene)
        self.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

    def getHeights(self):
        return [self.currentStart.getHeightPosition(), self.currentEnd.getHeightPosition()]

    def setPipe(self, pipe, square):
        # check if the square is meant for pipes or start and end points
        if not square.isLocked():
            pipe.setPixmap(QPixmap(self.pipeType).scaled(self.square_size - 1, self.square_size))
            pipe.setOffset(square.x * self.square_size + 1, square.y * self.square_size)

            # Handle rotation
            pipe.setRotation(self.pipeRotation)
            pipe.setTransformOriginPoint(square.x * square.w + square.w / 2, square.y * square.h + square.h / 2)

            self.scene.addItem(pipe)

    def removePipe(self, pipe):
        self.scene.removeItem(pipe)

    def setType(self, image):
        self.pipeType = image

    def rotate(self, rotation):
        self.pipeRotation = rotation

    def clearGrid(self):
        for item in self.scene.items():
            # Gets the name of the class to check if it is a pipe and removes it
            if item.__class__.__name__ == 'GridPipe':
                self.scene.removeItem(item)
                item.remove()

    def setPoint(self, gridSquare, image, type):
        point = CalcPoint(image, gridSquare)
        point.setOffset(gridSquare.x * self.square_size, gridSquare.y * self.square_size)
        self.scene.addItem(point)
        if type == "start":
            self.currentStart = point
        else:
            self.currentEnd = point

    def removeCalcPoint(self, type):
        if type == "start":
            self.currentStart.removePoint()
            self.scene.removeItem(self.currentStart)
        else:
            self.currentEnd.removePoint()
            self.scene.removeItem(self.currentEnd)

    # For unit-testing purposes
    def pickNSquares(self, n):
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
