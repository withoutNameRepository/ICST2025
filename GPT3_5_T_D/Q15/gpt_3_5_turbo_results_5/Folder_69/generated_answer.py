
def sum_odd_ints_inclusive(lst):
    odd_ints = [x for x in lst[32:36] if x % 2 != 0]
    return sum(odd_ints) if odd_ints else 0
