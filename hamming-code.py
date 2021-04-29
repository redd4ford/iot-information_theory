from utils import trim


def hamming_encode(number):
    parity_bits = get_parity_bits_positions(number)

    hamming_len = len(number) + len(parity_bits)
    hamming_list = ['x' for _ in range(hamming_len)]
    index = 0
    for i in range(hamming_len):
        # leave parity bits' positions as 'x'; fill all the remaining places
        # with information bits
        if i not in parity_bits:
            hamming_list[i] = number[index]
            index += 1

    index = 0
    for parity_pos in parity_bits:
        hamming_list[parity_pos] = calculate_parity_bit(hamming_list, parity_bits, index)
        index += 1

    return hamming_list


def get_parity_bits_positions(number):
    parity_bits = []
    index = 0
    parity_pos = 2 ** index
    while parity_pos <= len(number):
        parity_bits.append(parity_pos - 1)
        index += 1
        parity_pos = 2 ** index
    return parity_bits


def calculate_parity_bit(number, parity_bits, parity_bit_pos):
    controlled_bits, _ = get_controlled_bits(number, parity_bits, parity_bit_pos)
    # counting ones
    ones_counter = 0
    for digit in controlled_bits:
        ones_counter += digit if digit == 1 else 0
    # if the number of ones is odd, set the parity bit to 1
    return 0 if ones_counter % 2 == 0 else 1


def get_controlled_bits(number, parity_bits, parity_bit_pos):
    # look into positions controlled by this parity bit: for parity bit #N,
    # it will be N bits every N bits starting with position N
    # (e.g. for 2 it will be 2, 3; 6, 7; 10, 11; 14, 15; ...)
    bits = []
    indices = []
    for z in range(2 ** parity_bit_pos):
        for bit in range(z + 2 ** parity_bit_pos - 1, len(number), 2 ** (parity_bit_pos + 1)):
            if bit not in parity_bits:
                # add the bit controlled by this parity bit
                bits.append(number[bit])
                indices.append(bit)
    return bits, indices


def hamming_decode(combination):
    parity_bits = get_parity_bits_positions(combination)
    decoded = [0 for _ in range(len(combination) - len(parity_bits))]

    index = 0
    for i in range(len(combination)):
        if i not in parity_bits:
            decoded[index] = combination[i]
            index += 1

    return decoded


def is_valid(combination):
    parity_bits = get_parity_bits_positions(combination)
    corrupted_bits = []

    index = 0
    for parity_bit in parity_bits:
        # restore the parity bits for this combination
        if calculate_parity_bit(combination, parity_bits, index) != combination[parity_bit]:
            # if the bit is not correct, set the flag for it
            corrupted_bits.append(parity_bit)
        index += 1

    return corrupted_bits if len(corrupted_bits) > 0 else True


def fix_corrupted(number, error_bits):
    # get the index of a corrupted info bit
    corrupted_index = 1
    for error in error_bits:
        corrupted_index += error

    # invert the corrupted bit
    number[corrupted_index] = 1 if number[corrupted_index] == 0 else 0
    if is_valid(number):
        print(f'fixed code               {trim(number)}')


if __name__ == '__main__':

    decimal_number = int(input('initial (decimal)        '))
    binary_number = bin(decimal_number)
    print(f'initial (binary)         {binary_number}')

    number_split = [int(digit) for digit in str(bin(decimal_number)[2:])]
    hamming_number = hamming_encode(number_split)
    print(f'encoded (hamming)        {trim(hamming_number)}')

    corrupted_number = hamming_number
    if isinstance(is_valid(hamming_number), bool):
        print('no error found')
        result = hamming_decode(hamming_number)
        print(f'decoded (binary)         {trim(result)}')
        print(f'decoded (decimal)        {int(trim(result), base=2)}')

        # plant a corrupted bit
        corruption_pos = 4
        corrupted_number[corruption_pos] = 1 if corrupted_number[corruption_pos] == 0 else 0

        print('\n')
        print(f'encoded (corrupted)      {trim(corrupted_number)}')

    print(f'decoded (binary)         {trim(hamming_decode(corrupted_number))}')
    print(f'decoded (decimal)        {int(trim(hamming_decode(corrupted_number)), base=2)}')
    errors = is_valid(corrupted_number)
    print(f'found an error, triggered parity bits={errors}')
    print(f'fixing the error(s)...')
    fix_corrupted(corrupted_number, errors)
