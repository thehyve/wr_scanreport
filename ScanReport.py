# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:03 2016

@author: Maxim
"""

import xlrd
import ScanTable

class ScanReport(object):
    
    def __init__( self, filename ):
        self.filename = filename
        self.scan_tables = dict()
    
    def loadFromFile( self, filename ):
        """ Loads file and fills ScanTable and ScanFields
            Returns true if success."""   
        
        wb = xlrd.open_workbook( filename )
        sheets = wb.sheets()
        
        sheet_overview = sheets.pop(0)
        #TODO: process the overview sheet (n_rows, type, etc.)
        
        for sheet_table in sheets:
            table_name = sheet_table.name
            
            scanTable = self.createScanTable( table_name )
            
            self._processValueFrequencies( sheet_table, scanTable )
        
        return True


    def _processValueFrequencies( self, sheet_table, scanTable ):
        """ Processes value frequencies from one table. Returns the number of scan fields added to scanTable """
        # Every two columns is a pair of term values and term frequencies
        column_indices = range( 0, sheet_table.ncols, 2)
                    
        n_columns_processed = 0
        for i in column_indices:
            #Name of the column at first row, left.
            column_name = sheet_table.cell( 0, i )
            
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
        if table_name not in self.scan_tables:
            self.scan_tables[ table_name ] = ScanTable( table_name )
        
        return self.scan_tables.get( table_name )
        
    def getScanTable( self,  table_name ):
        return self.scan_tables.get( table_name, False )
        
    def createDummyData( self, folder, n_rows ):
        pass