
def if_contains_anagrams(string_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate through each string in the list
    for string1 in string_list:

        # Iterate through each string after the first one
        for string2 in string_list[string_list.index(string1) + 1:]:

            # Check if the strings are anagrams
            if sorted(string1.lower()) == sorted(string2.lower()):

                # Increment the anagram count
                anagram_count += 1

    # Return True if there are at least 136 pairs of anagrams in the list, and False otherwise
    return anagram_count >= 136
