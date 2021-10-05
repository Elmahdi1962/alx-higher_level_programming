#!/usr/bin/python3


class LockedClass:

    def __setattr__(self, key, value):
        if key == 'first_name':
            object.__setattr__(self, key, value)
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{:s}'".format(key)
                )

    def __init__(self):
        pass
