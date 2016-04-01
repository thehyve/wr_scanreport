# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:02:46 2016

@author: Maxim
"""
from ScanField import ScanField

class ScanTable(object):
    """ All info of all fields of one table in a Scan Report """
    
    def __init__(self, name):
        self.name = name
        self.scan_fields = dict() #name : ScanField
    
    def createScanField( self, fieldname ):
        """ Create new scan field and return it or return existing if fieldname already present """
        field_key = str(fieldname).lower()
        if field_key not in self.scan_fields:
            self.scan_fields[ field_key ] = ScanField( fieldname )
        
        return self.scan_fields.get( field_key )
        
    def getScanField( self, fieldname ):
        """ Get existing scan field or returns False if not exists"""
        field_key = str(fieldname).lower()
        try:
            return self.scan_fields[ field_key ]
        except KeyError:
            raise Exception("Could not find field name '%s' in table '%s'" % (fieldname, self.name) )
        
    def getFieldNames( self ):
        return sorted( [scanField.name for scanField in self.scan_fields.values()] )
        
    def getScanFields( self ):
        return self.scan_fields.values()
        
    def printTotals( self ):
        for scanField in self.getScanFields():
            print "{:20.20} {:8}".format(scanField.name, scanField.total_frequency)
        
            