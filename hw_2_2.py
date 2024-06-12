print('Enter 5-digit integer number: ')
user_input = input()
original_number = int(user_input)

numbers = original_number // 10**4
tens = (original_number - numbers * 10**4) // 10**3
hundreds = (original_number - numbers * 10**4 - tens * 10**3) // 10**2
thousands = (original_number - numbers * 10**4 - tens * 10**3 - hundreds * 10**2) // 10
ten_thousands = original_number - numbers * 10**4 - tens * 10**3 - hundreds * 10**2 - thousands * 10

inverted_number = ten_thousands * 10**4 + \
                  thousands * 10**3 + \
                  hundreds * 10**2 + \
                  tens * 10 + \
                  numbers

print('Inverted number is', inverted_number)
