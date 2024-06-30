user_input = input("Enter a non-negative integer to get 1-digit product of it`s digits:\n")


def number_digits_product(orig_value):
    result = "Incorrect value: should be non-negative integer"

    if orig_value.isdigit():
        mid_result = orig_value

        while len(mid_result) > 1:
            result = 1
            for digit in mid_result:
                result *= int(digit)
            mid_result = str(result)

    return result


print(number_digits_product(user_input))
