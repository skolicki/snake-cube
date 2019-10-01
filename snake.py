# A simple recursive code to solve putting together https://en.wikipedia.org/wiki/Snake_cube
# Reformatted a bit aiming at brevity :)
# Hint: if you want to actually follow the result, it's physically easier going backwards

import copy

def move(cube, pos, legs, path, dir):
    for d in range(legs[0]):
        pos = [pos[i] + dir[i] for i in range(3)]
        if not all(pos[i] in (0, 1, 2) for i in range(3)) or cube[pos[0]][pos[1]][pos[2]]:
            return False
        cube[pos[0]][pos[1]][pos[2]] = 1
    return check(cube, pos, legs[1:], path + [pos])

def check(cube, pos, leg, moves):
    if leg == len(legs):
        print("hurray")
        print(moves)
        return True
    return any(move(copy.deepcopy(cube), pos, leg, moves, dir) for dir in ([-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]))

check(
    [[[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]],  # already fill at [0, 0, 0]
    [0, 0, 0],  # 4 legs of length 2 implies starting in a corner
    [2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2],  # hardcoded physical toy
    [])
