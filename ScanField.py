# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:03:47 2016

@author: Maxim
"""


class ScanField(object):
    """ Fieldname and frequencies of unique values """
    
    def __init__(self, name):
        self.name = name
        self.type = None
        self.max_length = None
        self.n_rows = None
        self.n_rows_checked = None
        self.fraction_empty = None
        
        self.value_frequencies = dict()
        
    def setValueFrequency( self, value, frequency ):
        """ Sets the frequency, returns False if value already exists."""        
        if value in self.value_frequencies:
            return False
        
        self.value_frequencies[ str(value) ] = int(frequency)
        return True
    
    def getValueFrequency( self, value ):
        return self.value_frequencies.get( value, False ) #return false if not exists
    
    