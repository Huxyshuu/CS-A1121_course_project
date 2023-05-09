from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, \
    QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QGraphicsPixmapItem, QLineEdit
from PyQt6.QtGui import QPalette, QColor, QPixmap, QIntValidator

#custom Classes
from pipeButtonCreator import PipeButtonCreator
from grid import Grid


class UI:
    def __init__(self, main):
        self.main = main


        # Layout inits
        self.baseLayout = QHBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()

        # Nesting layouts for proper grouping of elements
        self.baseLayout.addLayout(self.leftLayout)
        self.baseLayout.addLayout(self.rightLayout)

        # self.notice()


        # creates grid buttons i.e. pipes, clear and rotate
        self.gridButtons(0)

        # creates inputs and output for the calculations
        self.calculatorUI()

        # Grid (750, 750, 50) is a good size for a window of size (1280, 850)
        self.main.view = Grid(750, 750, 75)  # Width, Height, Square size
        self.main.view.show()
        self.rightLayout.addWidget(self.main.view)

        widget = QWidget()
        widget.setLayout(self.baseLayout)
        self.main.setCentralWidget(widget)

    def notice(self):
        noticeText = "<b>Notice:</b> <br> Start and End points are currently chosen at random everytime the program is opened."
        notice = QLabel(
            noticeText)
        notice.setMaximumSize(500, 50)
        notice.setStyleSheet(' border: 2px solid rgb(255, 84, 124); padding: 2px; background-color: rgb(255, 186, 213)')
        notice.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.leftLayout.addWidget(notice)

    def gridButtons(self, rotation):
        self.main.rotateButton = QPushButton("Rotate")
        self.main.rotateButton.setFixedSize(QSize(100, 60))
        self.main.rotateButton.clicked.connect(self.main.rotatePipes)
        self.main.rotateButton.setStyleSheet("QPushButton {"
                                            "background-color: white;"
                                            "font-size: 15px;"
                                            "}"

                                            "QPushButton:hover {"
                                            "background-color: rgb(255, 220, 220);"
                                            "border: 2px solid rgb(235, 100, 100);"
                                            "}")
        self.topLayout.addWidget(self.main.rotateButton)



        self.pipeList = ['../Images/StraightPipe.png',
                    '../Images/CornerPipe.png',
                    '../Images/TPipe.png',
                    '../Images/SectionPipe.png']

        # Adding pipes to topLayout
        self.main.pipeButtons = PipeButtonCreator(self.pipeList, 50,
                                                  self.topLayout,
                                                  rotation).returnPipeButtons()


        # Pipes
        self.pipeBox = QWidget()
        self.rightLayout.addWidget(self.pipeBox)
        self.pipeBox.setLayout(self.topLayout)
        self.pipeBox.setStyleSheet("QWidget {"
                              "border: 1px solid black; "
                              "background-color: rgb(180, 180, 180);"
                              "}")

        self.main.clearButton = QPushButton("Clear Grid!")
        self.main.clearButton.setFixedSize(QSize(100, 60))
        self.main.clearButton.clicked.connect(self.main.clearGrid)
        self.main.clearButton.setStyleSheet("QPushButton {"
                                            "background-color: white;"
                                            "font-size: 15px;"
                                            "}"

                                            "QPushButton:hover {"
                                            "background-color: rgb(255, 220, 220);"
                                            "border: 2px solid rgb(235, 100, 100);"
                                            "}")

        self.addClearButton()

    def addClearButton(self):
        self.topLayout.addWidget(self.main.clearButton)



    def refresh(self, rotation):
        #Remove old instances
        for icon in self.main.pipeButtons:
            icon.setParent(None)
        self.main.clearButton.setParent(None)

        self.main.pipeButtons = PipeButtonCreator(self.pipeList, 50,
                                                  self.topLayout,
                                                  rotation).returnPipeButtons()
        self.addClearButton()

    def calculatorUI(self):
        # Left side buttons
        # Start input
        startLayout = QVBoxLayout()
        startLayout.setContentsMargins(20, 0, 20, 0)
        startInputLayout = QHBoxLayout()
        startInputLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        startLayout.addLayout(startInputLayout)
        self.leftLayout.addLayout(startLayout)

        startLabel = QLabel("Set pressure for starting point (kPa):")
        startLabel.setStyleSheet("font-size: 15px;")
        startInput = QLineEdit()
        startInput.setValidator(QIntValidator(0, 100000))
        startInput.textChanged.connect(self.main.changeStartData)
        startInput.setStyleSheet("font-size: 15px;")
        self.main.startData = QLabel("Starting point pressure: 0 kPa")
        self.main.startData.setStyleSheet("font-size: 13px;")
        self.main.startData.setFixedSize(400, 30)

        startInputLayout.addWidget(startLabel)
        startInputLayout.addWidget(startInput)
        startLayout.addWidget(self.main.startData)

        # End input
        endLayout = QVBoxLayout()
        endLayout.setContentsMargins(20, 0, 20, 0)
        endInputLayout = QHBoxLayout()
        endLayout.addLayout(endInputLayout)
        self.leftLayout.addLayout(endLayout)

        endLabel = QLabel("Set pressure for end point (kPa):")
        endLabel.setStyleSheet("font-size: 15px;")
        endInput = QLineEdit()
        endInput.setValidator(QIntValidator(0, 100000))
        endInput.textChanged.connect(self.main.changeEndData)
        endInput.setStyleSheet("font-size: 15px;")
        # endInput.setFixedWidth(50)
        self.main.endData = QLabel("End point pressure: 0 kPa")
        self.main.endData.setStyleSheet("font-size: 13px;")
        self.main.endData.setFixedSize(400, 30)

        endInputLayout.addWidget(endLabel)
        endInputLayout.addWidget(endInput)
        endLayout.addWidget(self.main.endData)

        calcLayout = QVBoxLayout()
        self.leftLayout.addLayout(calcLayout)

        calcButton = QPushButton("Calculate flow")
        calcButton.setFixedSize(QSize(150, 80))
        calcButton.setStyleSheet("QPushButton {"
                                 "font-size: 15px; background-color: white;"
                                 "}"
                                 "QPushButton:hover {"
                                 "background-color: lightgray;"
                                 "}")
        # PyCharm showing a warning on .connect, but it works.
        calcButton.clicked.connect(
            lambda: self.main.calculateFlow(int(self.main.startData.text().split(":")[1][:-4].strip()),
                                            int(self.main.endData.text().split(":")[1][:-4].strip())))

        calcLayout.addWidget(calcButton, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.main.flowLabel = QLabel("Flow speed: 0 m/s")
        self.main.flowLabel.setStyleSheet("font-size: 15px;")
        self.main.flowLabel.setFixedHeight(70)

        calcLayout.addWidget(self.main.flowLabel, alignment=Qt.AlignmentFlag.AlignHCenter)


