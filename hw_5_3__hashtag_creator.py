import string

input_string = input('Enter the phrase to make a hashtag: ')


def make_hashtag(orig_string, tag_length=140):
    char_set = list(string.punctuation)
    char_set.remove('_')
    not_acceptable_chars = tuple(char_set)
    resulting_hashtag = '#'

    words_list = orig_string.split()
    for orig_word in words_list:
        spelled_word = list(orig_word)
        fined_word = []
        for orig_char in spelled_word:
            if orig_char not in not_acceptable_chars:
                fined_word.append(orig_char)
        else:
            fined_word_str = ''.join(fined_word)
            resulting_hashtag += fined_word_str.capitalize()
    return resulting_hashtag[:tag_length]


print(make_hashtag(input_string, 20))
