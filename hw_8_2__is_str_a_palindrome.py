def is_palindrome(orig_str):
    if orig_str == '':
        return False

    from string import punctuation as chars_to_filter_out

    chars_to_filter_out += ' '
    is_pal = True

    cmp_tpl = tuple(filter(lambda x: x not in chars_to_filter_out, orig_str))

    for i in range(len(cmp_tpl) // 2):
        if cmp_tpl[i].lower() != cmp_tpl[-i - 1].lower():
            is_pal = False
            break

    return is_pal


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
