import keyword
import string

input_value = input('Enter variable name to check:\n')


def check_variable_name(orig_name):
    char_set = list(string.punctuation)
    char_set.remove('_')
    not_acceptable_chars = tuple(char_set)
    reserved_keywords = tuple(keyword.kwlist)

    is_name_acceptable = True
    check_is_over = False

    while not check_is_over:
        # space or being a reserved word
        if orig_name.find(' ') > -1 or orig_name in reserved_keywords:
            is_name_acceptable = False
            break

        # start with digit
        if 47 < ord(orig_name[0]) < 58:
            is_name_acceptable = False
            break

        # two underscores are only at the beginning and there are other chars except them
        if orig_name.rfind('__') > -1 and orig_name != '__':
            is_name_acceptable = False
            break

        # capital letters or punctuation
        for char in orig_name:
            if char in not_acceptable_chars or 64 < ord(char) < 91:
                is_name_acceptable = False
                break

        check_is_over = True

    return is_name_acceptable
