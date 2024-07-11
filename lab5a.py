#!/usr/bin/env python3
# Author ID: [swiafe]

def read_file_string(file_name):
    try:
        f = open(file_name, 'r')
        content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."
    except IOError:
        return f"Error: Could not read from file '{file_name}'."
    finally:
        if f:
            f.close()

def read_file_list(file_name):
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        lines = [line.strip() for line in lines]  
        return lines
    except FileNotFoundError:
        return [f"Error: File '{file_name}' not found."]
    except IOError:
        return [f"Error: Could not read from file '{file_name}'."]
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
