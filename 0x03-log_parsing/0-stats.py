#!/usr/bin/python3
"""
This script parse logs from the stdin.
"""
import sys
import re


def show_logs(status_frequency: dict, total_size: int) -> None:
    """"
    Updated regex pattern with correct groups for status code and file size
    """
    print('File total_size:{}'.format(total_size))
    for code in sorted(status_frequency):
        print("{}: {}".format(code, status_frequency[code]))


if __name__ == '__main__':
    pattern = (
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \['
        r'(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}\.\d+)\] '
        r'"GET /projects/\d+ HTTP/1\.1" '
        r'(\d{3}) (\d+)$'
    )
    status_code = [200, 301, 400, 401, 403, 404, 405, 500]
    total_size = 0
    counter = 0
    status_frequency = {str(code): 0 for code in status_code}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                counter += 1
                total_size += int(match.group(3))
                code = int(match.group(2))
                if code in status_code:
                    status_frequency[str(code)] += 1
                if counter % 10 == 0:
                    show_logs(status_frequency, total_size)
    except KeyboardInterrupt:
        show_logs(status_frequency, total_size)
