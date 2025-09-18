from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(f"contents: \n{contents}")

lines = contents.splitlines()
print(f"lines: {lines}")
for line in lines:
    print(line)

# file_1 = open('pi_digits.txt', 'r')
# file_1.close()

with open('pi_digits.txt', 'r') as file_1:
    contents = file_1.read()
    print(f"file_1.read(): {contents}")