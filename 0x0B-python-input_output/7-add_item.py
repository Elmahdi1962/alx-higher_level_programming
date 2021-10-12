#!/usr/bin/python3
'''task 7 module'''


import sys, 5-save_to_json_file, 6-load_from_json_file

arglist = list(sys.argv)

arglist += load_from_json_file('add_item.json')

save_to_json_file(arglist, 'add_item.json')
