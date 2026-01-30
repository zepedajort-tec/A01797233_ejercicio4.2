"""
Convert decimal numbers to binary and hexadecimal representations.
"""

import sys
import time
from .utils import print_elapsed


def to_binary(number):
    """Convert an integer to binary."""
    if number >= 0:
        return bin(number)[2:]
    return format(number & 0xFFFFFFFF, "b")


def to_hex(number):
    """Convert an integer to hexadecimal."""
    if number >= 0:
        return hex(number)[2:].upper()
    return format(number & 0xFFFFFFFF, "X")


def main():
    """Main program execution."""
    start_time = time.time()
    files = sys.argv[1:]

    if not files:
        print("Usage: python convert_numbers.py file1.txt file2.txt")
        sys.exit(1)

    output_file = "testing-files/P2/A4.2.P2.Results-output.txt"
    with open(output_file, "w", encoding="utf-8") as out:
        for filename in files:
            header = f"\nITEM\t{filename[:-4]}\tBIN\tHEX"
            out.write(header + "\n")
            print(header)

            with open(filename, "r", encoding="utf-8") as file:
                item = 1
                for line in file:
                    value = line.strip()
                    try:
                        number = int(value)
                        binary = to_binary(number)
                        hexa = to_hex(number)
                    except ValueError:
                        binary = "#VALUE!"
                        hexa = "#VALUE!"

                    row = f"{item}\t{value}\t{binary}\t{hexa}"
                    out.write(row + "\n")
                    print(row)
                    item += 1

        print_elapsed(start_time, out)


if __name__ == "__main__":
    main()
