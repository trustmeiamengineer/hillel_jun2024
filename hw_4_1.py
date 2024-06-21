empty_list = []
small_list = [9]
normal_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


def list_move_zeros_to_end(orig_list):
    zero_value = [0]
    zeros_count = 0
    non_zero_values = []
    for i in range(len(orig_list)):
        if orig_list[i] != 0:
            non_zero_values.append(orig_list[i])
        else: zeros_count += 1
    non_zero_values.extend(zero_value * zeros_count)
    return non_zero_values


print(list_move_zeros_to_end(normal_list))
