# A simple recursive code to solve putting together https://en.wikipedia.org/wiki/Snake_cube
# Reformatted a few times aiming at brevity :)
# Hint: if you want to actually follow the result, it's physically easier going backwards

import copy

def move(cube, pos, dir, sgn, legs, path):
    if not legs:
        print(path)
        return True
    for d in range(legs[0]):
        pos[dir] += sgn
        if not pos[dir] in range(3) or cube[pos[0]][pos[1]][pos[2]]:
            return False
        cube[pos[0]][pos[1]][pos[2]] = 1
    return any(move(copy.deepcopy(cube), copy.copy(pos), dir, sgn, legs[1:], path + [pos]) for dir in range(3) for sgn in (-1, 1))

move(
    [[[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]],  # already fill at [0, 0, 0]
    [0, 0, 0],  # 4 legs of length 2 implies starting in a corner
    0, 1,  # first direction is arbitrary due to rotation/symmetry, as long as it's a correct move
    [2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2],  # hardcoded physical toy
    [])
