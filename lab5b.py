#!/usr/bin/env python3
# Author ID: [swiafe]

def read_file_string(file_name):
    try:
        f = open(file_name, 'r')
        read_data = f.read()
        f.close()
        return read_data
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."
    except IOError:
        return f"Error: Could not read from file '{file_name}'."

def read_file_list(file_name):
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        f.close()
        lines = [line.strip() for line in lines] 
        return lines
    except FileNotFoundError:
        return [f"Error: File '{file_name}' not found."]
    except IOError:
        return [f"Error: Could not read from file '{file_name}'."]

def append_file_string(file_name, string_of_lines):
    try:
        f = open(file_name, 'a')
        f.write(string_of_lines)
        f.close()
    except IOError:
        print(f"Error: Could not append to file '{file_name}'.")

def write_file_list(file_name, list_of_lines):
    try:
        f = open(file_name, 'w')
        for line in list_of_lines:
            f.write(line + '\n')
        f.close()
    except IOError:
        print(f"Error: Could not write to file '{file_name}'.")

def copy_file_add_line_numbers(file_name_read, file_name_write):
    try:
        f_read = open(file_name_read, 'r')
        f_write = open(file_name_write, 'w')
        lines = f_read.readlines()
        for i, line in enumerate(lines, start=1):
            f_write.write(f"{i}:{line}")
        f_read.close()
        f_write.close()
    except FileNotFoundError:
        print(f"Error: File '{file_name_read}' not found.")
    except IOError:
        print(f"Error: Could not write to file '{file_name_write}'.")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    # Perform the following operations
    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
