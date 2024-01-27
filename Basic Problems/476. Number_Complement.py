def invert_binary(nums):
    binary_representation = bin(nums)[2:]
    inverted_string = ''.join(['1' if bit == '0' else '0'
                               for bit in binary_representation])
    decimal_number = int(inverted_string, 2)
    return decimal_number

# Example usage:

nums = 5
inverted_binary = invert_binary(nums)


print(inverted_binary)
