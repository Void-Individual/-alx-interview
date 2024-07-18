#!/usr/bin/python3
"""Script to read stdin line by line and compute metrics"""

from sys import stdin
import ipaddress
from datetime import datetime

x = 1
file_size = 0
status_codes = {
    '200': 0, '301': 0, '400': 0,
    '401': 0, '403': 0, '404': 0,
    '405': 0, '500': 0}

# Toggle a loop to keep reading from stdin
while (x):
    try:
        # Read the passed line and confirm its format
        data = stdin.readline()
        # Retrieve the ip and confirm its validity
        ip = data.split(' ', maxsplit=1)[0]
        try:
            ipaddress.ip_address(str(ip))
            # Collect the rest of the line minus ip
            data = data.split('-', maxsplit=1)[1]
        except ipaddress.AddressValueError:
            continue

        # Retrieve and check the date sub-string format
        start_date = data.find('[')
        end_date = data.find(']')
        date = data[start_date + 1: end_date].strip()
        try:
            datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            # Retrieve the rest of the data without the date
            data = data.split("]")[1]
        except ValueError:
            continue

        # Retrieve and confirm the rest of the variables
        try:
            # Confirm the presence of the required get response
            data = data.split('\"GET /projects/260 HTTP/1.1\"')[1]
            # Retrieve the status code
            status_code = data.split()[0]
            # Add it to the stored dict keys if it exists
            if status_code in status_codes:
                status_codes[status_code] += 1
            # Retrieve the size of the file
            size = data.split()[-1]
            # Confirm it to be an int and add it to the cumulative
            file_size += int(size)
        except Exception:
            continue

    except KeyboardInterrupt:
        print(f"File size: {file_size}")
        for key, value in status_codes.items():
            print(f"{key}: {value}")
        break

    if x >= 10:
        print(f"File size: {file_size}")
        for key, value in status_codes.items():
            print(f"{key}: {value}")
        x = 1
    else:
        x += 1
