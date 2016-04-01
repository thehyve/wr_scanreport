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
        if fieldname not in self.scan_fields:
            self.scan_fields[ fieldname ] = ScanField( fieldname )
        
        return self.scan_fields.get( fieldname )
        
    def getScanFieldByName( self, fieldname ):
        """ Get existing scan field or returns False if not exists"""
        return self.scan_fields.get( fieldname, False )
