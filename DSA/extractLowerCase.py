import re

input_str = "H5ello!!!123"

new_str = ''.join([char for char in input_str if char.islower()])
int_str = ''.join([char for char in input_str if char.isdigit()])
upper_str = ''.join([char for char in input_str if char.isupper()])

extract_lower = ''.join([char for char in re.findall(r'[0-9]', input_str)])

print(new_str, int_str, upper_str, extract_lower)  # Output: "ello"