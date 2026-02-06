"""
Compute descriptive statistics from numeric data files.
"""

import sys
import time
from .utils import print_elapsed

def read_numbers(filename):
    """Read numeric values from a file, ignoring invalid entries."""
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Invalid value ignored in {filename}: {line.strip()}")
    return numbers


def mean(data):
    """Calculate the arithmetic mean."""
    return sum(data) / len(data)


def median(data):
    """Calculate the median value."""
    sorted_data = sorted(data)
    size = len(sorted_data)
    mid = size // 2
    if size % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def mode(data):
    """Calculate the mode value."""
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    max_count = max(frequency.values())
    if max_count == 1:
        return "#N/A"
    for key, count in frequency.items():
        if count == max_count:
            return key
    return "#N/A"


def variance(data, avg):
    """Calculate the variance."""
    return sum((x - avg) ** 2 for x in data) / len(data)


def standard_deviation(var):
    """Calculate the standard deviation."""
    return var ** 0.5


def main():
    """Main program execution."""
    start_time = time.time()
    files = sys.argv[1:]

    if not files:
        print("Usage: python compute_statistics.py file1.txt file2.txt")
        sys.exit(1)

    results = {
        "COUNT": [],
        "MEAN": [],
        "MEDIAN": [],
        "MODE": [],
        "SD": [],
        "VARIANCE": []
    }

    for filename in files:
        data = read_numbers(filename)
        avg = mean(data)
        var = variance(data, avg)

        results["COUNT"].append(len(data))
        results["MEAN"].append(avg)
        results["MEDIAN"].append(median(data))
        results["MODE"].append(mode(data))
        results["SD"].append(standard_deviation(var))
        results["VARIANCE"].append(var)

    output_file = "output-files/P1/A4.2.P1.Results-output.txt"
    with open(output_file, "w", encoding="utf-8") as out:
        header = "TC\t" + "\t".join(f"TC{i + 1}" for i in range(len(files)))
        out.write(header + "\n")
        print(header)

        for key, values in results.items():
            row = key + "\t" + "\t".join(str(v) for v in values)
            out.write(row + "\n")
            print(row)

        print_elapsed(start_time, out)


if __name__ == "__main__":
    main()
