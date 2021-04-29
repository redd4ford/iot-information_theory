from utils import xor, inverse_binary


# rewrite each bit of the combination: 0 -> 01; 1 -> 10
def correlation_encode(combination):
    encoded = ''
    for digit in combination:
        encoded += digit + inverse_binary(digit)
    return encoded


def correlation_decode(combination):
    # divide the code into pairs
    pairs = []
    for i in range(0, len(combination) - 1, 2):
        pairs.append([combination[i], combination[i + 1]])

    if is_valid(pairs):
        print('no error found, verification part can be removed')
        decoded = ""
        for pair in pairs:
            decoded += pair[0]
        return decoded
    else:
        print('found an error. the sum is not null')
        return False


# error check: for each pair, the sum of information and verification bits
# should be 1 (bits should not be equal)
def is_valid(pairs):
    pairs_sums = [xor(pairs[i][0], pairs[i][1]) for i in range(0, len(pairs))]
    return False not in pairs_sums


if __name__ == '__main__':
    decimal_number = int(input('initial (decimal)     '))
    binary_number = bin(decimal_number)
    print(f'initial (binary)      {binary_number}')

    correlated_number = correlation_encode(binary_number[2:])
    print(f'encoded (correlation) {correlated_number}')

    result = correlation_decode(correlated_number)
    if not isinstance(result, bool):
        print(f'decoded (binary)      {result}')
        print(f'decoded (decimal)     {int(result, 2)}')
