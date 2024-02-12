class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Extract two characters at a time using list comprehension
        result = [s[i:i + k] for i in range(0, len(s), k)]

        temp = []
    
        for index, value in enumerate(result):
            if index % 2 == 0:
                reversed_value = value[::-1]
                temp.append(reversed_value)
            else: temp.append(value)

        merged_string = ''.join(temp)

        return merged_string