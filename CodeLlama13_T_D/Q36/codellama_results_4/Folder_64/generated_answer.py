
def filter_chars(string):
    result = ""
    for i in range(1, 7):
        char = string[i]
        if char > "3" and char < "^":
            result += char
        else:
            result += string[i]
    return result
