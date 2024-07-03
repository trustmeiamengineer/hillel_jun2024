def second_index(text, some_str):
    result = None
    split_list = text.split(some_str)

    if len(split_list) > 2:
        result = len(split_list[0]) + len(split_list[1]) + len(some_str)

    return result


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
