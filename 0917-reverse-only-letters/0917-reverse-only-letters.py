class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
            # Convert the string to a list for easy manipulation
        char_list = list(s)

    # Initialize pointers for the start and end of the string
        start, end = 0, len(char_list) - 1

        while start < end:
        # Move the pointers until both characters at the pointers are alphabetic
          while start < end and not char_list[start].isalpha():
              start += 1
          while start < end and not char_list[end].isalpha():
               end -= 1

        # Swap the characters at the pointers
          char_list[start], char_list[end] = char_list[end], char_list[start]

            # Move the pointers to the next positions
          start += 1
          end -= 1

        return ''.join(char_list)
        