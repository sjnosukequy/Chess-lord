import pygame

# Screen components
TILE_SIZE = 64
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOARD_SIZE = TILE_SIZE * 8
BOARD_X = (SCREEN_WIDTH-BOARD_SIZE)//2
BOARD_Y = int((SCREEN_HEIGHT / 2) - (BOARD_SIZE / 2))
IMG_SCALE = (TILE_SIZE - 2, TILE_SIZE - 6)

# Basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game colors
SMALL_TEXT_COLOR = (241, 250, 238)
LARGE_TEXT_COLOR = (230, 57, 70)
BG_COLOR = (58, 77, 57)
BG_COLOR_LIGHT = (115, 144, 114)
TILE_COLOR_LIGHT = (213, 213, 213)
TILE_COLOR_DARK = (0, 0, 0)
HIGHLIGHT_COLOR = (51, 153, 255)

# Create screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Converts 8x8 grid locations to pixel coordinates
def to_coords(x, y):
    return BOARD_X + x * TILE_SIZE, BOARD_Y + y * TILE_SIZE
