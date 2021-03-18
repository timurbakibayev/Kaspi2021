from chess import *

allow_functions = {
        "K": k_allowed,
        "N": n_allowed,
        "R": r_allowed,
        "P": p_allowed,
        "Q": q_allowed,
        "B": b_allowed,
        "PE": pe_allowed,
    }


def attacked_1_8(cell, board, by_color):
    return attacked(coord(cell), board, by_color)


def attacked(cell, board, by_color):
    x_to,y_to = uncoord(cell)
    for i in range(len(board)):
        for j in range(len(board)):
            color, fig = board[i][j]
            x,y = uncoord((i,j))
            if color == by_color:
                if fig == "P":
                    fig = "PE"
                if allow_functions[fig]((x,y),(x_to,y_to),by_color):
                    if middle_empty((i, j), (cell[0], cell[1]), board):
                        return True
    return False


def middle_attacked(cell1, cell2, board, by_color):
    for cell in middle(cell1, cell2):
        if attacked(cell, board, by_color):
            return True
    return False


def middle_empty(cell1, cell2, board):
    i,j = cell1
    i_to, j_to = cell2
    for cell in middle((i,j),(i_to,j_to)):
        if not empty(board[cell[0]][cell[1]]):
            return False
    return True



def middle(cell1, cell2):
    i,j = cell1
    i_to,j_to = cell2
    di, dj = 0, 0
    if i_to > i:
        di = 1
    elif i_to < i:
        di = -1
    if j_to > j:
        dj = 1
    elif j_to < j:
        dj = -1

    cells = []
    counter = 0
    while (i, j) != (i_to, j_to) and counter < 100:
        counter += 1
        i += di
        j += dj
        if (i, j) != (i_to, j_to):
            cells.append((i,j))

    return cells


def coord(cell1):
    x,y = cell1
    i,j = 8-y, x-1
    return i,j


def uncoord(cell1):
    i,j = cell1
    x,y = j+1, 8-i
    return x,y


def empty(cell_content):
    return cell_content == "  "


def board_move_ok(cell_from, cell_to, board):
    if out_of_range(cell_from, cell_to):
        return False
    i, j = coord(cell_from)
    i_to, j_to = coord(cell_to)
    color, figure = board[i][j]
    color_to, figure_to = board[i_to][j_to]
    if color == "W":
        by_color = "B"
    else:
        by_color = "W"

    if figure == "K" and not attacked(coord(cell_from), board, by_color):
        # Check castling
        castling = False
        # White
        if color == "W" and coord(cell_from) == (7,4) and coord(cell_to) == (7,2) and board[7][0] == "WR":
            if middle_empty((7, 4), (7, 0), board) and not middle_attacked((7, 4), (7, 0), board, "B"):
                return True

        if color == "W" and coord(cell_from) == (7,4) and coord(cell_to) == (7,6) and board[7][7] == "WR":
            if middle_empty((7,4),(7,7), board) and not middle_attacked((7, 4), (7, 7), board, "B"):
                # Check Schach later
                return True

        # Black
        if color == "B" and coord(cell_from) == (0,4) and coord(cell_to) == (0,2) and board[0][0] == "BR":
            if middle_empty((0,4),(0,0), board) and not middle_attacked((0, 4), (0, 0), board, "W"):
                # Check Schach later
                return True

        if color == "B" and coord(cell_from) == (0,4) and coord(cell_to) == (0,6) and board[0][7] == "BR":
            if middle_empty((0,4),(0,7), board) and not middle_attacked((0, 4), (0, 7), board, "W"):
                # Check Schach later
                return True

        # Middle_empty and Middle_not_under_attack

        # check if Schach and figure == king

    eating = not empty(board[i_to][j_to])

    if color == color_to:
        return False

    if figure != "P" or empty(board[i_to][j_to]):
        if not allow_functions[figure](cell_from, cell_to, color == "W"):
            return False

    if figure == "N":
        return True

    if figure == "P" and eating:
        if not allow_functions["PE"](cell_from, cell_to, color == "W"):
            return False

    if not middle_empty((i,j),(i_to,j_to), board):
        return False

    # check if Schach

    return True

# TODO: If King and currently under attack, cannot castle
# TODO: If King, after move, should not be under attack
