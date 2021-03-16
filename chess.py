def p_allowed(cell_from,cell_to,white):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if white:
        return x1 == x2 and y1 + 1 == y2
    else:
        return x1 == x2 and y1 - 1 == y2


def board_move_ok(cell_from, cell_to, board):
    return True