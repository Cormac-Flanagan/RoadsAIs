import numpy as np
import pygame
import random
import math
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 20)
WIDTH, HEIGHT = 700, 600
WHITE = (255, 255, 255)
window = pygame.display.set_mode((WIDTH, HEIGHT))

boardX, boardY = 70, 60

board = np.zeros([boardY, boardX])
Qlearn = np.zeros([boardY, boardX])


game_running = True
no_winner = True

AI_wins = 0
AI_lose = 0

iteration = 0
target = 5000

piece_sizeX = WIDTH/boardX
piece_sizeY = HEIGHT/boardY


def draw_screen():
    window.fill((0, 0, 50))
    for (x, y), val in np.ndenumerate(board):
        if val == 1:
            color = (255, 0, 0)
        elif val == -1:
            color = (255, 255, 0)
        else:
            color = (0, 0, 0)
        rect = pygame.Rect(
            [piece_sizeX*y, piece_sizeY*x, piece_sizeX, piece_sizeY])
        pygame.draw.rect(window, color, rect)
        Qtext = myfont.render(str(Qlearn[x][y]), True, WHITE)
        window.blit(Qtext, rect)
    pygame.display.update()


while game_running and iteration < target:
    board = np.zeros([boardY, boardX])
    no_winner = True
    iteration += 1
    while no_winner:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        draw_screen

print(f"AI:{AI_wins} \n OTHERS: {AI_lose}")

print(f'Qlearn \n {Qlearn}')
