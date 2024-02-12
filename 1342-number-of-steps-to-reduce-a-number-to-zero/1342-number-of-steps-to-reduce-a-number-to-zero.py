class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        if num == 0:
            return 0

        else:
            while True:
                if num % 2 == 0:
                    num = num // 2
                    count = count + 1

                elif num % 2 != 0:
                    num = num - 1
                    count = count + 1
                if num == 0:
                    break


        return (count)
