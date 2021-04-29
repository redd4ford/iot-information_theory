from utils import xor, inverse_binary


def inverse_encode(combination):
    # if the number of ones is even, verification part is the same as the info part
    if combination.count('1') % 2 == 0:
        combination *= 2
    # if the number of ones is odd, verification part is the inverted info part
    else:
        combination += inverse_binary(combination)
    return combination


def inverse_decode(combination):
    # split the combination in half
    info_part = combination[0:len(combination) // 2]
    verification_part = combination[len(combination) // 2:]

    checked = ''
    if info_part.count('1') % 2 == 0:
        # if the number of ones is even, check whether the verification and
        # info parts are equal
        if info_part == verification_part:
            checked = verification_part
        else:
            print('verification part is not the same as info part')
            return False
    else:
        # if the number of ones is odd, check whether the inverted
        # verification and info parts are equal
        checked += inverse_binary(verification_part)
        if info_part != checked:
            print('inverted verification part is not the same as the info part')
            return False

    if is_valid(info_part, checked):
        print('no error found, verification part can be removed')
        return info_part
    else:
        print('found an error. the sum is not null')
        return False


# error check: the sum of both halves should be 0
def is_valid(info_part, check_part):
    sum_result = [xor(info_part[i], check_part[i]) for i in range(0, len(info_part))]
    return 1 not in sum_result


if __name__ == '__main__':

    decimal_number = int(input('initial (decimal)  '))
    binary_number = bin(decimal_number)
    print(f'initial (binary)   {binary_number}')

    inverse_number = inverse_encode(binary_number[2:])
    print(f'encoded (inverse)  {inverse_number}')

    inverse_to_binary = inverse_decode(inverse_number)
    if not isinstance(inverse_to_binary, bool):
        print(f'decoded (binary)   {inverse_to_binary}')
        result = int(inverse_to_binary, base=2)
        print(f'decoded (decimal)  {result}')
