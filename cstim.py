# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:59:27 2021

@author: Mani
Here we place definitions of tables for the cstim schema
"""
import datajoint as dj
schema = dj.Schema('cstim')

@schema
class SlopeBinParams(dj.Manual):
    definition = """
    # fepsp slopes binning parameters
    slope_bw: double # bin width in minutes
    -----
    """

@schema
class SlopeParams(dj.Manual):
    definition = """
    # params for computing fepsp slopes
    slope_win = 500: double  # window in microsec for computing slope
    ---
    """
    
@schema
class FepspSlope(dj.Computed):
    definition = """
    # compute raising or falling slope of epsp
    -> cstim.FpRespTrace
    -> cstim.SlopeParams
    ---
    fepsp_slope                 : double                        # slope of epsp mV/ms
    slope_onset                 : double                        # onset of slope measurement (uS)
    """
@schema
class FpRespTrace(dj.Computed):
    definition = """
    # Trace of the field potential response trace
    -> acq.Events
    -> cont.Fp
    -> cstim.PeriEventTimes
    ---
    y       : longblob         # trace of the field potential responses (Volts)
    t       : longblob         # time points relative to event onset
    """
@schema
class SlopeBinned(dj.Computed):
    definition = """
    # bin the slopes of fepsp
    -> cont.Chan
    -> cstim.SlopeBinParams
    -----
    y:   longblob   # binned fepsp slope
    t       :   longblob   #middle bin time (us)
    se: longblob # standard error
    """    