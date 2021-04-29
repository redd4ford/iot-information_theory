# generate Gray code by performing XOR between the number and
# the right-shifted number
def gray_encode(number):
    return bin(
        int(number, base=2) ^ (int(number, base=2) >> 1)
    )


# decode Gray code by performing XOR of right-shifted combinations
def gray_decode(number):
    number = int(number, base=2)
    shift_count = number

    while shift_count:
        shift_count >>= 1
        number ^= shift_count
    return bin(number)


if __name__ == "__main__":

    decimal_number = int((input('initial (decimal)     ')))

    binary_number = bin(decimal_number)
    print(f'initial (binary)      {binary_number}')

    gray_number = gray_encode(binary_number)
    print(f'encoded (gray)        {gray_number}')

    gray_number_to_binary = gray_decode(gray_number)
    print(f'decoded (binary)      {gray_number_to_binary}')

    result = int(gray_number_to_binary, base=2)
    print(f'decoded (decimal)     {result}')
