def minimumSum(num):

    # Sort the number with the minimum digits
    sorted_digits = [int(digit) for digit in sorted(str(num))]

    # making pair with lsb and msb
    digit_pairs = [(sorted_digits[i], sorted_digits[-(i + 1)]) for i in range(len(sorted_digits) // 2)]

    # subtotal total of the each pair
    integers = [int(str(pair[0]) + str(pair[1])) for pair in digit_pairs]

    # sum of the both subtotal
    result_sum = sum(integers)

    return result_sum


num = 4009
result = minimumSum(num)
print(result)