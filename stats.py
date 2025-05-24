def num_words(txt):
    return len(txt.split())

def character_count(text):
    lib = {}
    for s in text.lower():
        if s in list(lib.keys()):
            lib[s] += 1
        else:
            lib[s] = 1
    return lib


def make_report(lib):
    chars_list = []
    for character, count in dict(sorted(lib.items(), key=lambda x:x[1], reverse=True)).items():
        chars_list.append({'char' : character, 'num' : count})

    return chars_list