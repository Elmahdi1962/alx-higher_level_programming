#!/usr/bin/python3
'''class that rejcts __dict__ and uses slots instead'''


class LockedClass:
    '''this is the locked class'''

    __slots__ = "first_name"
