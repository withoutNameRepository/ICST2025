 def return_binary_or_hexadecimal(tuple):
    a = tuple[10]
    b = tuple[28]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple:
            sum += i

    if sum % 2 == 1:
        return bin(sum).replace("0b", "")

    else:

        return hex(sum).replace("0x", "").lower()
