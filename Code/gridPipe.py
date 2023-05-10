from PyQt6.QtWidgets import QGraphicsPixmapItem


class GridPipe(QGraphicsPixmapItem):
    def __init__(self, gridSquare):
        super(GridPipe, self).__init__()
        self.gridSquare = gridSquare

    def remove(self):
        self.gridSquare.setEmpty(True)