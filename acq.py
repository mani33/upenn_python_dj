# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:43:01 2021

@author: Mani

This is the code for creating all tables of the acq schema
"""

import datajoint as dj
schema = dj.Schema('acq')

@schema
class Animals(dj.Manual):
    definition = """
    # All details of each mouse are entered here.
    animal_id : int unsigned # mouse or rat id - internal to database
    -----
    dob=Null: date # date of birth in the format: 'YYYY-MM-DD'
    sex="unknown": enum('M','F','unknown') # male or female
    species:enum('mouse','rat') # mouse, rat, cat, dog, pig etc
    genotype= "unknown": varchar(256) # genotype e.g. DAT+/-
    strain_bkgd= "unknown" : varchar(256) # mouse or rat strain name C57
    source=Null : varchar(256) # from where the animals came from
    notes=Null: varchar(1024) # any special note about the animal
    other_id=Null: varchar(256) # any other alternative id
    father_id=Null: int unsigned # daddy
    mother_id=Null: int unsigned # mommy
    animals_ts=CURRENT_TIMESTAMP :  timestamp # automatically generated
    """
@schema
class Sessions(dj.Manual):
    definition = """
    acq.Sessions (manual) # list of sessions
    -> acq.Animals
    session_start_time: bigint              # start session timestamp
    ---
    session_stop_time           : bigint                        # end of session timestamp
    session_path                : varchar(255)                  # path to the data
    session_datetime=null       : datetime                      # readable format of session start
    room_num                    : varchar(24)      # room number where exp happened
    acq_system="Neuralynx"      : enum('Neuralynx','Plexon') # data acq system
    """
    
@schema
class Ephys(dj.Manual):
    definition = """
    # Basic details of the ephys acquisition session
    ->acq.Sessions
    ephys_start_time       : bigint       # start session timestamp
    ---
    ephys_stop_time        : bigint       # end of session timestamp
    ephys_path             : varchar(256) # path to the ephys data
    recording_software     : varchar(256) # name of the recording software with version number
    """
    
@schema
class Events(dj.Imported):
    definition = """
    # events from Neuralynx Events.nev file
    ->acq.Sessions
    event_ts       : bigint       # event timestamp
    event_ttl: double # value of the TTL pulse
    ---
    event_port: double # port number
    event_str: varchar(512) # event string
    """
        