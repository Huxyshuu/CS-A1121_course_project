from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QTransform

from clickableLabel import ClickableLabel


class PipeButtonCreator:
    def __init__(self, pipeList, pipeScale, layout, rotation):
        # Initialize list to hold pipe buttons
        self.pipeButtons = []

        # Loop through each pipe file in the given list
        for pipe in pipeList:
            # Create a new clickable label object
            newPipe = ClickableLabel()

            # Set the type of the label to the current pipe file
            newPipe.setType(pipe)

            # Extract the name of the pipe from the file name
            newPipe.setName(pipe[10:][:-4])

            # Create a transformation object to rotate the pipe image
            transform = QTransform()
            transform.rotate(rotation)

            # Load the pipe image file, scale it to the desired size, and apply the rotation transformation
            newPipe.setPixmap(QPixmap(pipe).scaled(pipeScale, pipeScale).transformed(transform))

            # Set the size of the button to include a margin of 10 pixels
            newPipe.setFixedSize(pipeScale + 10, pipeScale + 10)

            # Center the image inside the button
            newPipe.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # Add the button to the given layout
            layout.addWidget(newPipe)

            # Add the button to the list of pipe buttons
            self.pipeButtons.append(newPipe)

        # Loop through each button in the list of pipe buttons
        for toAddButton in self.pipeButtons:
            # Loop through each button again to compare with the current one
            for otherButton in self.pipeButtons:
                # Check if the button is not the same as the one being compared
                if toAddButton.getName() != otherButton.getName():
                    # If they are different, add the other button to the list of other buttons for the button
                    toAddButton.setOtherButtons(otherButton)

    def returnPipeButtons(self):
        return self.pipeButtons

