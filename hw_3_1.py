
first_value = input("Enter first operand: ")
operation = input("Enter operation: ")
second_value = input("Enter second operand: ")

first_operand = complex(first_value) if 'j' in (first_value) \
          else float(first_value) if '.' in (first_value) \
          else int(first_value)
second_operand = complex(second_value) if 'j' in (second_value) \
            else float(second_value) if '.' in (second_value) \
            else int(second_value)

if operation == '+':
    print(first_operand + second_operand)
elif operation == '-':
    print(first_operand - second_operand)
elif operation == '*':
    print(first_operand * second_operand)
else:
    if second_operand == 0+0j:
        print("Denominator must not be zero")
    else: print(first_operand / second_operand)
