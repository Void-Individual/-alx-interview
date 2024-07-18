#!/usr/bin/python3
"""Script to read stdin line by line and compute metrics"""

from sys import stdin, stdout
import ipaddress
from datetime import datetime


def print_output() -> None:
    """Function to print output"""

    print(f"File size: {file_size}")
    for key, value in status_codes.items():
        if value > 0:
            print(f"{key}: {value}")
    stdout.flush()


if __name__ == "__main__":
    x = 1
    file_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0,
        '401': 0, '403': 0, '404': 0,
        '405': 0, '500': 0}

    # Toggle a loop to keep reading from stdin
    try:
        # Read the passed line and confirm its format
        for line in stdin:
            # Retrieve the ip and confirm its validity
            ip = line.split(' ', maxsplit=1)[0]
            try:
                ipaddress.ip_address(str(ip))
                # Collect the rest of the line minus ip
                line = line.split('-', maxsplit=1)[1]
            except ipaddress.AddressValueError:
                continue

            # Retrieve and check the date sub-string format
            start_date = line.find('[')
            end_date = line.find(']')
            date = line[start_date + 1: end_date].strip()
            try:
                datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
                # Retrieve the rest of the line without the date
                line = line.split("]")[1]
            except ValueError:
                continue

            # Retrieve and confirm the rest of the variables
            try:
                # Confirm the presence of the required get response
                line = line.split('\"GET /projects/260 HTTP/1.1\"')[1]
                # Retrieve the status code
                status_code = line.split()[0]
                # Add it to the stored dict keys if it exists
                if status_code in status_codes:
                    status_codes[status_code] += 1
                # Retrieve the size of the file
                size = line.split()[1]
                # print(status_code, size)
                # Confirm it to be an int and add it to the cumulative
                file_size += int(size)
                # print(x)
                if x == 10:
                    print_output()
                    x = 1
                else:
                    x += 1
            except Exception:
                continue
    finally:
        print_output()
