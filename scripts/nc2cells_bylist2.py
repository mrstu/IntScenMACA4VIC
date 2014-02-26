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

def main(args):
#     LLi_file = "goodlatlons.txt"
#     #LLi_file = "goodlatlons_1000.txt"
#     outdir   = "/raid3/stumbaugh/IS/CONUS/v2.2/nc2forcings_dump"
#     ncfilein = "CONUS_v2.2/macav2.2livneh_was_daily_CanESM2_historical_1950_1969_CONUS.nc"
#     ncfilein = "/home/raid3/stumbaugh/IS/CONUS/v2.2/splitmon/was/historical/CanESM2/1950-01-01_1950-01-31"
    
    LLi_file = args[0]
    outdir   = args[1]
#     ncfilein = args[2:]
    ncfilein = args[2]
    print args
    nc = PyNC.PyNC()
     
    nc.read_txtLLinds(LLi_file)

#     if len(ncfilein)>1:
#     for innc in ncfilein:            
#     print innc
    nc.nc2txtcells(ncfilein)
    #nc.dump_by_cell(outdir) #One cell per file
    nc.dump_cells(outdir) # All cells per file

if __name__=='__main__':
    if len(sys.argv)>=4:
        print sys.argv[1:]
        main(sys.argv[1:])
    else:
        print 'Need args <lat_lon_ilat_ilon table> <input netcdf file> <output location>'