# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:47:19 2021

@author: Mani
Here we place all table definitions for the Cont(continuous data) schema
"""
import datajoint as dj
schema = dj.Schema('cont')

@schema
class Chan(dj.Imported):
    definition = """
    # cont.Chan (imported) # select channels for extracting continuous traces
    ->acq.Ephys
    chan_num: tinyint unsigned # A/D channel number starts from 0
    ---
    chan_name: varchar(24) # name of the channel such as t1c1
    chan_filename: varchar(256) # file location of raw data
    chan_ts = CURRENT_TIMESTAMP :  timestamp # automatically generated
    """
    
@schema
class ChanType(dj.Manual):
    definition = """
    # channel type: emg or recording
    -> acq.Animals
    chan_type_num: tinyint unsigned # corresponds to which type of channel
    chan_num: tinyint unsigned # number of the channel
    ---
    chan_type: varchar(12) # name of the type of channel
    """
    
@schema
class Fp(dj.Computed):
    definition = """
    # local field filtered at 0.1-5000Hz
    -> acq.Ephys
    -> cont.Chan
    -> cont.FpParams
    ---
    fp_file           : varchar(255)      # name of file containg field potential
    sampling_rate     : double            # sampling rate of trace
    """
    
@schema
class FpParams(dj.Manual):
    definition = """
    # Parameters being used field potential filtering
    cutoff_freq: double # low pass cutoff frequency
    ---
    """
    
@schema
class Motion(dj.Computed):
    definition = """
    # Motion tracking data
    -> cont.MotionParams
    -> acq.Sessions
    ---    
    dist_var:   longblob   #variance of the distance from the origin
    t       :   longblob   #middle bin time (us)
    """
    
@schema
class MotionBinned(dj.Computed):
    definition = """
    # Motion data binned
    -> cont.Motion
    -> cstim.SlopeBinParams
    -----
    y:   longblob   # binned fepsp slope
    t       :   longblob   #middle bin time (us)
    se: longblob # standard error
    """

@schema
class MotionBinParams(dj.Manual):
    definition = """
    # Motion binning parameters
    motion_avg_bw: double # bin width in minutes
    -----
    """
    
@schema
class MotionParams(dj.Manual):
    definition = """
    # params for computing motion index
    bw = 5: double  # window in sec for computing motion index
    ---
    """
@schema
class NremSegManual(dj.Computed):
    definition = """
    # Non_REM segments manually selected
    -> cont.Motion
    -> detect.Experts
    -----
    seg_begin : blob # segment startings
    seg_end : blob # segment ends
    """

@schema
class RemSegManual(dj.Computed):
    defnition = """
    # REM segments
    -> cont.Motion
    -> detect.Experts
    -----
    seg_begin : blob # segment startings
    seg_end : blob # segment ends
    """
    
@schema
class SleepSegManual(dj.Computed):
    definition = """
    # Sleep segments manually extracted
    -> cont.Motion
    -> detect.Experts
    -----
    seg_begin: blob # sleep segment beginnings
    seg_end: blob # sleep segment ends
    """
    
@schema
class TDratio(dj.Computed):
    definition = """
    # Theta-Delta Ratio
    -> cont.Chan
    -> acq.Sessions
    -> cont.TDratioParams
    ---
    theta_data:   longblob   #theta wave activity
    delta_data:   longblob   #delta wave activity
    td_ratio:     longblob   #ration of theta wave to delta wave activity
    t       :   longblob     # bin center time (microsec, neuralynx time)
    """
    
@schema
class TDratioParams(dj.Manual):
    definition = """
    # Theta - delta ratio parameters
    theta_begin: double # theta band start freq
    theta_end: double # theta band end freq
    delta_begin: double # delta begin freq
    delta_end: double # delta end freq
    td_bw: double # bin width in seconds for computing theta delta ratio
    -----
    """

@schema
class TdrBinned(dj.Computed):
    definition = """
    # Theta delta ratio binned
    -> cont.TDratio
    -> cstim.SlopeBinParams
    -----
    y:   longblob   # binned thetal/delta ratio
    t       :   longblob   #middle bin time (us)
    se: longblob # standard error
    th: longblob # thetal power binned
    se_th: longblob # standard error for theta power
    del: longblob # delta power binned
    se_del: longblob # delta power standard error
    """
    
@schema
class TdrBinParams(dj.Manual):
    definition = """
    # Binning params for td ratio
    tdr_avg_bw: double # bin width in minutes
    -----
    """   
    
    
    
    
    
    
    
    
    