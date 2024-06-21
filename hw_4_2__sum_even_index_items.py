empty_list = []
one_item_list = [6]
normal_list = [0, 1, 7, 2, 4, 8]


def sum_even_index_items(orig_list):
    result = 0
    if len(orig_list) > 0:
        for i in range(len(orig_list)):
            if i % 2 == 0:
                result += orig_list[i]
        result *= orig_list[-1]
    return result


print(sum_even_index_items(normal_list))
