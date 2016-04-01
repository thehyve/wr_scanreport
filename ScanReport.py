# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:03 2016

@author: Maxim
"""

import xlrd
from ScanTable import ScanTable

class ScanReport(object):
    
    def __init__( self, filename = None ):
        self.filename = filename
        self.scan_tables = dict()
        
        if filename:
            self.loadFromFile( filename )
    
    def loadFromFile( self, filename ):
        """ Loads file and fills ScanTable and ScanFields
            Returns true if success."""   
        
        wb = xlrd.open_workbook( filename )
        sheets = wb.sheets()
        
        sheet_overview = sheets.pop(0)
        #TODO: process the overview sheet (n_rows, type, etc.)
        
        for sheet_table in sheets:            
            self._processSheet( sheet_table )
        
        return True


    def _processSheet( self, sheet_table ):
        """ Processes value frequencies from one table. Returns the number of scan fields added to scanTable """
        # Create new Dcan Table object.
        table_name = sheet_table.name
        scanTable = self.createScanTable( table_name )
        
        # Every two columns is a pair of term values and term frequencies
        column_indices = range( 0, sheet_table.ncols, 2)
                    
        n_columns_processed = 0
        for i in column_indices:
            #Name of the column at first row, left.
            column_name_cell = sheet_table.cell( 0, i )
            column_name = column_name_cell.value
            
            scanField = scanTable.createScanField( column_name )
            
            # Get terms and frequencies belonging to this column.
            # Skip first column
            # Number of rows is as long as longest column. Means a lot of empty rows for some columns.
            term_values = sheet_table.col( i, 1)
            term_frequencies = sheet_table.col( i + 1, 1 )
            
            term_pairs = zip( term_values, term_frequencies )
            
            for term_value_cell, term_freq_cell in term_pairs:
                term_value = term_value_cell.value
                term_freq = term_freq_cell.value
                
                #Break if no frequency, then the end is reached (columns are frequency ordered)
                if not term_freq:
                    break
                
                scanField.setValueFrequency( term_value, term_freq )
            
            n_columns_processed += 1
        
        return n_columns_processed
    
    def createScanTable( self, table_name ):
        """ Create new scan table and return it or return existing if table name already present """
        tablename_key = str(table_name).lower()
        if tablename_key not in self.scan_tables:
            self.scan_tables[ tablename_key ] = ScanTable( table_name )
        
        return self.scan_tables.get( tablename_key )
        
    def getScanTable( self,  table_name ):
        tablename_key = str(table_name).lower()
        try:
            return self.scan_tables[ tablename_key ]
        except KeyError:
            raise Exception("Could not find table name '%s'" % table_name)
    
    def getScanTables( self ):
        return self.scan_tables.values()
        
    def getValueFrequencyByIdentifier( self, table_name, field_name, value_name ):
        sTable = self.getScanTable( table_name )            
        sField = sTable.getScanField( field_name )
            
        frequency = sField.getFrequencyByValue( value_name )
        if frequency is False:
            raise Exception("Could not find value name '%s'" % value_name)
            
        return frequency
        
    def mergeScanReport( self, scan_report_to_add ):
        """ Merges current scan report with a second scan_report.
            All frequencies are added up. If table/field/value not already present, then create new."""
        
        # For every table, for every field, add frequencies
        tables_to_add = scan_report_to_add.getScanTables()        
        for table in tables_to_add:
            table_name = table.name
            fields = table.getScanFields()
            
            for field in fields:  
                field_name = field.name
                values = field.getValues()
                
                for value in values:
                    frequency = field.getFrequencyByValue( value )
                    self._addFrequencyByIdentifier( frequency, table_name, field_name, value )
    
    def _addFrequencyByIdentifier( self, frequency_to_add, table_name, field_name, value_name ):
        # Create or return table/field if already exists
        scan_table = self.createScanTable( table_name )
        scan_field = scan_table.createScanField( field_name )
        scan_field.addToFrequency( value_name, frequency_to_add )
        
        
    def createDummyData( self, folder, n_rows ):
        pass