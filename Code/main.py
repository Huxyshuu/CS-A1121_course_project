import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, \
    QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QGraphicsPixmapItem
from PyQt6.QtGui import QPalette, QColor, QPixmap

#custom Classes
from grid import Grid
from pipes import Pipes
from pipeAdder import PipeAdder

class MainWindow(QMainWindow): # Creating a subclass of QMainWindow for better control over the window customization

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Pipeflow - Hugo")

        self.setFixedSize(QSize(1280, 850)) # Sets a fixed window size



        self.button = QPushButton("Press Me!")
        self.button.setFixedSize(QSize(200, 200))
        self.button.clicked.connect(self.printClick) # PyCharm showing error on .connect  # it works regardless
                                                     # widget.clicked.connect(func) # Add functionality

        self.clearButton = QPushButton("Clear Grid!")
        self.clearButton.setFixedSize(QSize(100, 60))
        self.clearButton.clicked.connect(self.clearGrid)
        self.clearButton.setStyleSheet("background-color: white;")

        # Layout inits
        baseLayout = QHBoxLayout()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()
        topLayout = QHBoxLayout()

        def onClicked(self):
            print("Sup")

        #Adding pipes to topLayout
        pipeList = ['../Images/StraightPipe.png', '../Images/CornerPipe.png', '../Images/TPipe.png', '../Images/SectionPipe.png']
        pipes = PipeAdder(pipeList, 50, topLayout)  # list of pipes, pipe scale, layout
        pipeButtons = pipes.returnPipeButtons()
        print(pipeButtons)

        baseLayout.addLayout(leftLayout)
        baseLayout.addLayout(rightLayout)

        # Left side buttons
        label = QLabel("Stuff")
        label.setFixedSize(100, 100)
        leftLayout.addWidget(label)
        leftLayout.addWidget(self.button)

        # Top right layout
        # Pipes
        pipeBox = QWidget()
        rightLayout.addWidget(pipeBox)
        pipeBox.setLayout(topLayout)
        pipeBox.setStyleSheet("border: 1px solid black; background-color: lightgray;")

        topLayout.addWidget(self.clearButton)

        # Bottom right layout
        # Grid (750, 750, 50) is a good size for a window of size (1280, 850)
        self.view = Grid(750, 750, 50) # Width, Height, Square size
        self.view.show()
        rightLayout.addWidget(self.view)

        widget = QWidget()
        widget.setLayout(baseLayout)
        self.setCentralWidget(widget)

    def printClick(self):
        print("Hey")

    def clearGrid(self):
        print("Grid cleared")



app = QApplication(sys.argv)

window = MainWindow()
window.show() # Makes the window visible

app.exec()