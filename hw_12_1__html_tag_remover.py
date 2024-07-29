import codecs
src = 'draft.html'


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as src_file:
        html_file = src_file.read()

    bgn, end = 0, 0
    tags_values = []
    try:
        while True:
            # index of char next after closing angle bracket - considered as beginning of tag value
            bgn = html_file[end:].index('>') + end + 1
            # index of opening angle bracket - considered as end of tag value
            end = html_file[bgn:].index('<') + bgn
            # ignore non-informative substrings, consisting only of spaces, LF, TAB etc.
            if html_file[bgn:end].strip():
                tags_values.append(html_file[bgn:end] + '\n')

    except ValueError as e:
        pass

    with codecs.open(result_file, 'w', 'utf-8') as dst_file:
        dst_file.writelines(tags_values)

    return None


delete_html_tags(src, result_file='cleaned.txt')
