import argparse

parser = argparse.ArgumentParser(description="Greet a user")

parser.add_argument("--name", help="The name of the user")
parser.add_argument("--age", type=int, help="The age of the user")

args = parser.parse_args()
print(f"Hello, {args.name}! You are {args.age} years old.")