
def return_nth_smallest_ascii(string):
    n = 13
    char_list = []
    
    for i in range(0, 19):
        if string[i] not in char_list:
            char_list.append(string[i])
            
    return sorted(char_list)[n-1]
