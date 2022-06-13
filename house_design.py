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
        self.window_rect = self.window.get_rect()
        self.prev_pos = pygame.mouse.get_pos()
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

        # Draw furniture
        for furniture in self.furnitures:
            # Draw furniture for the first time
            if furniture.rect == None:
                furniture.rect = pygame.draw.rect(self.window, furniture.color, [
                    furniture.origin, furniture.size])

            # Draw enclosure
            furniture.enclosure = furniture.rect.copy()
            furniture.enclosure.inflate_ip(10, 10)
            pygame.draw.rect(self.window, YELLOW, furniture.enclosure)

            # Update furniture frame
            self.window.blit(furniture.img, furniture.rect)
            # self.label(furniture.name, GREEN, furniture.rect.center)

        # Draw connecting line
        if self.selected:
            for furn in [x for x in self.furnitures if id(x) != id(self.selected)]:
                pygame.draw.line(self.window, GREEN,
                                 self.selected.rect.center, furn.rect.center, width=2)

                d = utils.distance(self.selected.rect.center, furn.rect.center)
                mid_point = utils.mid(
                    self.selected.rect.center, furn.rect.center)
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
                            self.selected.rect.center = pygame.mouse.get_pos()
                            break

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.drag, self.selected = False, None

                elif event.type == pygame.MOUSEMOTION:
                    if self.drag and self.selected:
                        # Check if selected obj overlap another obj:
                        # If enclosure is overlap, if we move object toward another object => Not allow
                        overlap_furn = None
                        for furn in [x for x in self.furnitures if id(x) != id(self.selected)]:
                            if self.selected.enclosure.colliderect(furn.enclosure):
                                overlap_furn = furn
                                break

                        # Get motion vector:
                        moving_direction = utils.vector(
                            self.prev_pos, pygame.mouse.get_pos())

                        vT = utils.vector(
                            self.selected.rect.center, pygame.mouse.get_pos())
                        if overlap_furn:
                            # Determine relative position
                            rel_pos = utils.relative_pos(
                                self.selected.rect, overlap_furn.rect)

                            print(
                                f"{moving_direction} - {overlap_furn} - {rel_pos}")
                            is_move = False
                            if rel_pos == "left" and utils.sign(moving_direction[0]) != 1:
                                is_move = True

                            elif rel_pos == "right" and utils.sign(moving_direction[0]) != -1:
                                is_move = True

                            elif rel_pos == "top" and utils.sign(moving_direction[1]) != 1:
                                is_move = True

                            elif rel_pos == "bottom" and utils.sign(moving_direction[1]) != -1:
                                is_move = True

                            if is_move:
                                self.selected.rect.move_ip(vT[0], vT[1])

                        else:
                            self.selected.rect.move_ip(vT[0], vT[1])

                        self.selected.rect.clamp_ip(self.window_rect)

                        # Save previous mouse position
                        self.prev_pos = pygame.mouse.get_pos()

            self.draw()


if __name__ == "__main__":
    game = House()
    game.loop()
