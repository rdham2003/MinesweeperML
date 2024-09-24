def revealTile(board_revealed, board_unrevealed, i, j):
    if board_unrevealed[i][j] == 0:
        stack = []
        stack.append(i,j)
        while len(stack) != 0:
            curPos = stack.pop()
            x = curPos[0]
            y = curPos[1]
            if (not (board_unrevealed))
    else:
        board_revealed[i][j] = board_unrevealed[i][j]

def gameOver(minesweeper):
    for i in range(len(minesweeper)):
        for j in range(len(minesweeper[0])):
            if minesweeper[i][j] == 'M':
                return True
    return False