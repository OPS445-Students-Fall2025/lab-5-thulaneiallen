#!/usr/bin/env python3
# Author ID: Thulanei Allen

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as f:
        contents = f.read()  # read all text, remove trailing newline
    return contents

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()  # splitlines() removes '\n' automatically
    return lines


def append_file_string(file_name, string_of_lines):
    """Append the given string to the end of file_name (create file if missing)."""
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Write each item from list_of_lines to file_name as its own line."""
    with open(file_name, 'w') as f:
        for item in list_of_lines:
            f.write(str(item) + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """
    Read all lines from file_name_read and write them to file_name_write
    with 1-based line numbers prefixed like 'N:<line>'.
    """
    with open(file_name_read, 'r') as src, open(file_name_write, 'w') as dst:
        for idx, line in enumerate(src, start=1):
            dst.write(f"{idx}:{line.rstrip()}\n")



if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))