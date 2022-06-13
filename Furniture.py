from house_config import *
import utils


class Furniture:

    def __init__(self, name, origin, size, color, img) -> None:
        self.name = name
        self.origin = origin
        self.center = [0, 0]
        self.size = size
        self.color = color
        self.img = img
        self.drag = False
        self.rect = None
        self.encl_param = 5
        # self.enclosure = None
        # self.encl_color = YELLOW
        # self.encl_origin = [self.origin[0] - self.encl_param,
        #                     self.origin[1] - self.encl_param]
        # self.encl_size = [self.size[0]+2*self.encl_param,
        #                   self.size[1]+2*self.encl_param]

        # Do some init method:
        self.update_center_points()

    # def update_enclosure(self):
    #     self.encl_origin = [self.origin[0] - self.encl_param,
    #                         self.origin[1] - self.encl_param]

    def update_center_points(self):
        x, y = self.origin
        self.center = [x+self.size[0]/2, y+self.size[1]/2]

    def set_center(self, center):
        x, y = center
        self.origin = [x-self.size[0]/2, y-self.size[1]/2]

        # Not allow objects move out of the window
        if self.origin[0] < 0:
            self.origin[0] = 0

        if self.origin[1] < 0:
            self.origin[1] = 0

        if self.origin[0] + self.size[0] > WIN_WIDTH:
            self.origin[0] = WIN_WIDTH - self.size[0]

        if self.origin[1] + self.size[1] > WIN_HEIGHT:
            self.origin[1] = WIN_HEIGHT - self.size[1]

        self.update_center_points()
        # self.update_enclosure()

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
