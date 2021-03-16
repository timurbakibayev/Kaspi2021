def borders(cell_from, cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if y1 > 8 or y2 > 8 or y1 < 1 or y2 < 1:
        return False
    if x1 > 8 or x2 > 8 or x1 < 1 or x2 < 1:
        return False
    return True


def p_allowed(cell_from,cell_to,white):
    black = not white
    x1, y1 = cell_from
    x2, y2 = cell_to
    if (y2 == 1 or y1 == 1) and white:
        return False
    if (y1 == 8 or y2 == 8) and black:
        return False
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


def board_move_ok(cell_from, cell_to, board):
    return True


def k_allowed(cell_from,cell_to):
    return borders(cell_from, cell_to) and max(abs(cell_from[1]-cell_to[1]), abs(cell_from[0]-cell_to[0])) == 1
