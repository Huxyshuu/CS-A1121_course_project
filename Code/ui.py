from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QLineEdit
from PyQt6.QtGui import QIntValidator

#custom Classes
from pipeButtonCreator import PipeButtonCreator
from grid import Grid


class UI:
    def __init__(self, main):
        self.main = main

        self.pipeImages = ['../Images/StraightPipe.png',
                           '../Images/CornerPipe.png',
                           '../Images/TPipe.png',
                           '../Images/SectionPipe.png']

        # Layout inits
        self.baseLayout = QHBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()

        # Nesting layouts for proper grouping of elements
        self.baseLayout.addLayout(self.leftLayout)
        self.baseLayout.addLayout(self.rightLayout)

        # create small notice label
        self.notice()

        # Grid (750, 750, 50) is a good size for a window of size (1280, 850)
        GRID_WIDTH = 750
        GRID_HEIGHT = 750
        SQUARE_SIZE = 75

        self.grid = Grid(GRID_WIDTH, GRID_HEIGHT, SQUARE_SIZE)
        self.grid.show()

        # creates grid buttons i.e. pipes, clear and rotate
        DEFAULT_ROTATION = 0
        self.gridButtons(DEFAULT_ROTATION)

        # creates inputs and output for the calculations
        self.calculatorUI()

        self.rightLayout.addWidget(self.grid)

        widget = QWidget()
        widget.setLayout(self.baseLayout)
        self.main.setCentralWidget(widget)

    def notice(self):
        noticeText = "<b>Instructions:</b> <br> 1. Choose the desired start and end point heights by clicking on colored squares in the grid" \
                     "<br>2. Build a pipeline connecting both points by placing pipes and rotating them" \
                     '<br>3. Enter the start and end pressures in (kPa) and press "Calculate Flow!"' \
                     '<br><br>The y-axis of the grid is height and x-axis the width, each square is 1m x 1m'
        notice = QLabel(noticeText)
        notice.setMaximumSize(500, 110)
        notice.setStyleSheet(' text-align: center; border: 2px solid rgb(255, 206, 79); padding: 2px; background-color: rgb(255, 237, 191)')
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

        # Adding pipes to topLayout
        self.main.pipeButtons = PipeButtonCreator(self.pipeImages, 50,
                                                  self.topLayout,
                                                  rotation).returnPipeButtons()


        # Toolbar for pipes, rotate and clear
        self.toolBar = QWidget()
        self.rightLayout.addWidget(self.toolBar)
        self.toolBar.setLayout(self.topLayout)
        self.toolBar.setStyleSheet("QWidget {"
                              "border: 1px solid black; "
                              "background-color: rgb(180, 180, 180);"
                              "}")

        self.main.clearButton = QPushButton("Clear Grid!")
        self.main.clearButton.setFixedSize(QSize(100, 60))
        self.main.clearButton.clicked.connect(self.grid.clearGrid)
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
        #Remove old instances of buttons
        for icon in self.main.pipeButtons:
            icon.setParent(None)
        self.main.clearButton.setParent(None)

        # Create new buttons with new rotation
        self.main.pipeButtons = PipeButtonCreator(self.pipeImages, 50,
                                                  self.topLayout,
                                                  rotation).returnPipeButtons()
        self.addClearButton()

    # Last 2 methods default the pressure to 0 if input fields are empty
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

    def calculatorUI(self):
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
        self.leftLayout.addLayout(endLayout)

        endLabel = QLabel("Set pressure for end point (kPa):")
        endLabel.setStyleSheet("font-size: 15px;")
        endInput = QLineEdit()
        endInput.setValidator(QIntValidator(0, 100000))
        endInput.textChanged.connect(self.changeEndData)
        endInput.setStyleSheet("font-size: 15px;")
        self.endData = QLabel("End point pressure: 0 kPa")
        self.endData.setStyleSheet("font-size: 13px;")
        self.endData.setFixedSize(400, 30)

        endInputLayout.addWidget(endLabel)
        endInputLayout.addWidget(endInput)
        endLayout.addWidget(self.endData)

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

        calcButton.clicked.connect(
            lambda: self.main.calculateFlow(int(self.startData.text().split(":")[1][:-4].strip()),
                                            int(self.endData.text().split(":")[1][:-4].strip())))

        calcLayout.addWidget(calcButton, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.main.flowLabel = QLabel("Flow speed: 0 m/s")
        self.main.flowLabel.setStyleSheet("font-size: 15px;")
        self.main.flowLabel.setFixedHeight(70)

        calcLayout.addWidget(self.main.flowLabel, alignment=Qt.AlignmentFlag.AlignHCenter)


