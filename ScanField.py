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
        self.total_frequency = 0
        self.max_frequency = 0
        self.min_frequency = 999999999
        
    def setValueFrequency( self, value, frequency ):
        """ Sets the frequency, returns False if value already exists."""        
#        if value in self.value_frequencies:
#            return False
        
        frequency = int(frequency)
        value_key = str(value).lower()
        self.value_frequencies[ value_key ] = frequency
        
        # Update additional parameters
        self.total_frequency += frequency
        self.max_frequency = max( [self.max_frequency, frequency] )
        self.min_frequency = min( [self.min_frequency, frequency] )
        
    def getFrequencyByValue( self, value ):
        """ Returns False if value not exists. Effectively a zero. """
        value_key = str(value).lower()
        return self.value_frequencies.get( value_key, False ) 
        
    def addToFrequency( self, value, frequency_to_add ):
        """ Add frequency_to_add to the current frequency of value. Creates new value if value not yet present. """
        new_frequency = self.getFrequencyByValue( value ) + frequency_to_add
        self.setValueFrequency( value, new_frequency )
    
    def getValues( self ):
        return self.value_frequencies.keys()
        
    def printFrequencies( self, n = None, reverse = True ):
        if not n:
            n = len(self.value_frequencies)
        
        items = sorted( self.value_frequencies.items(), key = lambda x: x[1], reverse = reverse )
        
        for value, frequency in items[:n]:
            print "{:20.20} {:8}".format(value, frequency)