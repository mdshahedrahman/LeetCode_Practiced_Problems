class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1

        else:
            first_number = 0
            second_number = 1
            pre_result = 0

            for i in range(n - 1):
                pre_result = first_number + second_number
                first_number = second_number
                second_number = pre_result
        return pre_result
