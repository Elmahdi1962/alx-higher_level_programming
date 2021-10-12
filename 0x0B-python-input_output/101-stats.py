#!/usr/bin/python3
'''task 14 module'''


from sys import stdin


status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }

total_size = i = 0


def printer():
    '''this function prints the statistics'''
    print(f'File size: {total_size}', flush=True)
    for key, value in status_codes.items():
        if value > 0:
            print(f'{key}: {value}', flush=True)


try:
    for line in stdin:
        try:
            splitted_line = line.split(' ')
            status = int(splitted_line[-2])
            total_size += int(splitted_line[-1])
            status_codes[status] += 1
        except Exception:
            pass
        i += 1

        if i >= 10:
            printer()
            i = 0
    printer()
except KeyboardInterrupt as e:
    printer()
    raise
