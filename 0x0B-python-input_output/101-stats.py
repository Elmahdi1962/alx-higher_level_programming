#!/usr/bin/python3
'''task 14 module'''


import sys
import signal

status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

total_size = i = 0


def printer(signum, frame):
    '''this function prints the statistics'''
    print(f'File size: {total_size}', flush=True)
    for key, value in status_codes.items():
        if value > 0:
            print(f'{key}: {value}', flush=True)


for line in sys.stdin:
    idx_status = line.find('1.1"') + 5
    idx_size = idx_status + 4
    status = line[idx_status:idx_status+3]
    total_size += int(line[idx_size:idx_size+4])
    status_codes[status] += 1
    i += 1
    signal.signal(signal.SIGINT, printer)
    if i >= 10:
        printer(1, 1)
        i = 0
