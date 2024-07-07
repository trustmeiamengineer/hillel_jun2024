def popular_words(text, words):

    res_dict = {word:0 for word in words}

    from string import punctuation
    for char in punctuation:
        text.replace(char, '')

    spt_text = text.lower().split()

    for w in spt_text:
        if w in words:
            res_dict[w] += 1

    return res_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
