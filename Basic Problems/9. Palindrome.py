class Solution:
    def isPalindrome(self, x: int) -> bool:
        convert_str = str(x)
        reverse_str = str(convert_str)[::-1]

        # reversed_num = int(reversed_str)
        if (convert_str == reverse_str):
            print("true")
            return True
        else:
            print("false")
            return False

x = int(input("x: "))

solution_obj = Solution()
solution_obj.isPalindrome(x)
