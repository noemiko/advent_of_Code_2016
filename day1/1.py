# --- Day 1: No Time for a Taxicab ---
#
# Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars.
# Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas,
# Santa needs you to retrieve all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar;
# the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
# unfortunately, is as close as you can get - the instructions on the Easter Bunny
# Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.
#
# The Document indicates that you should start at the given coordinates (where you just landed) and face North.
# Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees,
# then walk forward the given number of blocks, ending at a new intersection.
#
# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the
# destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?
#
# For example:
#
# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?

import io


def init():
    with io.open('./input.txt', 'r') as f:
        instructions = [direction.strip() for direction in f.readline().split(', ') if len(direction.strip()) > 0]
        # started coordinates
        x, y = 0, 0
        # the direction in which you are returned (North or West or South or East)
        face_direction = 'N'
        for instruction in instructions:
            step_direction = instruction[0] #left or right
            number_of_steps = int(instruction[1:])
            face_direction = get_rotation_direction(face_direction, step_direction)
            move = get_move_coordinates_change(face_direction, number_of_steps)
            x += move['x']
            y += move['y']
        print('Distance is : {}'.format(abs(x)+abs(y)))


def get_move_coordinates_change(face_direction, steps):
    if face_direction == 'N':
        return {'x': 0, 'y': steps}
    elif face_direction == 'E':
        return {'x': steps, 'y': 0}
    elif face_direction == 'S':
        return {'x': 0, 'y': -steps}
    elif face_direction == 'W':
        return {'x': -steps, 'y': 0}


def get_rotation_direction(face_direction, direction):
    if face_direction == 'N':
        if direction == 'L':
            return 'W'
        elif direction == 'R':
            return 'E'
    elif face_direction == 'E':
        if direction == 'L':
            return 'N'
        elif direction == 'R':
            return 'S'
    elif face_direction == 'W':
        if direction == 'L':
            return 'S'
        elif direction == 'R':
            return 'N'
    elif face_direction == 'S':
        if direction == 'L':
            return 'E'
        elif direction == 'R':
            return 'W'

init()