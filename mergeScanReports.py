# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:25:07 2016

@author: Maxim
"""

import xlrd

wb = xlrd.open_workbook('ScanReport_concept_1.xlsx')

sheet_overview = wb.sheet_by_index(0)

sheet_table = wb.sheet_by_index(1)

result = dict() #TODO: create object that contains white rabbit output.

# Every two columns is a pair of term values and term frequencies
column_indices = range(0,sheet_table.ncols,2)

for i in column_indices:
    #Name of the column at first row, left.
    column_name = sheet_table.cell( 0, i )
    
    # Get terms and frequencies belonging to this column.
    # Skip first column
    # Number of rows is as long as longest column. Means a lot of empty rows for some columns.
    term_values = sheet_table.col( i, 1)
    term_frequencies = sheet_table.col( i + 1, 1 )
    
    term_pairs = zip( term_values, term_frequencies )
    # Number of pairs is as long as
    
    frequencies_dict = dict()
    for term_value_cell, term_freq_cell in term_pairs:
        term_value = term_value_cell.value
        term_freq = term_freq_cell.value
        if not term_freq:
            continue
        
        frequencies_dict[ term_value ] = term_freq
        
        try:
            int(term_freq)
        except Exception as e:
            print e
            print term_freq
            
    result[ column_name ] = frequencies_dict