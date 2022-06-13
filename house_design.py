import pygame
import time
import random
from Furniture import Furniture
import utils
from house_config import *


class House:

    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('House Design')

        self.furnitures = [
            Furniture("Table", [10, 10], TABLE_SIZE, RED, IMG_TABLE),
            Furniture("Chair", [200, 10], CHAIR_SIZE, RED, IMG_CHAIR),
            Furniture("TV", [500, 10], TV_SIZE, RED, IMG_TV),
        ]

        # Functional attribure
        self.drag = False
        self.selected = None

    def message(self, msg, color):
        mesg = FONT.render(msg, True, color)
        self.window.blit(mesg, [WIN_WIDTH / 6, WIN_HEIGHT / 3])

    def label(self, msg, color, origin):
        label = FONT.render(msg, True, color)
        self.window.blit(label, [origin[0]-label.get_width()/2, origin[1]])

    def draw(self):
        # Draw background
        self.window.blit(IMG_BG, (0, 0))

        # Draw border
        # Border coordinates
        # top_left = [0, 0]
        # top_right = [INNER_WIDTH, 0]
        # bot_right = [INNER_WIDTH, INNER_HEIGHT]
        # bot_left = [0, INNER_HEIGHT]
        # pygame.draw.lines(self.window, BLACK, True, [
        #                   top_left, top_right, bot_right, bot_left], width=2)

        # Draw furniture
        for furniture in self.furnitures:
            # Draw enclosure
            # furniture.enclosure = pygame.draw.rect(self.window, furniture.encl_color, [
            #     furniture.encl_origin, furniture.encl_size])

            # Draw furniture
            furniture.rect = pygame.draw.rect(self.window, furniture.color, [
                furniture.origin, furniture.size])
            self.window.blit(furniture.img, furniture.rect)
            # self.label(furniture.name, GREEN, furniture.origin)

        # Draw connecting line
        if self.selected:
            for furn in [x for x in self.furnitures if id(x) != id(self.selected)]:
                print(self.selected.center)
                print(furn.center)
                pygame.draw.line(self.window, GREEN,
                                 self.selected.center, furn.center, width=2)

                d = utils.distance(self.selected.center, furn.center)
                mid_point = utils.mid(self.selected.center, furn.center)
                self.label(str(d), BLACK, mid_point)

        pygame.display.update()

    ######################################################
    # Functional Methods
    ######################################################

    def resolve_overlap(self):
        '''
        Check if 2 furniture are overlapped. If yes, separate them a little bit
        '''
        is_overlap = False
        for furn in [x for x in self.furnitures if id(x) != id(self.selected)]:
            if self.selected.rect.colliderect(furn.rect):
                is_overlap = True
                # Separate these shapes a little bit
                self.selected.move_await(furn.rect)
                break
        return is_overlap

    def loop(self):
        game_over = False
        game_close = False
        self.clock.tick(60)
        x1 = WIN_WIDTH / 2
        y1 = WIN_HEIGHT / 2

        while not game_over:
            self.window.fill(BLUE)

            # Each furniture will have origin and size. From these info, we will able to calculate its area
            # Then we'll able to drag
            # When user MOUSEBUTTONDOWN => Drag = True. Check if they click any object
            # If yes, set the center of that object to the cursor
            # When the cursor change, rerender the object
            # When user MOUSEBUTTONUP => Drag = False, release the object

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True

                    if event.key == pygame.K_c:
                        self.loop()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.drag = True
                    # Find selected object
                    for furniture in self.furnitures:
                        if furniture.rect.collidepoint(event.pos):
                            self.selected = furniture
                            self.selected.set_center(pygame.mouse.get_pos())
                            self.resolve_overlap()
                            break

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.selected:
                        self.resolve_overlap()
                    self.drag, self.selected = False, None

                elif event.type == pygame.MOUSEMOTION:
                    if self.drag and self.selected:
                        # Check if selected obj overlap another obj:
                        self.selected.set_center(pygame.mouse.get_pos())
                        # self.resolve_overlap()

            self.draw()


if __name__ == "__main__":
    game = House()
    game.loop()
