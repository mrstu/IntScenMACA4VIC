#!/usr/bin/env python

import os 
import os.path
import sys
import glob

import numpy as np
import numpy.ma as ma

from collections import OrderedDict as OD

egoodcols = "/home/stumbaugh/downloader/IS/v2.2/dummy_valinds.txt"
#LLi_file = "goodlatlons_1000.txt"
eindir   = "/raid3/stumbaugh/IS/CONUS/v2.2/nc2forcings_dump/tasmax/rcp45/CanESM2"
eoutdir   = "/raid3/stumbaugh/IS/CONUS/v2.2/active_cells/tasmax/rcp45/CanESM2"

def main(args):
    '''Simple script to read sequential blocks of data and write/append active columns to individual time series files.'''
#     LLi_file = "goodlatlons.txt"
#     #LLi_file = "goodlatlons_1000.txt"
#     outdir   = "/raid3/stumbaugh/IS/CONUS/v2.2/nc2forcings_dump"
#     ncfilein = "CONUS_v2.2/macav2.2livneh_was_daily_CanESM2_historical_1950_1969_CONUS.nc"
#     ncfilein = "/home/raid3/stumbaugh/IS/CONUS/v2.2/splitmon/was/historical/CanESM2/1950-01-01_1950-01-31"
    
    goodcols = args[0]
    indir = args[1]
    outdir   = args[2]
    
    try:
        os.makedirs(outdir)
    except OSError:
        pass
    
    cols = np.loadtxt(goodcols, np.int)
    
    filelist=glob.glob('%s/*'%indir)
    for infile in filelist:
        print infile
        
        a = np.loadtxt(infile,usecols=cols)
        for nc, ic in enumerate(cols):
            fout = open("%s/cell_%i"%(outdir,ic),"a+")
            np.savetxt(fout,a[:,nc],fmt="%4.3f")
            fout.close()
            

if __name__=='__main__':    
    if len(sys.argv)>=4:
        print sys.argv[1:]
        main(sys.argv[1:])
    else:
        print 'Need args <column index list> <monthly grid base location> <output location>'
        print 'For example:'
        print 'python grd2active.py %s %s %s'%(egoodcols, eindir, eoutdir)