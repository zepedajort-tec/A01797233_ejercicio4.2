"""
Utility functions shared across application modules.
"""

import time


def print_elapsed(start_time, output):
    """Print and save elapsed execution time."""
    elapsed = time.time() - start_time
    message = f"\nElapsed Time: {elapsed:.4f} seconds\n"
    output.write(message)
    print(message)
