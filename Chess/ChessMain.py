"""
This is the main driver file. it will be responsible for handling user input and displaying and current gamestate object.
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512 #400 is also good
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Init global dictionary of images.
'''
def loadImages():
    peices = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
    for peice in peices:
        IMAGES[peice] = p.transform.scale(p.image.load("images/" + peice + ".png"), (SQ_SIZE, SQ_SIZE))
        # Can access an image by saying 'IMAGES[wp]'

'''
Main driver will handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)

main()