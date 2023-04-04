import os
import keyboard
from time import sleep
import random
DIMENSION = 10
board = [
    [
        "╔", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "╗"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"
    ],
    [
        "╚", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "╝"
    ],
]
def mknull():
    for i in range(12):
        for j in range(12):
            if board[i][j] not in ("╔", "═", "╗", "║", "╚", "╝"):
                board[i][j] = ' '
x = 5
y = 3
body = []
food = [None, None]
food[0], food[1] = random.randint(1, 10), random.randint(1, 10)

board[x][y] = "►"
board[x][y-1] = "■"
board[x][y-2] = "■"
board[food[0]][food[1]] = "•"
body.append((x, y-2))
body.append((x, y-1))
string = '\n'.join([''.join(row) for row in board])
print(f"{string}")
while (s := keyboard.read_key()) != 'esc':
    mknull()
    
    board[food[0]][food[1]] = "•"

    def fd():
        food[0], food[1] = random.randint(1, 10), random.randint(1, 10)
        board[food[0]][food[1]] = "•"
    T = [True for i, (col, row) in enumerate(body) if col == x and row == y]
    
    if s == 'right':
        body.append((x, y))
        # board[x][y] = "■"
        y += 1
        if y == 0 or y == 11 or [True for i, (col, row) in enumerate(body) if col == x and row == y]:
            print('Error')
            break
        board[x][y] = "►"
        if x != food[0] or y != food[1]:
            body.pop(0)
        else:
            fd()
    elif s == 'left':
        body.append((x, y))
        # board[x][y] = "■"
        y -= 1
        if y == 0 or y == 11 or [True for i, (col, row) in enumerate(body) if col == x and row == y]:
            print('Error')
            break
        board[x][y] = '◄'
        if x != food[0] or y != food[1]:
            body.pop(0)
        else:
            fd()
    elif s == 'down':
        body.append((x, y))
        # board[x][y] = "■"
        x += 1
        if x == 0 or x == 11 or [True for i, (col, row) in enumerate(body) if col == x and row == y]:
            print('Error')
            break
        board[x][y] = "▼"
        if x != food[0] or y != food[1]:
            body.pop(0)
        else:
            fd()
    elif s == 'up':
        body.append((x, y))
        # board[x][y] = "■"
        x -= 1
        if x == 0 or x == 11 or [True for i, (col, row) in enumerate(body) if col == x and row == y]:
            print('Error')
            break
        board[x][y] = "▲"
        if x != food[0] or y != food[1]:
            body.pop(0)
        else:
            fd()

    for i, (col, row) in enumerate(body):
        board[col][row] = "■"

    sleep(0.5)
    _ = os.system('cls')

    string = '\n'.join([''.join(row) for row in board])
    print(f"{string}")
