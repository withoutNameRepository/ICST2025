
def insert_before_character(s, char):
    return "".join([char + c if c == 'w' else c for c in s])
