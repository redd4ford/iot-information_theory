def inverse_binary(combination):
    inverse = ''
    for digit in combination:
        inverse += '0' if digit == '1' else '1'
    return inverse


def xor(x, y):
    x = False if x == '0' else True
    y = False if y == '0' else True
    return False if x == y else x or y


def trim(combination_as_list):
    trimmed = ''
    for bit in combination_as_list:
        trimmed += str(bit)
    return trimmed
