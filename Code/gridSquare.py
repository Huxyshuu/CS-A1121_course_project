from PyQt6.QtWidgets import QGraphicsRectItem


class GridSquare(QGraphicsRectItem):
    def __init__(self, x, y, w, h):
        super(GridSquare, self).__init__(x, y, w, h)
        # coordinates are divided by the size of the box for easier readability, (1, 1) instead of (w, h)
        self.x = x / w
        self.y = y / h

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        print("Clicked a square at ({}, {})".format(self.x, self.y))
