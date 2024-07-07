def find_unique_value(orig_list):
    chk_dict = dict()

    for i in orig_list:
        if not chk_dict.get(i):
            chk_dict[i] = 1

        else:
            chk_dict[i] += 1

    uniq_val = None

    for k in chk_dict:
        if chk_dict[k] == 1:
            uniq_val = k
            break

    return uniq_val


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([5, 5, 5, 2, 2, 2]) is None, 'Test4'
print("ОК")

