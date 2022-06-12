import pygame
import os

# Color
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
# Font
pygame.font.init()
FONT = pygame.font.SysFont("bahnschrift", 25)
# Window size
WIN_WIDTH = 800
WIN_HEIGHT = 800
INNER_WIDTH = WIN_WIDTH - 2
INNER_HEIGHT = WIN_HEIGHT - 2
# Furniture
TABLE_SIZE = [250, 200]
CHAIR_SIZE = [50, 50]
TV_SIZE = [150, 150]
# Image
IMG_TABLE = pygame.image.load(os.path.join("imgs", "table.png"))
IMG_CHAIR = pygame.image.load(os.path.join("imgs", "chair.png"))
IMG_TV = pygame.image.load(os.path.join("imgs", "tv.png"))
IMG_BG = pygame.image.load(os.path.join("imgs", "floor.png"))
IMG_TABLE = pygame.transform.scale(IMG_TABLE, TABLE_SIZE)
IMG_CHAIR = pygame.transform.scale(IMG_CHAIR, CHAIR_SIZE)
IMG_TV = pygame.transform.scale(IMG_TV, TV_SIZE)
IMG_BG = pygame.transform.scale(IMG_BG, [WIN_WIDTH, WIN_HEIGHT])
