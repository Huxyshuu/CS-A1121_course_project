import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, \
    QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QGraphicsPixmapItem, QLineEdit
from PyQt6.QtGui import QPalette, QColor, QPixmap, QIntValidator

#custom Classes
from grid import Grid
from gridPipe import GridPipe
from pipeButtonCreator import PipeButtonCreator


class MainWindow(QMainWindow): # Creating a subclass of QMainWindow for better control over the window customization

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Pipeflow - Hugo")

        self.setFixedSize(QSize(1280, 850)) # Sets a fixed window size


        self.clearButton = QPushButton("Clear Grid!")
        self.clearButton.setFixedSize(QSize(100, 60))
        self.clearButton.clicked.connect(self.clearGrid)
        self.clearButton.setStyleSheet("QPushButton {"
                                            "background-color: white;"
                                            "font-size: 15px;"
                                       "}"
                                       
                                       "QPushButton:hover {"
                                            "background-color: rgb(255, 220, 220);"
                                            "border: 2px solid rgb(235, 100, 100);"
                                       "}")

        # Layout inits
        baseLayout = QHBoxLayout()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()
        topLayout = QHBoxLayout()









        pipeList = ['../Images/StraightPipe.png',
                    '../Images/CornerPipe.png',
                    '../Images/TPipe.png',
                    '../Images/SectionPipe.png']

        # Adding pipes to topLayout
        self.pipeButtons = PipeButtonCreator(pipeList, 50, topLayout).returnPipeButtons()  # list of pipes, pipe scale, layout

        baseLayout.addLayout(leftLayout)
        baseLayout.addLayout(rightLayout)

        # Left side buttons
        # Start input
        startLayout = QVBoxLayout()
        startLayout.setContentsMargins(20, 0, 20, 0)
        startInputLayout = QHBoxLayout()
        startInputLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        startLayout.addLayout(startInputLayout)
        leftLayout.addLayout(startLayout)

        startLabel = QLabel("Set pressure for starting point (kPa):")
        startLabel.setStyleSheet("font-size: 15px;")
        startInput = QLineEdit()
        startInput.setValidator(QIntValidator(0, 100000))
        startInput.textChanged.connect(self.changeStartData)
        startInput.setStyleSheet("font-size: 15px;")
        self.startData = QLabel("Starting point pressure: 0 kPa")
        self.startData.setStyleSheet("font-size: 13px;")
        self.startData.setFixedSize(400, 30)

        startInputLayout.addWidget(startLabel)
        startInputLayout.addWidget(startInput)
        startLayout.addWidget(self.startData)

        # End input
        endLayout = QVBoxLayout()
        endLayout.setContentsMargins(20, 0, 20, 0)
        endInputLayout = QHBoxLayout()
        endLayout.addLayout(endInputLayout)
        leftLayout.addLayout(endLayout)

        endLabel = QLabel("Set pressure for end point (kPa):")
        endLabel.setStyleSheet("font-size: 15px;")
        endInput = QLineEdit()
        endInput.setValidator(QIntValidator(0, 100000))
        endInput.textChanged.connect(self.changeEndData)
        endInput.setStyleSheet("font-size: 15px;")
        # endInput.setFixedWidth(50)
        self.endData = QLabel("End point pressure: 0 kPa")
        self.endData.setStyleSheet("font-size: 13px;")
        self.endData.setFixedSize(400, 30)

        endInputLayout.addWidget(endLabel)
        endInputLayout.addWidget(endInput)
        endLayout.addWidget(self.endData)

        calcLayout = QVBoxLayout()
        leftLayout.addLayout(calcLayout)

        calcButton = QPushButton("Calculate flow")
        calcButton.setFixedSize(QSize(150, 80))
        calcButton.setStyleSheet("QPushButton {"
                                      "font-size: 15px; background-color: white;"
                                 "}"
                                 "QPushButton:hover {"
                                      "background-color: lightgray;"
                                 "}")
        # PyCharm showing a warning on .connect, but it works.
        calcButton.clicked.connect(lambda: self.calculateFlow(int(self.startData.text().split(":")[1][:-4].strip()), int(self.endData.text().split(":")[1][:-4].strip())))

        calcLayout.addWidget(calcButton, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.flowLabel = QLabel("Flow speed: 0 m/s")
        self.flowLabel.setStyleSheet("font-size: 15px;")
        self.flowLabel.setFixedHeight(30)

        calcLayout.addWidget(self.flowLabel, alignment=Qt.AlignmentFlag.AlignHCenter)



        # Top right layout
        # Pipes
        pipeBox = QWidget()
        rightLayout.addWidget(pipeBox)
        pipeBox.setLayout(topLayout)
        pipeBox.setStyleSheet("QWidget {"
                                  "border: 1px solid black; "
                                  "background-color: rgb(180, 180, 180);"
                              "}")

        topLayout.addWidget(self.clearButton)

        # Bottom right layout
        # Grid (750, 750, 50) is a good size for a window of size (1280, 850)
        self.view = Grid(750, 750, 75) # Width, Height, Square size
        self.view.show()
        rightLayout.addWidget(self.view)

        widget = QWidget()
        widget.setLayout(baseLayout)
        self.setCentralWidget(widget)

    def calculateFlow(self, start, end):
        # two lines below extract the pressure from the text for use in the calculation
        result = start + end
        self.flowLabel.setText("Flow speed: {} m/s".format(result))
        return result

    def clearGrid(self):
        for item in self.view.scene.items():
            # Gets the name of the class to check if it is a pipe and removes it
            if item.__class__.__name__ == 'GridPipe':
                self.view.scene.removeItem(item)
                item.remove()

    def getGrid(self):
        return self.view

    def changeEndData(self, text):
        if text:
            self.endData.setText("End point pressure: {} kPa".format(text))
        else:
            self.endData.setText("End point pressure: 0 kPa")

    def changeStartData(self, text):
        if text:
            self.startData.setText("Starting point pressure: {} kPa".format(text))
        else:
            self.startData.setText("Starting point pressure: 0 kPa")


    # self.pipe = QGraphicsPixmapItem()
    # self.pipe.setPixmap(QPixmap('../Images/StraightPipe.png').scaled(49, 49))
    # self.pipe.setOffset(self.x * 50 + 1, self.y * 50)
    # self.scene.addItem(self.pipe)
    # self.scene.removeItem(self.pipe)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() # Makes the window visible

    app.exec()