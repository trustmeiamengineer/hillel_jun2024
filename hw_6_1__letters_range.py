from string import ascii_letters


def get_consecutive_letters(orig_str):
    start_letter = ascii_letters.find(orig_str[0])
    end_letter = ascii_letters.find(orig_str[2])
    result = 'input contains non-English letter'

    if start_letter > -1 and end_letter > -1:
        result = ascii_letters[start_letter:end_letter + 1]

    return result


input_str = input('Enter two dash separated letters to display all letters in between of them:\n')

print(get_consecutive_letters(input_str))
