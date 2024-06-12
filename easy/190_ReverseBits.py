# Level: Easy

# Problem:
#   Reverse bits of a given 32 bits unsigned integer

# Sample Input
n = 0o1000


def reverse_bits(bits):
    result = 0

    for i in range(32):
        bit = (bits >> i) & 1
        result = result | (bit << (31 - i))

    return result


result = reverse_bits(n)
print(f"Reverse bits: {result}")
