#!/usr/bin/python3
"""
Script to compute metrics from log input
"""


import sys


def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def main():
    total_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    try:
        line_num = 0
        for line in sys.stdin:
            try:
                tokens = line.split()
                status_code, file_size = tokens[-2], int(tokens[-1])
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                line_num += 1
            except (IndexError, ValueError):
                pass

            if line_num % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
