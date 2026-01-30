"""
Count distinct words and their frequencies in one or more text files.
"""

import sys
import time
import os
from .utils import print_elapsed


OUTPUT_DIR = "testing-files/P3"


def process_file(filename: str) -> None:
    """Process a single file and generate its word count output."""
    start_time = time.time()
    counts: dict[str, int] = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(filename))[0]
    output_file = os.path.join(
        OUTPUT_DIR, f"{base_name}.Result-output.txt"
    )

    with open(output_file, "w", encoding="utf-8") as out:
        header = f"Row Labels\tCount of {base_name}"
        out.write(header + "\n")
        print(header)

        total = 0
        for word in sorted(counts):
            out.write(f"{word}\t{counts[word]}\n")
            print(f"{word}\t{counts[word]}")
            total += counts[word]

        out.write("(blank)\t\n")
        out.write(f"Grand Total\t{total}\n")
        print(f"Grand Total\t{total}")

        print_elapsed(start_time, out)


def main():
    """Main program execution."""
    if len(sys.argv) < 2:
        print("Usage: python -m app.word_count file1.txt [file2.txt ...]")
        sys.exit(1)

    for filename in sys.argv[1:]:
        process_file(filename)


if __name__ == "__main__":
    main()
