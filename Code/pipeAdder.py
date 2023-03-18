from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

from clickableLabel import ClickableLabel


class PipeAdder:
    def __init__(self, pipeList, pipeScale, layout):
        self.pipeButtons = {}

        for pipe in pipeList:
            newPipe = ClickableLabel()
            newPipe.setName(pipe[10:][:-4])

            newPipe.setPixmap(QPixmap(pipe).scaled(pipeScale, pipeScale))
            newPipe.setFixedSize(pipeScale + 10, pipeScale + 10)  # offset of 10 as margin
            newPipe.setAlignment(Qt.AlignmentFlag.AlignCenter)

            layout.addWidget(newPipe)

            self.pipeButtons[pipe[10:][:-4]] = newPipe






    def returnPipeButtons(self):
        return self.pipeButtons

