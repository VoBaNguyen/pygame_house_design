from house_config import *
import utils


class Furniture:

    def __init__(self, name, origin, size, color, img) -> None:
        self.name = name
        self.origin = origin
        self.size = size
        self.color = color
        self.img = img
        self.drag = False
        self.rect = None
        self.encl_param = 5

    def translate(self, points, size):
        [xA, yA], [xB, yB] = points
        xT, yT = size

        xAB, yAB = [xB-xA, yB-yA]
        self.origin[0] = self.origin[0] + utils.sign(xAB) + xT
        self.origin[1] = self.origin[1] + utils.sign(yAB) + yT

    def move_await(self, rect):
        if self.rect.x <= rect.x and self.rect.x+self.size[0] >= rect.x:
            self.origin[0] = rect.x - self.size[0] - self.encl_param

        else:
            self.origin[0] = rect.x + rect.width + self.encl_param

        return 1

    def __repr__(self):
        return f"<Obj {self.name} - {self.origin}>"
