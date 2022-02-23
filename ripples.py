# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:10:19 2021

@author: Mani
# Definitions of tables for the ripples schema
"""
import datajoint as dj
schema = dj.Schema('ripples')

@schema
class DetFilterParams(dj.Manual):
    definition = """ 
    # ripple detection filter settings
    cutoff_low: int unsigned # filter low cutoff
    cutoff_high: int unsigned # high cutoff
    transband_low: int unsigned # transition on the left side
    transband_high:int unsigned # transition on the right side
    fs: int unsigned # sampling rate
    -----
    """
    
@schema
class DetFilter(dj.Manual):
    definition = """
    # ripple detection filter settings
    cutoff_low: int unsigned # filter low cutoff
    cutoff_high: int unsigned # high cutoff
    transband_low: int unsigned # transition on the left side
    transband_high:int unsigned # transition on the right side
    fs: int unsigned # sampling rate
    -----
    filter_obj: blob # filterfactory object for filtering
    """
    
@schema
class DetParams(dj.Manual):
    definition = """
    # ripple detection filter settings
    std: double # thresholding standard deviation
    seg_len: double # duration of segments (in sec) for detecting ripples
    minwidth: double # minimum width (in ms)to be considered as a ripple event
    mingap: double # minimum gap (in ms) between ripple events
    -----
    """
    
@schema
class PeriEventFpTrace(dj.Computed):
    definition = """
    # lfp trace of the ripplemy newest table
    -> cont.Fp
    -> ripples.PeriEventTimes
    -> acq.Events
    -----
    t: longblob # time in s
    y: longblob # field potential trace in Volts
    """    
    
@schema
class PeriEventTimes(dj.Manual):
    definition = """
    # pre and post event times for picking traces
    pre: double              # pre event time in s
    post: double              # post event time in s
    -----
    """  
    
@schema
class RipEvents(dj.Computed):
    definition = """
    # Ripple events details
    ->acq.Ephys
    ->cont.Chan
    -> ripples.DetFilter
    -> ripples.DetParams
    begin : double # ripple start time
    -----
    y: blob # waveform of the ripple
    rms_mag: double # rms magnitude of the ripple
    peak_amp   : double # ripple peak time
    peak_t: double # peak time
    peak_prom : double # peak prominence
    width: double # width of ripple in ms
    """
    
    
    