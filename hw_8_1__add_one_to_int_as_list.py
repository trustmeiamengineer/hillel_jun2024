def add_one(orig_list):
    if len(orig_list) == 0:
        return orig_list
    else:
        inc_value = 1
        for i in range(len(orig_list)):
            inc_value += orig_list[i] * 10 ** (len(orig_list) - 1 - i)

        result = [x for x in str(inc_value)]

        if result[0] == '-':
            result[1] = '-' + result[1]
            result.remove('-')

        return [int(x) for x in result]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

# check for negative number
assert add_one([-1, 0, 0]) == [-9, 9], 'Test5'

# check for empty list
assert add_one([]) == [], 'Test6'
print('OK')
