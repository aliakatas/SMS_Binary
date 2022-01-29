import pathlib as plib
import pandas as pd
from .smsdat_cards import cards

class SMSDat:
    '''
    '''
    def __init__(self, filepath=None, io='i'):

        self._filepath = filepath 
        
        if self._filepath != None:
            self._filepath = plib.Path(self._filepath).resolve()
            if self._filepath.is_file() and io == 'i': 
                self._fid = open(self._filepath, 'rb')
        else:
            raise FileNotFoundError('There is no data file provided.')
    
    def __repr__(self):
        return f'SMS Binary file: {self._filepath}'

    def read_contents(self):
        bytes = self._fid.read(4)
        if bytes == cards['Version']:
            print(bytes)
        elif bytes == cards['Object type']:
            print(bytes)
        elif bytes ==  cards['Size of float']:
            print(bytes)
        elif bytes ==  cards['Size of flag']:
            print(bytes)
        elif bytes ==  cards['Scalar']:
            print(bytes)
        elif bytes ==  cards['Vector']:
            print(bytes)
        elif bytes ==  cards['Vector type']:
            print(bytes)
        elif bytes ==  cards['Object ID']:
            print(bytes)
        elif bytes ==  cards['Number of data']:
            print(bytes)
        elif bytes ==  cards['Number of cells']:
            print(bytes)
        elif bytes ==  cards['Name']:
            print(bytes)
        elif bytes ==  cards['Timecard-start']:
            print(bytes)
        elif bytes ==  cards['Timecard-end']:
            print(bytes)
        elif bytes ==  cards['Reference time']:
            print(bytes)
        elif bytes ==  cards['Time units']:
            print(bytes)
        else:
            print('Unknown bytes')
    