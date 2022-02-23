# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:51:32 2021

@author: Mani
# Here we have definitions of tables for the detect schema.
"""
import datajoint as dj
schema = dj.Schema('detect')

@schema
class Experts(dj.Manual):
    definition = """
    # human experts to detect various things manually
    expert_id: int unsigned # id - internal to database
    -----
    expert_name :varchar(256)# expert's name
    """
