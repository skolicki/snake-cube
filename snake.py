import copy

legs = [2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2]

def add(v1, v2):
    return [v1[i] + v2[i] for i in range(3)]

def mult(v, a):
    return [v[i] * a for i in range(3)]

def in_bounds(pos):
    return all(pos[i] in (0, 1, 2) for i in range(3))

def free(cube, pos):
    return not cube[pos[0]][pos[1]][pos[2]]

def fill(cube, pos):
    cube[pos[0]][pos[1]][pos[2]] = 1

def move(cube, pos, leg, moves, dir):
    for d in range(legs[leg]):
        pos2 = add(pos, mult(dir, d + 1))
        if not in_bounds(pos2) or not free(cube, pos2):
            return False
        fill(cube, pos2)
    new_pos = add(pos, mult(dir, legs[leg]))
    return check(cube, new_pos, leg + 1, moves + [new_pos])

def check(cube, pos, leg, moves):
    if leg == len(legs):
        print("hurray")
        print(moves)
        return True
    return any(move(copy.deepcopy(cube), pos, leg, moves, dir) for dir in ([-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]))

cube = [[[None, None, None], [None, None, None], [None, None, None]], [[None, None, None], [None, None, None], [None, None, None]], [[None, None, None], [None, None, None], [None, None, None]]]
fill(cube, [0, 0, 0])
check(cube, [0, 0, 0], 0, [])
