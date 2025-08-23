from pathlib import Path

path = Path("/Users/chenlong/workspace/internation_class_cs/python/wangweizhu/chapter10/pi_digits.txt")
contents = path.read_text().rstrip()
lines = contents.splitlines()
print("contents:", contents)
print("lines:", lines)

pi_string = ''
for line in lines:
    pi_string += line.strip()
print("pi_string: ", pi_string)
print("len(pi_string): ", len(pi_string))

# write file
path = Path('/Users/chenlong/workspace/internation_class_cs/python/wangweizhu/chapter10/programming.txt')
path.write_text('I love programming.')

try:
    path = Path('alice.txt')
except FileNotFoundError:
    contents = path.read_text(encoding='utf-8')
# else:
#     print("contine")
print("contine")