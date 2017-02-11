# Now that you've helpfully marked up their design documents,
# it occurs to you that triangles are specified in groups of t
# hree vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
#
# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:
#
# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?


import io

TRIANGLES = [] #one row has lines lenght to check is traingle


def init():
    first_temporary_array = [] # temporary arrays to sort data
    second_temporary_array = []
    third_temporary_array = []

    with io.open('./input.txt', 'r') as f:
        for row in f:
            lines = [int(length) for length in row.split(' ') if length.strip() != '']

            first_temporary_array.append(lines[0])
            second_temporary_array.append(lines[1])
            third_temporary_array.append(lines[2])

            if len(first_temporary_array) == 3:
                #add data by columns
                TRIANGLES.append(first_temporary_array)
                TRIANGLES.append(second_temporary_array)
                TRIANGLES.append(third_temporary_array)

                #clear arrays for next data to sort

                first_temporary_array = []
                second_temporary_array = []
                third_temporary_array = []

        number_of_triangles = get_number_of_triangles()

        print('Number of triangles: {}'.format(number_of_triangles))


def get_number_of_triangles():
    number_of_triangles = 0
    for triangle in TRIANGLES:
        if is_triangle(triangle):
            number_of_triangles += 1
    return number_of_triangles


def is_triangle(line):
    if line[0] + line[1] <= line[2]:
        return False
    elif line[2] + line[0] <= line[1]:
        return False
    elif line[2] + line[1] <= line[0]:
        return False
    return True

init()