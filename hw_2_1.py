print('Enter 4-digit number: ')
user_input = input()
original_number = int(user_input)

thousands = original_number // 1000
hundreds = (original_number - thousands * 1000) // 100
tens = (original_number - thousands * 1000 - hundreds * 100) // 10
numbers = original_number - thousands * 1000 - hundreds * 100 - tens * 10

print(thousands, hundreds, tens, numbers, sep='\n')
