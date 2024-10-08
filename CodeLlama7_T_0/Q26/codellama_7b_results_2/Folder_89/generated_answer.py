
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers
    for i in my_list:
        # Check if the current integer is between 15 and 57, both inclusive
        if 15 <= i <= 57:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
