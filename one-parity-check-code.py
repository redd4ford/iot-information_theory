def count_ones(number):
    return number.count('1')


def add_parity_bit(number):
    return number + '0' if count_ones(number) % 2 == 0 else number + '1'


# error check: the number of ones without the parity bit should be odd if
# it is 1, and even if it is 0
def is_valid(combination):
    return count_ones(combination[-1]) % 2 == count_ones(combination[:-1]) % 2


if __name__ == "__main__":

    decimal_number = int(input('initial (decimal)           '))
    binary_number = bin(decimal_number)
    print(f'initial (binary)            {binary_number}')

    with_parity_bit = add_parity_bit(binary_number)
    print(f'encoded (with parity bit)   {with_parity_bit}')

    if is_valid(with_parity_bit):
        print(f'no error found, parity bit can be removed')
        parity_to_binary = with_parity_bit[:-1]
        print(f'decoded (binary)            {parity_to_binary}')

        result = int(parity_to_binary, base=2)
        print(f'decoded (decimal)           {result}')
    else:
        print('found an error')
