
def insert_after_index(my_list):
    new_list = my_list[:]
    # Find the index where we want to insert the new element
    insert_index = next((i for i, x in enumerate(my_list) if x == 500), None)
    # Check if we found the index we were looking for
    if insert_index is not None:
        # Insert the new element at the found index
        new_list.insert(insert_index + 1, [912, 170])
    return new_list
