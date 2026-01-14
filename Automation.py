import os

# Example: Count words in a text file
file_name = "sample.txt"

if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        word_count = len(text.split())
    print(f"The file '{file_name}' has {word_count} words.")
else:
    print(f"The file '{file_name}' does not exist.")
