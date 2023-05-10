import math
import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow

#custom Classes
from ui import UI

# Creating a subclass of QMainWindow for better control over the window customization
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pipeflow - Hugo")

        #default rotation of the pipes
        self.pipeRotation = 0

        # Sets a fixed window size
        self.setFixedSize(QSize(1280, 850))

        # Creates the UI for the program
        self.ui = UI(self)

        #self.view is initalized in the UI method
        self.grid = self.view



    def calculateFlow(self, start, end):
        # two lines below extract the pressure from the text for use in the calculation
        startHeight, endHeight = self.grid.getCalcPoints()

        loss = (4 * 0.01 * math.pow(0.28, 2)) / (math.pow(math.pi, 2) * math.pow(0.3, 5) * 997)

        #v = sqrt(2(P_start - P_end) + 2(pgh_end - pgh_start - h_end*f + h_start*f) / p)
        bernoulli = 2 * (start - end) + 2 * (997 * 9.81 * endHeight - 997 * 9.81 * startHeight - endHeight * loss + startHeight * loss) / 997

        if bernoulli > 0:
            result = math.sqrt(bernoulli)
            # flowLabel is found in UI class
            self.flowLabel.setText("<p>Flow speed: {} m/s</p>".format(result))
            return result
        else:
            self.flowLabel.setText('<p style="color: red; text-align: center;">Flow speed: ERROR m/s</p>\nPlease set the starting value to be greater than the end')
            return 0

    def clearGrid(self):
        for item in self.grid.scene.items():
            # Gets the name of the class to check if it is a pipe and removes it
            if item.__class__.__name__ == 'GridPipe':
                self.grid.scene.removeItem(item)
                item.remove()

    def rotatePipes(self):
        if self.pipeRotation == 270:
            self.pipeRotation = 0
        else:
            self.pipeRotation += 90
        self.grid.rotate(self.pipeRotation)
        self.ui.refresh(self.pipeRotation)

    def getGrid(self):
        return self.grid

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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() # Makes the window visible

    app.exec()