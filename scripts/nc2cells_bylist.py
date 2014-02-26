#!/usr/bin/env python

import os 
import os.path
import sys

import numpy as np
import numpy.ma as ma

from collections import OrderedDict as OD

try:
    from netCDF4 import Dataset
    from netCDF4 import num2date, date2num
except:
    print 'No netCDF4 module in path.  Proceeding without netCDF4 module support'

from mattslib.nclib import PyNC 

LLi_file = "goodlatlons.txt"
#LLi_file = "goodlatlons_1000.txt"
outdir   = "/raid3/stumbaugh/IS/CONUS/v2.2/nc2forcings_dump"
ncfilein = "CONUS_v2.2/macav2.2livneh_was_daily_CanESM2_historical_1950_1969_CONUS.nc"
ncfilein = "/home/raid3/stumbaugh/IS/CONUS/v2.2/splitmon/was/historical/CanESM2/1950-01-01_1950-01-31"

nc = PyNC.PyNC()

nc.read_txtLLinds(LLi_file)
nc.nc2txtcells(ncfilein)
#nc.dump_by_cell(outdir) #One cell per file
nc.dump_cells(outdir) # All cells per file
