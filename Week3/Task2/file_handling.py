# File Handling - file_handling.py

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            return content
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def write_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def count_words_in_file(file_path):
    try:
        content = read_file(file_path)
        if content:
            word_count = len(content.split())
            print(f"The file contains {word_count} words.")
    except Exception as e:
        print(f"An error occurred while counting words in the file: {e}")

# Example usage:
try:
    read_file('data.txt')
    write_to_file('output.txt', "This is user input data.")
    count_words_in_file('data.txt')
except Exception as e:
    print(f"An error occurred: {e}")
