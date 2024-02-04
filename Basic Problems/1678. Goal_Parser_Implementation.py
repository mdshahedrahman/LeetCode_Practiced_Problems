import re

command = "(al)G(al)()()G"

# Replace empty parentheses with 'o' and remove parentheses with non-empty content
modified_string = re.sub(r'\(\)', 'o', command)
modified_string = re.sub(r'\(([^)]+)\)', r'\1', modified_string)

print("Original string:", command)
print("Modified string:", modified_string)


