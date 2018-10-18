#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:05:33 2018

@author: tim
"""

import numpy
import random


def gen_block(size = 4, index_of_def = 0):
    instances = gen_instances(size)
    c_insts = assign_category(instances, index_of_def)
    return(c_insts)
    
def gen_shuffled_block(size = 4, index_of_def = 0):
    instances = gen_instances(size)
    c_insts = assign_category(instances, index_of_def)
    random.shuffle(c_insts)
    return(c_insts)


def var_blocks():
    
    #first block def     : 1 at block[0]
    #distractor block def: 1 at block[1]
    
    first_block_no_var = [
            [0, [0, 0, 0, 0]],
            [0, [0, 0, 0, 1]],
            [0, [0, 0, 1, 0]],
            [0, [0, 0, 1, 1]],
            [0, [0, 1, 0, 0]], # switch
            [0, [0, 1, 0, 1]],
            [0, [0, 1, 1, 0]], # switch
            [0, [0, 1, 1, 1]],
            [1, [1, 0, 0, 0]],
            [1, [1, 0, 0, 1]], # switch
            [1, [1, 0, 1, 0]],
            [1, [1, 0, 1, 1]], # switch
            [1, [1, 1, 0, 0]],
            [1, [1, 1, 0, 1]],
            [1, [1, 1, 1, 0]],
            [1, [1, 1, 1, 1]]
            ]
    
    distractor_block_no_var= [
        [0, [0, 0, 0, 0]],
        [0, [0, 0, 0, 1]],
        [0, [0, 0, 1, 0]],
        [0, [0, 0, 1, 1]],
        [1, [0, 1, 0, 0]], #switch
        [1, [0, 1, 0, 1]],
        [1, [0, 1, 1, 0]], #switch
        [1, [0, 1, 1, 1]],
        [0, [1, 0, 0, 0]],
        [0, [1, 0, 0, 1]], #switch
        [0, [1, 0, 1, 0]],
        [0, [1, 0, 1, 1]], #switch
        [1, [1, 1, 0, 0]],
        [1, [1, 1, 0, 1]],
        [1, [1, 1, 1, 0]],
        [1, [1, 1, 1, 1]]
        ]
    
    first_block_var = [
            [0, [0, 0, 0, 0]],
            [0, [0, 0, 0, 1]],
            [0, [0, 0, 1, 0]],
            [0, [0, 0, 1, 1]],
            [1, [0, 1, 0, 0]], # switch
            [0, [0, 1, 0, 1]],
            [1, [0, 1, 1, 0]], # switch
            [0, [0, 1, 1, 1]],
            [1, [1, 0, 0, 0]],
            [0, [1, 0, 0, 1]], # switch
            [1, [1, 0, 1, 0]],
            [0, [1, 0, 1, 1]], # switch
            [1, [1, 1, 0, 0]],
            [1, [1, 1, 0, 1]],
            [1, [1, 1, 1, 0]],
            [1, [1, 1, 1, 1]]
            ]
    
    distractor_block_var= [
        [0, [0, 0, 0, 0]],
        [0, [0, 0, 0, 1]],
        [0, [0, 0, 1, 0]],
        [0, [0, 0, 1, 1]],
        [0, [0, 1, 0, 0]], #switch
        [1, [0, 1, 0, 1]],
        [0, [0, 1, 1, 0]], #switch
        [1, [0, 1, 1, 1]],
        [0, [1, 0, 0, 0]],
        [1, [1, 0, 0, 1]], #switch
        [0, [1, 0, 1, 0]],
        [1, [1, 0, 1, 1]], #switch
        [1, [1, 1, 0, 0]],
        [1, [1, 1, 0, 1]],
        [1, [1, 1, 1, 0]],
        [1, [1, 1, 1, 1]]
        ]
    
    random.shuffle(first_block_no_var) 
    random.shuffle(distractor_block_no_var)
    random.shuffle(first_block_var)
    random.shuffle(distractor_block_var)
    
    lo_var_lo_vol = [first_block_no_var, first_block_no_var, distractor_block_no_var, distractor_block_no_var]
    hi_var_lo_vol = [distractor_block_var, distractor_block_var, first_block_var, first_block_var]
    lo_var_hi_vol = [first_block_no_var, first_block_no_var, distractor_block_no_var, distractor_block_no_var]
    hi_var_hi_vol = [distractor_block_var, first_block_var, distractor_block_var, first_block_var]
    
    
    
    return ({'lo_var_lo_vol':lo_var_lo_vol,
             'hi_var_lo_vol':hi_var_lo_vol,
             'lo_var_hi_vol':lo_var_hi_vol,
             'hi_var_hi_vol':hi_var_hi_vol
            })
    
    

    
    
    
    
    
    

