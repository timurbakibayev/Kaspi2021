def pe_allowed(cell_from,cell_to,white):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if (x1, y1) == (x2, y2):
        return False
    if white:
        return y1+1 == y2 and abs(x1-x2) == 1
    else:
        return y1-1 == y2 and abs(x1-x2) == 1


def out_of_range(cell_from, cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    return not (
        1 <= y1 <= 8 and
        1 <= x1 <= 8 and
        1 <= y2 <= 8 and
        1 <= x2 <= 8
    )



def p_allowed(cell_from,cell_to,white):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if (x1, y1) == (x2, y2):
        return False
    if not(
        1 <= y1 <= 8 and
        1 <= x1 <= 8 and
        1 <= y2 <= 8 and
        1 <= x2 <= 8
    ):
        return False

    if x1 != x2:
        return False
    if white:
        if y1 == 2 and y2 == 4:
            return True
        return y1+1 == y2
    else:
        if y1 == 7 and y2 == 5:
            return True
        return y1-1 == y2

def k_allowed(cell_from,cell_to,white=False):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if (x1, y1) == (x2, y2):
        return False

    if (1 <= x1 <= 8) and (1 <= x2 <= 8) and (1 <= y1 <= 8) and (1 <= y2 <= 8) and \
        ((abs(x1-x2) == 1 and abs(y1-y2) == 1) or (x1 == x2 and abs(y1-y2) == 1)
         or (y1 == y2 and abs(x1-x2) == 1)):
        return True
    else:
        return False

def r_allowed(cell_from,cell_to,white=False):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if (x1, y1) == (x2, y2):
        return False
    if (1 <= x1 <= 8) and (1 <= x2 <= 8) and (1 <= y1 <= 8) and (1 <= y2 <= 8) and \
            ((y1 == y2 and x1 != x2 and x1 in range(1, 9) and x2 in range(1, 9)) or\
             (x1 == x2 and y1 != y2 and y1 in range(1, 9) and y2 in range(1, 9))):
        return True
    else:
        return False

def b_allowed(cell_from,cell_to,white=False):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if (x1, y1) == (x2, y2):
        return False
    if (1 <= x1 <= 8) and (1 <= x2 <= 8) and (1 <= y1 <= 8) and (1 <= y2 <= 8) and \
            (abs(x1 - x2) == abs(y1 - y2)):
        return True
    else:
        return False

def n_allowed(cell_from,cell_to,white=False):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if (x1, y1) == (x2, y2):
        return False
    if (1 <= x1 <= 8) and (1 <= x2 <= 8) and (1 <= y1 <= 8) and (1 <= y2 <= 8) and \
            ((abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)):
        return True
    else:
        return False

def q_allowed(cell_from,cell_to,white=False):
    return b_allowed(cell_from, cell_to) or r_allowed(cell_from, cell_to)
