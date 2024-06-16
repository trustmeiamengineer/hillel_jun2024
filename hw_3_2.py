empty_list = []
one_elem_list = [1]
int_list = [12, 3, 4, 10]
string_list = ["Kyiv", "Uzhhorod", "Dnipro", "Odesa", "Kharkiv"]


def put_last_elem_as_first(user_list):
    if len(user_list) > 1:
        user_list.insert(0, user_list.pop(len(user_list) - 1))
    return user_list


print(string_list)
print(put_last_elem_as_first(string_list))
