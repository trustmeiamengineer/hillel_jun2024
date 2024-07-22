from inspect import isgenerator


def cubed_number(n):
    return n**3


def generate_cube_numbers(end):
    root_number = 2
    result = cubed_number(2)
    while result <= end:
        yield result
        root_number += 1
        result = cubed_number(root_number)


gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('OK')
