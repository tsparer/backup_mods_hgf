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



# possible values to use:
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4237059/
# 2014
# Uncertainty in perception and the Hierarchical Gaussian Filter
#kappa           = 2.49,
#omega           = .0006,
#sig_3_k         = .998
#  
# https://www.sciencedirect.com/science/article/pii/S0896627313008076
# Hierarchical Prediction Errors in Midbrain and Basal Forebrain during Sensory Learning
# 2013 (see papers supplementary methods for estimates from other experiments)
#Model/param Mean       SD       Mean exp 2            
#HGF1
#θ      0.0019         0.0017    0.710
#κ      2.835          0.0022    2.963
#ω      -4 0 -4 0      0.0016     0.702
#ζ      2.141           1.132 1.680 0.741

 


class category_feature_links:

    def __init__ (self, cat_name = "resistant", num_feat = 4, num_val = 2,

                        mu_2_k_min_1=   0,
                        sig_2_k_min_1   = 1,
                        mu_hat_1_k_min_1= .5,
                        mu_3_k_min_1    = 1,
                        kappa           = 2.835,
                        omega           = -4,
                        sig_3_k         = .0019
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
            self.HGF_val_list_0[i] = u_o.update_single(link_name, mu_2_k_min_1,
                                            sig_2_k_min_1, mu_hat_1_k_min_1, mu_3_k_min_1,
                                                kappa, omega,sig_3_k )

        self.HGF_val_list_1 = [0.0 for i in range(self.num_feat)] # generates an update object for each feature(i)
        for i in range(self.num_feat):
            link_name = i
            self.HGF_val_list_1[i] = u_o.update_single(link_name, mu_2_k_min_1,
                                            sig_2_k_min_1, mu_hat_1_k_min_1, mu_3_k_min_1,
                                                kappa, omega,sig_3_k )
            



    def get_all_link_weights(self, cat):
        if cat == 0:
            update_ob_to_use = self.HGF_val_list_0
        else:
            update_ob_to_use = self.HGF_val_list_1

        hgf_weights_list = update_ob_to_use
        list_of_link_weights = []

        for i in range(self.num_feat):
            current_feat = update_ob_to_use[i]
            link_strength_for_current_feature = current_feat.get_mu_predicted()
            list_of_link_weights.append(link_strength_for_current_feature)

        return  list_of_link_weights
    
    def is_consistent(self, inst, cat):
        consistent_list = []
        for i in inst:
            if i == cat:
                consistent_list.append(1)
            else:
                consistent_list.append(0)
        print("inst v consistent")
        print (cat)
        print (inst)
        print(consistent_list)
        return(consistent_list)

    def predict_cat_per_feature(self, inst, cat):
        # multiply each feature in an instance by it's value, adjust for zero
        # returns the list of "predictions" for given each feature in the instance
        # Map consistency
        if cat == 0:
            update_ob_to_use = self.HGF_val_list_0
        else:
            update_ob_to_use = self.HGF_val_list_1
        
        weights = self.get_all_link_weights(cat)
        print("predictions for cat")
        print(cat)
        print("weights")
        print(weights)
        predicted_link_activations =[]

        for i, val in enumerate(inst):
            link_value = weights[i]
         #   print (link_value)
            if val == 1:
                predicted_value = link_value
            elif val == 0:
                predicted_value = 1 - link_value

            predicted_link_activations.append(predicted_value)
        print("predicted activations")
        print(predicted_link_activations)

        return predicted_link_activations



    def update_links(self, cat_type, inst):  # I think I can remove feedback (Refactor)
        if cat_type == 0:
            update_ob_to_use = self.HGF_val_list_0
        elif cat_type == 1:
            update_ob_to_use = self.HGF_val_list_1
            
        
            
        for i in range(self.num_feat):
            update_ob_to_use[i].update(inst[i])

                # DOUBLE CHECK THIS- currently it's taking in kind of a co-occurence string, not actually the instance observed

                # To calculate the co-occurence between the category label and the answer, which is I think what I actually want
                   # use:

    def gibbs_sample_2(self, val_1, val_1_name, val_2, val_2_name):

        denom = val_1 + val_2
        if denom == 0:
            return('denom is zero', .5)
        num_1 = val_1/denom
        num_2 = val_2/denom

        test_value = random.random()

        if test_value <= num_1:
   #     if num_1 >= num_2:
            return (val_1_name, num_1)
        else:
            return (val_2_name, num_2)
    
    def remove_0s(self, inst):
        for i in range(len(inst)):
            if inst[i] <= .0000000001:
                inst[i] = .0000000001
        return inst

    def predict_category(self, inst):
        pred_0_list= self.predict_cat_per_feature(inst, 0)
        pred_0_list = self.remove_0s(pred_0_list)
        pred_1_list = self.predict_cat_per_feature(inst, 1)
        pred_1_list = self.remove_0s(pred_1_list)
        
        print("predicted 0 list")
        print(pred_0_list)
        


        nbayes_0 = reduce(lambda x, y: x*y, pred_0_list )
        nbayes_1 = reduce(lambda x, y: x*y, pred_1_list )
        print(nbayes_0)
        print(nbayes_1)
        pred_name, pred_val =self.gibbs_sample_2(nbayes_0, 0, nbayes_1, 1)
        self.most_recent_pred_name = pred_name
        self.most_recent_pred_cat =  pred_val
        
        return(pred_name, pred_val, nbayes_0, nbayes_1)
        


# Need to make two update objects, only update the
        
        
        

        
  # Add prediction functions in the above class-

  

def test(inst = [0,1,1,1], fb= 0):
    
    hgf_agent = category_feature_links()
    
    print(hgf_agent.HGF_val_list_0)
    print(hgf_agent.HGF_val_list_1)
    print("active vals for 0")
    links_0 = hgf_agent.get_all_link_weights(0)
    print(links_0)
    print("active vals for 1")
    links_1 = hgf_agent.get_all_link_weights(1)
    print(links_1)
    prediction, value = hgf_agent.predict_category(inst)
    print (prediction, value)
    hgf_agent.update_links(fb, inst)
    hgf_agent.update_links(fb, inst)
    
    print("/n \n post updat /n \n")
    
       
    print("active vals for 0")
    links_0 = hgf_agent.get_all_link_weights(0)
    print(links_0)
    print("active vals for 1")
    links_1 = hgf_agent.get_all_link_weights(1)
    print(links_1)
    prediction, value = hgf_agent.predict_category(inst)
    print (prediction, value)
    hgf_agent.update_links(fb, inst)
    hgf_agent.update_links(fb,  inst)
    
    print("/n \n post updat /n \n")
    
    print("new inst")
    
    inst = [0,0,0,0]
    print(inst)
    print("active vals for 0")
    links_0 = hgf_agent.get_all_link_weights(0)
    print(links_0)
    print("active vals for 1")
    links_1 = hgf_agent.get_all_link_weights(1)
    print(links_1)
    prediction = hgf_agent.predict_category(inst)
    print (prediction)
    hgf_agent.update_links(fb,  inst)
    hgf_agent.update_links(fb,  inst)
    
    print("maybe last inst")
    inst = [0,0,0,0]
    print(inst)
    print("active vals for 0")
    links_0 = hgf_agent.get_all_link_weights(0)
    print(links_0)
    print("active vals for 1")
    links_1 = hgf_agent.get_all_link_weights(1)
    print(links_1)
    prediction = hgf_agent.predict_category(inst)
    print (prediction)
    hgf_agent.update_links(fb, inst)
    hgf_agent.update_links(fb, inst)
 
   

    
    
    

    





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

    

### Just a test
def experiment_and_agent_block(size = 4):
    instances = gen_instances(size)
    c_insts = assign_category(instances)

    hgf_agent = category_feature_links()
    print(hgf_agent.HGF_val_list)

    for i in range(len(c_insts)):
        c_inst =numpy.random.choice(c_insts, replace = False)
        cat = c_insts[0]
        inst = c_insts[1]
        
    

        #predict cat
        #log prediction
        #get values
        #update predictions
        # cat_given .update_links(feedback):

######

# Above is only one block- remember, there are 4 blocks per learning period, and 3 overall periods

# to create high variability blocks, swap the diagnostic conditions between two

# To do today- add Gibbs sampler, rewrite funcs to pull info
        

        



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
    
    return ({'first_block_var':first_block_var, 
             'distractor_block_var':distractor_block_var})
    
    # take in sequence
    # randomly 
 #   def gen_no_var_no_vol: 
  #  def gen_no_var_vol:
   # def gen

    
    

    

        
    
