# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:08:49 2022

@author: Mani
"""
""" This is a collection of utilities related to datajoint database
management"""

# First import the datajoint tables
import acq as acq
import numpy as np

# 1. Function for getting session keys from timestamp strings
def get_key_from_session_ts(sess_timestamps):
    """ This function will return database key from one or more session time stamps.
    Usage example1: key = get_key_from_session_ts('2019-09-24_09-13-53')
    Usage example2: keys = get_key_from_session_ts(['2019-09-24_09-13-53',
    '2020-11-24_19-14-53']) 
    Input: List of strings
    Output: List of dictionaryies    
    """
                
    assert len(sess_timestamps) != 0, "Input is empty."                                 
    # If a single string is given, convert it to a list for the sake of uniformity
    if isinstance(sess_timestamps,str):
        sess_timestamps = [sess_timestamps]
    
    # Iterate through each session time stamp and get a list of keys
    keys = []
    for st in sess_timestamps:
        cond_str = 'session_path like "%{}"'.format(st)
        key = (acq.Sessions & cond_str).fetch1('KEY')
        keys.append(key)
        
    return keys
        
def get_light_pulse_times(key): 
    # Returns light pulse on and off times for a given session
    # Input: a dict of database session
    # Output: pon_times - light pulse on times (us) - 1D numpy array of int64 time stamps
    #         poff_times - light pulse off times (us) - 1D numpy array of int64 time stamps
    assert type(key)==dict, 'Input must be a single dictionary of session key'
    
    on_str = 'event_ttl = 1 and event_port = 2'
    off_str = 'event_ttl = 0 and event_port = 2'
    pon_times = np.array((acq.Events & key & on_str).fetch('event_ts'))
    poff_times = np.array((acq.Events & key & off_str).fetch('event_ts'))
    
    return pon_times, poff_times
        
        
        
        
        