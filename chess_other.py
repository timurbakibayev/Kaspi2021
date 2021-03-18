def borders(cell_from, cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if y1 > 8 or y2 > 8 or y1 < 1 or y2 < 1:
        return False
    if x1 > 8 or x2 > 8 or x1 < 1 or x2 < 1:
        return False
    return True

# PAWN
def p_allowed(cell_from, cell_to, white):
    black = not white
    x1, y1 = cell_from
    x2, y2 = cell_to
    if (y2 == 1 or y1 == 1) and white:
        return False
    if (y1 == 8 or y2 == 8) and black:
        return False

    if not borders(cell_from, cell_to):
        return False

    if white:
        if y1 == 2 and y2 == 4:
            return True
    else:
        if y1 == 7 and y2 == 5:
            return True

    if white:
        return x1 == x2 and y1 + 1 == y2
    else:
        return x1 == x2 and y1 - 1 == y2


#KING
def k_allowed(cell_from,cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if not borders(cell_from, cell_to):
        return False

    if x1 == x2 and y1 == y2:
        return False

    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        return True
    else:
        return False

#kNIGHT
def n_allowed(cell_from,cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if not borders(cell_from, cell_to):
        return False

    dx = abs(x1 - x2)  # модуль разницы координат X
    dy = abs(y1 - y2)  # модуль разницы координат Y
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        return True
    else:
        return False

#BISHOP
def b_allowed(cell_from,cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if not borders(cell_from, cell_to):
        return False

    if abs(x1 - x2) == abs(y1 - y2):
        return True
    else:
        return False
#ROOK
def r_allowed(cell_from,cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if not borders(cell_from, cell_to):
        return False
    if x1 == y1 and x2 == y2:
        return False
    if x1 == x2 or y1 == y2:
        return True
    else:
        return False

#QUEEN
def q_allowed(cell_from,cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if not borders(cell_from, cell_to):
        return False

    if x1 == y1 and x2 == y2:
        return False

    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 or x1 == x2 or y1 == y2:
        return True
    else:
        return False


def board_move_ok(cell_from, cell_to, board):
    return True
