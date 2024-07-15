def first_word(text):
    start_index, end_index = None, None
    for i in range(len(text)):
        if text[i].isalpha() and start_index is None:
            start_index = i

        if not text[i].isalpha() and text[i] != "'" and start_index is not None:
            end_index = i
            break

    return text[start_index:end_index]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
