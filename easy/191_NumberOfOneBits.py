# Level: Easy

# Problem:
#   Write a function that takes an unsigned integer and returns the number of
#   '1' bits it has (also known as the hamming weight)

# Note:
#   1. In some languages, such as java, there is no unsigned integer type. In
#      this case, the input will be given as a signed integer type. It should
#      not affect your implementation, as the integer's internal binary
#      representation is the same, whether it is signed or unsigned.
#   2. In Java, the compiler represents the signed integers using 2's complement
#      notation. Therefore, in Example 3, the input represents the signed integer
#      -3.

# Sample Input
n = 0o0000000000000000000000001011  # output 3


# Bit Shift and Modulus - O(32), O(C)
def calculate_number_one_bits(bits):
    num_one_bits = 0

    while bits > 0:
        num_one_bits += bits % 2
        bits = bits >> 1

    return num_one_bits


result = calculate_number_one_bits(n)
print(f"Number of one bits: {result}")
