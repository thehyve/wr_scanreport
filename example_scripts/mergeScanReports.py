# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:25:07 2016

@author: Maxim
"""

import copy
from wr_scanreport import ScanReport

scanReport1 = ScanReport( 'ScanReport_concept_1.xlsx' )
scanReport2 = ScanReport( 'ScanReport_MultiTable.xlsx' )

# Take first report as basis
scanReportMerge = copy.deepcopy( scanReport1 )
scanReportMerge.mergeScanReport( scanReport2 )

