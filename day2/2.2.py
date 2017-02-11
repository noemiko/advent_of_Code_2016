# --- Part Two ---
#
# You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:
#
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
# You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:
#
# You start at "5" and don't move at all (up and left are both edges), ending at 5.
# Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
# Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
# Finally, after five more moves, you end at 3.
# So, given the actual keypad layout, the code would be 5DB3.


import io


POLYGON = [[0, 0, 1, 0, 0],
          [0, 2, 3, 4, 0],
          [5, 6, 7, 8, 9],
          [0, 'A', 'B', 'C', 0],
          [0, 0, 'D', 0, 0]]

MAX_X = len(POLYGON)
MAX_Y = len(POLYGON[0])


def init():
    coordinates = {'x': 1, 'y': 1}
    with io.open('./input.txt', 'r') as f:
        for row_instructions in f:
            coordinates = get_last_move_coordinates(row_instructions, coordinates)

            print(POLYGON[coordinates['y']][coordinates['x']])


def get_last_move_coordinates(instructions, actual_coordinates):
    for letter in instructions:
        next_coordinates = get_new_coordinates(actual_coordinates, letter)

        if check_is_move_out_of_polygon(next_coordinates):
            continue
        else:
            actual_coordinates = next_coordinates.copy()
    return actual_coordinates


def get_new_coordinates(actual, letter):
    next_move_direction = get_move_on_polygon(letter)
    actual_coordinates = actual.copy()
    actual_coordinates['x'] += next_move_direction['x']
    actual_coordinates['y'] += next_move_direction['y']
    return actual_coordinates


def check_is_move_out_of_polygon(next_coordinates):
    if next_coordinates['x'] == -1 or next_coordinates['x'] == MAX_X:
        return True
    elif next_coordinates['y'] == -1 or next_coordinates['y'] == MAX_Y:
        return True
    elif (POLYGON[next_coordinates['y']], [next_coordinates['x']]) == 0:
        return True
    return False


def get_move_on_polygon(move):
    x, y = 0, 0
    if move == "U":
        y -= 1
    elif move == "D":
        y += 1
    elif move == "L":
        x -= 1
    elif move == "R":
        x += 1
    return {'x': x, 'y': y}

init()
