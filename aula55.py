from contextlib import contextmanager

# Defines a context manager that automatically opens and closes the file, handling errors.
@contextmanager
def my_open(file_path, mode):
    try:
        print('Opening file')
        file = open(file_path, mode, encoding='utf8')  # Opens the file
        yield file  # Returns the file to be used in the 'with' block
    except Exception as e:
        print('An error occurred', e)  # Catches and prints errors
    finally:
        print('Closing file')
        file.close()  # Ensures the file is closed

# Uses the context manager to open and manipulate the file
with my_open('aula150.txt', 'w') as file:
    file.write('Line 1\n')  # Writes the first line
    file.write('Line 2\n', 123)  # Error: 'write' accepts only 1 argument
    file.write('Line 3\n')  # Writes the third line
    print('WITH', file)  # Prints the file
