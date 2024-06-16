
empty_list = []
one_member_list = [5.5]
normal_list = ["Kharkiv", "Kherson", "Ternopil", "Donetsk", "Kropyvnytskyi"]


def split_list_in_two(orig_list):
    mid_index = len(orig_list) - len(orig_list) // 2
    return [orig_list[0:mid_index], orig_list[mid_index:]]


print(split_list_in_two(normal_list))
