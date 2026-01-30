# Python File Processing Project

This project contains three Python scripts designed to process text files using different approaches:

- **Compute Statistics**: Calculates basic numeric statistics.
- **Convert Numbers**: Converts textual numbers into their numeric representation.
- **Word Count**: Counts distinct words and their frequencies across one or more text files.

The entire workflow is managed using a **Makefile**.

---

## Project Structure
```
├── app/
│ ├── compute_statistics.py
│ ├── convert_numbers.py
│ ├── word_count.py
│ └── utils.py
│
├── testing-files/
│ ├── P1/ # Input files for Compute Statistics
│ ├── P2/ # Input files for Convert Numbers
│ └── P3/ # Input and output files for Word Count
│
├── requirements.txt
├── Makefile
└── README.md
```

## Requirements

- Python **3.9 or higher**
- `pip`
- Linux or macOS (recommended)

---

## Run the Entire Project

To install dependencies, run lint checks, and execute all programs in order:
```bash
  make run-all
```

## Clean Generated Files

To remove all generated output files (*.Result-output.txt):
```bash
  make clean
```

## Installation

Install all project dependencies by running:

```bash
  make install 
```

This command installs the packages listed in requirements.txt.

## Code Quality (Linting)

Run pylint without failing the build:
```bash
  make lint
```


Run pylint in strict mode (fails on any warning or error):
```bash
  make lint-strict
```
## Running the Programs
###  Compute Statistics

Processes multiple input files located in testing-files/P1/:
```bash
  make run-stat
```

### Convert Numbers

Processes input files located in testing-files/P2/:
```bash
  make run-convert
```

### Word Count

Processes multiple input files located in testing-files/P3/ and generates the output files in the same directory:
```bash
  make run-word
```
Output files are created using the following format:

testing-files/P3/<input_filename>.Result-output.txt