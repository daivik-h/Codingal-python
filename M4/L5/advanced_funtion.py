def find_cube(n):
    return n*n*n
number_list = [1,4,8,21,9]

cube_numbers = list(map(find_cube, number_list))
print(cube_numbers)