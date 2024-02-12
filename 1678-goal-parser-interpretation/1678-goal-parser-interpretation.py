import re 

class Solution:
    def interpret(self, command: str) -> str:
        # Replace empty parentheses with 'o' and remove parentheses with non-empty content
        modified_string = re.sub(r'\(\)', 'o', command)
        modified_string = re.sub(r'\(([^)]+)\)', r'\1', modified_string)

        return modified_string