#!/usr/bin/python3
'''contains the MyList class'''

class MyList(list):
    '''represents MyList'''

    def print_sorted(self):
        '''prints the list, but sorted'''

        print(sorted(self))
