import numpy as np
import pygame
import random
import math
import time
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 20)
WIDTH, HEIGHT = 700, 600
WHITE = (255, 255, 255)
window = pygame.display.set_mode((WIDTH, HEIGHT))

boardX, boardY = 70, 70

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

current_path = []


def determine_move(Xcur, Ycur, endPos, roads, current_path=[]):
    possible_moves = [(Xcur+1, Ycur), (Xcur-1, Ycur),
                      (Xcur, Ycur+1), (Xcur, Ycur-1)]
    next_move = {}

    total_travel = Xcur + Ycur
    first_choice = (Xcur, Ycur)
    for i in possible_moves:

        if not (0 <= i[-1] < boardY) or not (0 <= i[0] < boardX):
            possible_moves.remove(i)

    for z in current_path:
        if z in possible_moves:
            possible_moves.remove(z)
    print(possible_moves)
    if len(possible_moves) == 0:
        print("WHAT")

    for move in possible_moves:
        if roads[move[0]][move[1]] != 1:
            prediction = math.sqrt(
                (endPos[0]-move[0]) ** 2 + (endPos[1]-move[1])**2) - roads[move[-1]][move[0]]/100
            next_move[(prediction)] = move

    if len(next_move) > 0:
        minMove = min(next_move.keys())
        first_choice = next_move[minMove]
        current_path.append(first_choice)
    else:
        current_path = [(Xcur, Ycur)]

    print(f"c: {(Xcur, Ycur)} n:{first_choice} p:{min(next_move.keys())} e:{endPos}")
    time.sleep(0)

    return first_choice, current_path


def draw_screen():
    window.fill((0, 0, 50))
    for (x, y), val in np.ndenumerate(board):
        color = (0, val, 0)
        rect = pygame.Rect(
            [piece_sizeX*y, piece_sizeY*x, piece_sizeX, piece_sizeY])
    for (x, y), val in np.ndenumerate(road_board):
        color = (val, 0, val/2)
        rect = pygame.Rect(
            [piece_sizeX*y, piece_sizeY*x, piece_sizeX, piece_sizeY])
        pygame.draw.rect(window, color, rect)
        # Qtext = myfont.render(str(Qlearn[x][y]), True, WHITE)
    pygame.display.update()


def gen_roads(cities, roadmap):
    for it in range(10):
        print(it)
        for start in cities:
            starting_pos = cities[start]
            for destination in cities:
                ending_pos = cities[destination]
                current_pos = starting_pos
                path = []
                while current_pos != ending_pos:
                    (nx, ny), path = determine_move(current_pos[0], current_pos[-1],
                                                    ending_pos, roadmap, path)
                    current_pos = (nx, ny)
                    print((current_pos != ending_pos))
                for i in path:
                    roadmap[i[-1]][i[0]] += 1


while game_running and iteration < target:
    board = np.zeros([boardY, boardX])
    road_board = np.zeros([boardY, boardX])
    houseNum = 10
    houses = {10: (5, 0), 11: (20, 25)}
    # for y in range(boardY):
    #     for x in range(boardX):
    #         if random.random() <= abs(x - (boardX*2))/1000:
    #             board[y][x] = houseNum
    #             houses[houseNum] = (y, x)
    #             houseNum += 1

    board[5, 0] = 10
    board[20, 25] = 11

    gen_roads(houses, road_board)
    no_winner = True
    iteration += 1

    while no_winner:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            draw_screen()

print(f"AI:{AI_wins} \n OTHERS: {AI_lose}")

print(f'Qlearn \n {Qlearn}')
