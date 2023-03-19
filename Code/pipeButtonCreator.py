from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from clickableLabel import ClickableLabel


class PipeButtonCreator:
    def __init__(self, pipeList, pipeScale, layout):
        self.pipeButtons = []

        for pipe in pipeList:
            newPipe = ClickableLabel()
            newPipe.setType(pipe)
            newPipe.setName(pipe[10:][:-4])

            newPipe.setPixmap(QPixmap(pipe).scaled(pipeScale, pipeScale))
            newPipe.setFixedSize(pipeScale + 10, pipeScale + 10)  # offset of 10 as margin
            newPipe.setAlignment(Qt.AlignmentFlag.AlignCenter)

            layout.addWidget(newPipe)

            self.pipeButtons.append(newPipe)

        #Add other pipe buttons to each pipe object
        for toAddButton in self.pipeButtons:
            for otherButton in self.pipeButtons:
                if toAddButton.getName() != otherButton.getName():
                    toAddButton.setOtherButtons(otherButton)







    def returnPipeButtons(self):
        return self.pipeButtons

