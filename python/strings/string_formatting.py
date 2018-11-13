"""Problem: https://www.hackerrank.com/challenges/python-string-formatting/problem"""

def print_formatted(number):
    # Length of binary digits of last number to match spacing to
    width = len(str(format(number, 'b'))) + 1
    
    for i in range(1, number + 1):
        # Decimal values
        print(' ' * (width - len(str(i)) - 1) + str(i),end='')
        # Octal values
        octal = format(i, 'o')
        num_spaces = width - len(str(octal))
        print(' ' * num_spaces + str(octal),end='')
        # Hexadecimal values
        hexadecimal = format(i, 'x').upper()
        num_spaces = width - len(str(hexadecimal))
        print(' ' * num_spaces + str(hexadecimal),end='')
        # Binary values
        binary = format(i, 'b')
        num_spaces = width - len(str(binary))
        print(' ' * num_spaces + str(binary))
        