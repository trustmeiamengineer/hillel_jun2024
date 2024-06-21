short_list = [4.9, 0]
minimum_list = [5, 22, 6]
normal_list = [-3, 11, 8.3, 0, 5.2, -3.5, 6, 0.3, 5, -2]


def create_three_item_list(orig_list):
    if len(orig_list) < 3:
        return orig_list
    else:
        result = [orig_list[0], orig_list[2], orig_list[-2]]
        return result


print(create_three_item_list(minimum_list))
