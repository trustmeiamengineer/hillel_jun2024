def correct_sentence(input_text):
    result = input_text
    if len(result) > 0:
        if result[-1] != '.':
            result += '.'

        # lowercase letters in English or Ukrainian
        if ord(result[0]) > 96 or ord(result[0]) > 1071:
            result = chr(ord(result[0]) - 32) + result[1:]

    return result


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
