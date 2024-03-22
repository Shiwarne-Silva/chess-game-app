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
    loadImages() # only do this once, before the while loop.
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            drawGameState(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()

'''
Responsible for all graphics within a current game state.
'''
def drawGameState(screen, gs):
    drawBoard(screen) # draw squares on the board.
    #add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board)


'''
Draw the squares on the board. top let square is always light
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
'''
draw the pieces on the board using current GameState.board
'''
def drawPieces(screen, board):
    pass



if __name__ == "__main__":
    main()