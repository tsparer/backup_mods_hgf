#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:05:33 2018

@author: tim
"""

import numpy
import random
import simple_hgf_agent_1_oct_22_2018 as hgf
import json


def gen_instances(length):
    instances_s = ["".join(seq) for seq in itertools.product("01", repeat=length)]
    instances = [[int(i) for i in list(elem)] for elem in instances_s]
    return(instances)


def assign_category(l_instances, index_of_feat):
    categorized_instances = []
    for inst in l_instances:
        inst_and_def = []
        if inst[index_of_feat] == 1:
            inst_and_def.append(1)
            inst_and_def.append(inst)
        else:
            inst_and_def.append(0)
            inst_and_def.append(inst)
        categorized_instances.append(inst_and_def)
    return categorized_instances



def gen_block(size = 4, index_of_def = 0):
    instances = gen_instances(size)
    c_insts = assign_category(instances, index_of_def)
    return(c_insts)
    
def gen_shuffled_block(size = 4, index_of_def = 0):
    instances = gen_instances(size)
    c_insts = assign_category(instances, index_of_def)
    random.shuffle(c_insts)
    return(c_insts)
    
def gen_multi_blocks(multi_size, block_size, index_of_def = 0):
    multi_blocks = []
    for i in range(multi_size):
        new_block = gen_shuffled_block(block_size, index_of_def)
        multi_blocks = multi_blocks + new_block
        
    return(multi_blocks)
        
        


def create_cond_blocks():
    
    #first block def     : 1 at block[0]
    #distractor block def: 1 at block[1]
    
    first_block_no_var = [
            [0, [0, 0, 0, 0],'m'],
            [0, [0, 0, 0, 1],'m'],
            [0, [0, 0, 1, 0],'m'],
            [0, [0, 0, 1, 1],'m'],
            [0, [0, 1, 0, 0],'m'], # switch
            [0, [0, 1, 0, 1],'m'],
            [0, [0, 1, 1, 0],'m'], # switch
            [0, [0, 1, 1, 1],'m'],
            [1, [1, 0, 0, 0],'m'],
            [1, [1, 0, 0, 1],'m'], # switch
            [1, [1, 0, 1, 0],'m'],
            [1, [1, 0, 1, 1],'m'], # switch
            [1, [1, 1, 0, 0],'m'],
            [1, [1, 1, 0, 1],'m'],
            [1, [1, 1, 1, 0],'m'],
            [1, [1, 1, 1, 1],'m']
            ]
    
    distractor_block_no_var= [
        [0, [0, 0, 0, 0],'d'],
        [0, [0, 0, 0, 1],'d'],
        [0, [0, 0, 1, 0],'d'],
        [0, [0, 0, 1, 1],'d'],
        [1, [0, 1, 0, 0],'d'], #switch
        [1, [0, 1, 0, 1],'d'],
        [1, [0, 1, 1, 0],'d'], #switch
        [1, [0, 1, 1, 1],'d'],
        [0, [1, 0, 0, 0],'d'],
        [0, [1, 0, 0, 1],'d'], #switch
        [0, [1, 0, 1, 0],'d'],
        [0, [1, 0, 1, 1],'d'], #switch
        [1, [1, 1, 0, 0],'d'],
        [1, [1, 1, 0, 1],'d'],
        [1, [1, 1, 1, 0],'d'],
        [1, [1, 1, 1, 1],'d']
        ]
    
    first_block_var = [
            [0, [0, 0, 0, 0],'m'],
            [0, [0, 0, 0, 1],'m'],
            [0, [0, 0, 1, 0],'m'],
            [0, [0, 0, 1, 1],'m'],
            [1, [0, 1, 0, 0],'m', 's'], # switch
            [0, [0, 1, 0, 1],'m'],
            [1, [0, 1, 1, 0],'m', 's'], # switch
            [0, [0, 1, 1, 1],'m'],
            [1, [1, 0, 0, 0],'m'],
            [0, [1, 0, 0, 1],'m', 's'], # switch
            [1, [1, 0, 1, 0],'m'],
            [0, [1, 0, 1, 1],'m', 's'], # switch
            [1, [1, 1, 0, 0],'m'],
            [1, [1, 1, 0, 1],'m'],
            [1, [1, 1, 1, 0],'m'],
            [1, [1, 1, 1, 1],'m']
            ]
    
    distractor_block_var= [
        [0, [0, 0, 0, 0],'d'],
        [0, [0, 0, 0, 1],'d'],
        [0, [0, 0, 1, 0],'d'],
        [0, [0, 0, 1, 1],'d'],
        [0, [0, 1, 0, 0],'d', 's'], #switch
        [1, [0, 1, 0, 1],'d'],
        [0, [0, 1, 1, 0],'d', 's'], #switch
        [1, [0, 1, 1, 1],'d'],
        [0, [1, 0, 0, 0],'d'],
        [1, [1, 0, 0, 1],'d', 's'], #switch
        [0, [1, 0, 1, 0],'d'],
        [1, [1, 0, 1, 1],'d', 's'], #switch
        [1, [1, 1, 0, 0],'d'],
        [1, [1, 1, 0, 1],'d'],
        [1, [1, 1, 1, 0],'d'],
        [1, [1, 1, 1, 1],'d']
        ]
    
    random.shuffle(first_block_no_var) 
    random.shuffle(distractor_block_no_var)
    random.shuffle(first_block_var)
    random.shuffle(distractor_block_var)
    
    lo_var_lo_vol = distractor_block_no_var+ distractor_block_no_var + first_block_no_var+first_block_no_var
    hi_var_lo_vol = distractor_block_var + distractor_block_var + first_block_var + first_block_var
    lo_var_hi_vol = distractor_block_no_var + first_block_no_var + distractor_block_no_var + first_block_no_var
    hi_var_hi_vol = distractor_block_var + first_block_var + distractor_block_var + first_block_var
    # Note, if I want to make the conditions larger, e.g. 8 total sequences (hi, med, low, volatility), include
    # Can simply add more here, using the 
    # Also, to avoid overtraining the misconception, may also want to change to a 2nd distractor sequence?
    # Also, see current analysis plan, may want to change the %assessment_correct for the recall condition
    # 
    
    
    
    return ({'lo_var_lo_vol':lo_var_lo_vol,
             'hi_var_lo_vol':hi_var_lo_vol,
             'lo_var_hi_vol':lo_var_hi_vol,
             'hi_var_hi_vol':hi_var_hi_vol
            })
    
    
def gen_full_exp(condition):
    
    instances_dict = {}
    index = 0
    miscon1 = gen_multi_blocks(multi_size =4, block_size =4, index_of_def = 0)
    for i in range(len(miscon1)):
        instance_entry = {'trial_number':index, 'learning_period':'m', 'block_type':'m', 
                          'train_v_assess':'train' , 'index_of_def_var':0, 'instance':miscon1[i][1],
        'val_of_def_var_on_instance':miscon1[i][1][0], 'is_cat':miscon1[i][0], 'is_switch': 0 }
        instances_dict[index] = instance_entry
        index += 1
        
    assess1 = gen_multi_blocks(multi_size =1, block_size =4, index_of_def = 0)
    for i in range(len(assess1)):
        instance_entry = {'trial_number':index, 'learning_period':'m', 'block_type':'m', 
                          'train_v_assess':'assess' , 'index_of_def_var':'changes', 'instance':assess1[i][1],
        'val_of_def_var_on_instance':assess1[i][1][0], 'is_cat':assess1[i][0], 'is_switch': 0 }
        instances_dict[index] = instance_entry
        index += 1
    
    possible_conditions = create_cond_blocks()
    cond = possible_conditions[condition]
    for i in range(len(cond)):
        instance_entry = {'trial_number':index, 'learning_period':'d', 'block_type':cond[i][2], 
                          'train_v_assess':'train' , 'index_of_def_var':1, 'instance':cond[i][1],
        'val_of_def_var_on_instance':cond[i][1][1], 'is_cat':cond[i][0]}
        
        if len(cond[i]) == 4:
            instance_entry['is_switch'] = 1
        else:
            instance_entry['is_switch'] = 0
            
        instances_dict[index] = instance_entry
        index += 1
    
    #[0, [1, 0, 1, 0],'d'],
    #[1, [1, 0, 1, 1],'d', 's'], #switch
        
    
    assess2 = gen_multi_blocks(multi_size =1, block_size =4, index_of_def = 0) # Note that this is currently scoring the output based on it's relationship to the misconception
    for i in range(len(assess2)):
        instance_entry = {'trial_number':index, 'learning_period':'d', 'block_type':'m', 
                          'train_v_assess':'assess' , 'index_of_def_var':0, 'instance':assess2[i][1],
        'val_of_def_var_on_instance':assess2[i][1][0], 'is_cat':assess2[i][0], 'is_switch': 0 }
        instances_dict[index] = instance_entry
        index += 1
    
    target = gen_multi_blocks(multi_size =4, block_size =4, index_of_def = 2)
    for i in range(len(target)):
        instance_entry = {'trial_number':index, 'learning_period':'target', 'block_type':'target', 
                          'train_v_assess':'train' , 'index_of_def_var':2, 'instance':target[i][1],
        'val_of_def_var_on_instance':target[i][1][2], 'is_cat':target[i][0], 'is_switch': 0 }
        instances_dict[index] = instance_entry
        index += 1
        
    assess3 = gen_multi_blocks(multi_size =1, block_size =4, index_of_def = 2)
    for i in range(len(assess3)):
        instance_entry = {'trial_number':index, 'learning_period':'target', 'block_type':'target', 
                          'train_v_assess':'assess' , 'index_of_def_var':2, 'instance':assess3[i][1],
        'val_of_def_var_on_instance':assess3[i][1][2], 'is_cat':target[i][0], 'is_switch': 0 }
        instances_dict[index] = instance_entry
        index += 1
    
    #print(miscon1, assess1, cond, assess2, target)
    
    #full_exp = miscon1 + assess1 + cond + assess2 + target
    
    
    # Maybe outcome block should look like:
    #{'learning_period': ____, 'block_type',}
    # could create a dictionary of dictionaries where main key is trial number, and additional
    # info is trial # 
    #{1:{'trial_number':1, 'learning_period', 'block_type','train_v_assess': , 'index_of_def_var', 'instance',
    #    'val_of_def_var', 'is_cat', 'is_switch', #'response', 'response_correct'}}
    for key in range(index):
        if instances_dict[key]:
            print(key)
            print(instances_dict[key])
            
    # should be 240 entries in dict, last entry = 239, bc index starts at 0
    
    #instances_dict
    

    with open('trials.json', 'w') as file:
        json.dump(instances_dict, file)
    return(instances_dict)
    

def resp_correct(actual, resp):
    if resp == actual:
        return(1)
    else:
        return(0)
    
# then when running exp:
def run_single_subj(subj_id, condition):
    subj = hgf.category_feature_links()
    exp_inst = gen_full_exp(condition)
    subject_trial_dict = {}
    
    subj_id = str(subj_id)
    
    for i in range(240):
        subj_id_trial_num = subj_id + '_' + str(i)
        inst_dict = exp_inst[i]
        trial_inst = inst_dict['instance']
        trial_cat =  inst_dict['is_cat']
        predicted_cat, predicted_val, nbayes_0, nbayes_1 = subj.predict_category(trial_inst)
        response_correct = resp_correct(trial_cat, predicted_cat)
        # if assessment v. miscon == learning: then
        subj.update_links(trial_cat, trial_inst)
        inst_dict['nbayes_0']= nbayes_0 
        inst_dict['nbayes_1']= nbayes_1
        inst_dict['predicted_cat'] = predicted_cat
        inst_dict['predicted_val'] = predicted_val
        inst_dict['response_correct'] = response_correct
        inst_dict['subj_id'] = subj_id
        inst_dict['weights_0'] = subj.get_all_link_weights(0)
        inst_dict['weights_1'] = subj.get_all_link_weights(1)
        inst_dict['condition'] = condition
        
        
        feature_values= subj.get_all_link_weights(predicted_cat)
        
        for i in range(len(trial_inst)):
             feature_num_key = 'feature_at_index{num}'.format(num = i)
             feature_value_key = 'feature_value_at_index{num}'.format(num = i)
             inst_dict[feature_num_key] = trial_inst[i]
             inst_dict[feature_value_key] = feature_values[i]
        
        
        
        subject_trial_dict[subj_id_trial_num] = inst_dict
        print(inst_dict)
        print(subj_id_trial_num)
        
        print(subject_trial_dict)
        
    #for key in range(240):
     #   if [key]:
      #      print(key)
       #     print(subject_trial_dict[key])
        
    with open('trials_and_responses.json', 'w') as file:
        json.dump(subject_trial_dict, file)
    return(subject_trial_dict)

#  feature_values= get_all_link_weights(self, cat)
# 
     #    for i in range(len(inst)):
 #            feature_num_key = 'feature_at_index {num}'.format(num = i)
  #           feature_value_key = 'feature_value_at_index {num}'(num = i)
   #          inst_dict[feature_num_key] = trial_inst[i]
    #         inst_dict[feature_value_key] = feature_values[i]
             
             # '{first} {last}'.format(first='Hodor', last='Hodor!')
             

             
def run_all_subj(num_sub_per_cond, conditions =['lo_var_lo_vol', 
                                                'hi_var_lo_vol',
                                                'lo_var_hi_vol',
                                                'hi_var_hi_vol']):
    
    full_experiment_d = {}
    for condition in conditions:
        for j in range(num_sub_per_cond):
            subj_responses = run_single_subj(j, condition)
            for key in subj_responses:
                cond_subj_trial_id = condition + '_' + str(j)+'_'+str(key)
                full_experiment_d[cond_subj_trial_id] = subj_responses[key]
    
            
    with open('full_experiment.json', 'w') as file:
        json.dump(full_experiment_d, file)
    
    return(full_experiment_d)
    
    
    
    
    

