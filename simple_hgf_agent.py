# Set link weights
# Predict Category
# Update Link weights
# select category

#import category_and_learner_objects_3 as cl
import update_object_2_2 as u_o  # note the change in the update object normally is update_object_2_2
import numpy
import random
import bisect
import math
import itertools
from functools import reduce



class category_feature_links:

    def __init__ (self, cat_name = "resistant", num_feat = 4, num_val = 2,

                        mu_2_k_min_1=   0,
                        sig_2_k_min_1   = 1,
                        mu_hat_1_k_min_1= .1,
                        mu_3_k_min_1    = .1,
                        kappa           = 1.8,
                        omega           = 2.2,
                        sig_3_k         = .5
                  ):

        self.cat_name = cat_name
        self.num_feat = num_feat
        self.num_val  = num_val

        self.c_prior  = .5

        self.active_links = [0.0 for j in range(num_feat)]



        self.mu_hat_1_k_min_1 = mu_hat_1_k_min_1
        
        self.mu_2_k_min_1  = mu_2_k_min_1
        self.sig_2_k_min_1 = sig_2_k_min_1
        
        self.mu_3_k_min_1 =  mu_3_k_min_1
        self.sig_3_k      =  sig_3_k

        self.kappa =  kappa
        self.omega =  omega


        #self.HGF_val_list = [0.0 for i in range(num_feat)]   # number of objects to generate = # of features in instance.

#TO DO:  CHANGE THIS BINARY update Scheme
        self.HGF_val_list_0 = [0.0 for i in range(self.num_feat)] # generates an update object for each feature(i)
        for i in range(self.num_feat):
  
            link_name = i
            self.HGF_val_list[i] = u_o.update_single(link_name, mu_2_k_min_1,
                                            sig_2_k_min_1, mu_hat_1_k_min_1, mu_3_k_min_1,
                                                kappa, omega,sig_3_k )
            print(self.HGF_val_list[i])
            print(self.HGF_val_list)

        self.HGF_val_list_1 = [0.0 for i in range(self.num_feat)] # generates an update object for each feature(i)
        for i in range(self.num_feat):
  
            link_name = i
            self.HGF_val_list_1[i] = u_o.update_single(link_name, mu_2_k_min_1,
                                            sig_2_k_min_1, mu_hat_1_k_min_1, mu_3_k_min_1,
                                                kappa, omega,sig_3_k )
            



    def get_all_link_weights(self, cat):
        if cat_type == 0:
            update_ob_to_use = self.HGF_val_list_0
        else:
            update_ob_to_use = self.HGF_val_list_1

        hgf_weights_list = self.update_ob_to_use
        list_of_link_weights = []

        for i in range(self.num_feat):
            current_feat = update_ob_to_use[i]
            link_strength_for_current_feature = current_feat.get_mu_predicted()
            list_of_link_weights.append(link_strength_for_current_feature)

        return  list_of_link_weights

    def activate_links(self, inst):
        # multiply each feature in an instance by it's value, adjust for zero
        if cat_type == 0:
            update_ob_to_use = self.HGF_val_list_0
        else:
            update_ob_to_use = self.HGF_val_list_1
        

        weights = self.get_all_link_weights()
        print("weights")
        print(weights)
        predicted_link_activations =[]

        for i, val in enumerate(inst):
            link_value = weights[i]
            if val == 1:
                predicted_value = link_value
            elif val == 0:
                predicted_value = 1 - link_value

            predicted_link_activations.append(predicted_value)

        return predicted_link_activations



    def update_links(self,cat_type, feedback):
        if cat_type == 0:
            update_ob_to_use = self.HGF_val_list_0
        else:
            update_ob_to_use = self.HGF_val_list_1
            
        for i in range(self.num_feat):
            update_ob_to_use[i].update(feedback)

                # DOUBLE CHECK THIS- currently it's taking in kind of a co-occurence string, not actually the instance observed

                # To calculate the co-occurence between the category label and the answer, which is I think what I actually want
                   # use:

    def gibbs_sample_2(val_1, val_1_name, val_2, val_2_name):

        denom = val_1 + val_2
        num_1 = val_1/denom
        num_2 = val_2/denom

        test_value = random.random()

        if test_value <= num_1:
            return val_1_name
        else:
            return val_2_name
    


    def predict_category(self, inst):

        for i in inst:
            if i == 0:
                i = .00001

        nbayes_1 = reduce(lambda x, y: x*y, [1,2,3,4,5,6])
        nbayes_0 =
        


# Need to make two update objects, only update the
        
        
        

        
  # Add prediction functions in the above class-

  

def test(inst = [0,1,1,1], fb= 0):
    
    hgf_agent = category_feature_links()
    print(hgf_agent.HGF_val_list)
    active_vals = hgf_agent.activate_links(inst)
    print("active vals")
    print(active_vals)
    hgf_agent.update_links(fb)
    active_vals = hgf_agent.activate_links(inst)
    print("active vals")
    print(active_vals)
    hgf_agent.update_links(fb)
    active_vals = hgf_agent.activate_links(inst)
    print("active vals")
    print(active_vals)
    hgf_agent.update_links(fb)
    active_vals = hgf_agent.activate_links(inst)
    print("active vals")
    print(active_vals)

    





def gen_instances(length):
    instances_s = ["".join(seq) for seq in itertools.product("01", repeat=length)]
    instances = [[int(i) for i in list(elem)] for elem in binl]


def assign_category(index_of_feat, l_instances):
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
        
    


def block(size = 4):
    instances = gen_instances(size)
    c_insts = assign_category(instances)

    hgf_agent = category_feature_links()
    print(hgf_agent.HGF_val_list)

    for i in range len(c_insts):
        c_inst =numpy.random.choice(c_insts, replace = False)
        cat = c_insts[0]
        inst = c_insts[1]

        #predict cat
        #log prediction
        #get values
        #update predictions
        # cat_given .update_links(feedback):

######
        Fini
# Above is only one block- remember, there are 4 blocks per learning period, and 3 overall periods

# to create high variability blocks, swap the diagnostic conditions between two

# To do today- add Gibbs sampler, rewrite funcs to pull info
        

        



    
    active_vals = hgf_agent.activate_links(inst)
    print("active vals")
    print(active_vals)
    hgf_agent.update_links(fb)
    active_vals = hgf_agent.activate_links(inst)

        
    
