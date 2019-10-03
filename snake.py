# A simple recursive code to solve putting together https://en.wikipedia.org/wiki/Snake_cube
# Reformatted a bit aiming at brevity :)
# Hint: if you want to actually follow the result, it's physically easier going backwards

import copy

def move(cube, pos,  dir, legs, path):
    if not legs:
        print(path)  # short-curcuiting any will execute this once
        return True
    for d in range(legs[0]):
        pos = [pos[i] + dir[i] for i in range(3)]
        if not all(pos[i] in range(3) for i in range(3)) or cube[pos[0]][pos[1]][pos[2]]:
            return False
        cube[pos[0]][pos[1]][pos[2]] = 1
    return any(move(copy.deepcopy(cube), pos, legs[1:], path + [pos], dir) for dir in ([-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]))

move(
    [[[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]],  # already fill at [0, 0, 0]
    [0, 0, 0],  # 4 legs of length 2 implies starting in a corner
    [1, 0, 0],  # first direction is arbitrary due to rotation/symmetry
    [2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2],  # hardcoded physical toy
    [])
