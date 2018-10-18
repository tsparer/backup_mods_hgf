import random
import math
from decimal import *
import file_formatting
import Category_and_instance_generator   as Cig
import Category_link_objects_binary_gibbs_Dec_9_2015 as Clo

# sets categories + category definition

# creates learner object

# sets "single participant, experiment condition"

# runs experiment


def make_csv(l1, file_name):

    file = open(file_name, 'a')

    for i in range(len(l1)):
        data = str(l1[i])

        file.write(data)
        file.write(', ')


    file.write('\n')
    file.close()
        


def response_correct(actual_value, response):
    if actual_value == response:
        return 1
    else:
        return 0


class single_participant_experiment:

    def __init__(self, num_cat, num_feat, num_val):

        self.num_cat  = num_cat
        self.num_feat = num_feat
        self.num_val  = num_val
        self.learner = Clo.multi_category_learner(self.num_cat, self.num_feat, self.num_val)
        self.list_of_all_dynamic_parameter_values = []

        for i in range(num_cat):
            place_holder = []
            self.list_of_all_dynamic_parameter_values.append(place_holder)


        self.trial_by_trial_parameter_results = []
        self.trial_by_trial_results = []
        


    def set_categories_and_feat_link_parameters(self, category_def_string, num_feat, num_val):

        #self.cat_def = category_def_string
        self.num_feat = num_feat
        self.num_val  = num_val
       
        
       
    def set_learner_priors(self, mu_2_k_min_1,
            sig_2_k_min_1,  mu_hat_1_k_min_1, mu_3_k_min_1, kappa, omega, sig_3_k):

            self.mu_hat_1_k_min_1 = mu_hat_1_k_min_1
            
            self.mu_2_k_min_1  = mu_2_k_min_1
            self.sig_2_k_min_1 = sig_2_k_min_1
            
            self.mu_3_k_min_1 =  mu_3_k_min_1
            self.sig_3_k      =  sig_3_k

            self.kappa =  kappa
            self.omega =  omega

    def create_learner(self):

            self.learner = Clo.multi_category_learner(self.num_cat, self.num_feat, self.num_val)

            self.learner.set_feature_value_strengths_and_piors_for_categories(

                                                                        self.mu_hat_1_k_min_1, 
                            
                                                                        self.mu_2_k_min_1,  
                                                                        self.sig_2_k_min_1, 
                                                                            
                                                                        self.mu_3_k_min_1,
                                                                        self.sig_3_k,      

                                                                        self.kappa, 
                                                                        self.omega
                                                                        )
           
    

    def create_list_of_categories(self, number_of_categories, list_of_cat_defs):
        
        self.category_list =[]
        number_of_categories

        for i in range(number_of_categories):
            new_cat = Cig.category(i, list_of_cat_defs[i], self.num_feat, self.num_val)
            self.category_list.append(new_cat)

    def get_modifiable_cat_from_list(index_of_cat):

        return self.category_list[index_of_cat]

    def update_list_of_dynamic_parameters(self):
        self.learner.check_dynamic_parameters_for_all_categories()

    def get_all_dynamic_parameters_for_all_categories(self):
        all_parameters = self.learner.get_dynamic_parameters_for_all_categories()
        #print ("all parameters from all parameter function in exp/learner class")
        #print (all_parameters)

        return all_parameters
        
        

    def single_trial(self, index_of_cat_to_use, trial_number = 0):

        

        inst_will_be_in_cat_or_not = random.randint(0,1)
            
        if inst_will_be_in_cat_or_not   == 1:
            inst = self.category_list[index_of_cat_to_use].gen_inst_of_cat()
            correct_cat = 1
            #print (" \n\n correct cat")
            #print (correct_cat)
            
        elif inst_will_be_in_cat_or_not ==  0:
            inst = self.category_list[index_of_cat_to_use].gen_inst_not_in_cat()
            correct_cat = 0

            #print ("\n\n correct cat")
            #print (correct_cat)

        response = self.learner.categorize_instance(inst)

        #print("response was")
        #print (response)


        was_response_correct = response_correct(correct_cat, response)

        #print("response was correct?")
        #print (was_response_correct)
        #print("\n\n")

        self.learner.process_feedback("none", was_response_correct)

        self.update_list_of_dynamic_parameters()

        current_parameters = self.get_all_dynamic_parameters_for_all_categories()

        trial_results_data = [trial_number, correct_cat, response, was_response_correct]
        
        #print (current_parameters)

        # pull parameter values here

        trial_parameter_results = current_parameters

        self.trial_by_trial_parameter_results.append(trial_parameter_results)
        self.trial_by_trial_results.append(trial_results_data)

        ###############
        

        return was_response_correct

 ###########################################################################

 # functions for running a single simulated participant  ###
 ###############################################################

def windowed_average_response(response_list):

    sum_i = 0
    for i in range(len(response_list)):
        sum_i = sum_i + respons_list[i]

    average = sum_i/len(response_list)

    return average



        
            
        

def simulate_single_participant_full_experiment(trials, switch, num_cat, num_feat, num_val,
                                                cat_def_list,   block_size,
                                                mu_2_k_min_1, sig_2_k_min_1,
                                                mu_hat_1_k_min_1, mu_3_k_min_1, kappa,
                                                omega, sig_3_k):

        getcontext().prec = 8

        mu_2_k_min_1     = Decimal(mu_2_k_min_1)
        sig_2_k_min_1    = Decimal(sig_2_k_min_1)
        mu_hat_1_k_min_1 = Decimal(mu_hat_1_k_min_1)
        mu_3_k_min_1     = Decimal(mu_3_k_min_1)

        kappa           = Decimal(kappa)
        omega           = Decimal(kappa)
        sig_3_k         = Decimal(kappa)
        
        
        

        experiment_and_learner = single_participant_experiment( num_cat, num_feat, num_val)
        experiment_and_learner.set_learner_priors(mu_2_k_min_1, sig_2_k_min_1,
                                      mu_hat_1_k_min_1, mu_3_k_min_1, kappa,
                                      omega, sig_3_k)
        experiment_and_learner.create_list_of_categories(num_cat, cat_def_list)
        
        
        consistent_response_list = []
        for i in range(trials):

            print (i)

            if i < switch:
                
                def_to_use = 0
                response_consistent = experiment_and_learner.single_trial(0, i)
                consistent_response_list.append(response_consistent)

            else:
                def_to_use = 1
                response_consistent = experiment_and_learner.single_trial(1, i)
                consistent_response_list.append(response_consistent)

        #print (consistent_response_list)

 #       for i in range(trials):

            #seperates responses into blocks of a given size
 #           block_list = []
#            new_block  = []
#            for i in range(trials):
#                
#                break_point = consistent_response_list[i] % block_size
#                print (i)
#                print (block_list)
#                print (new_block)
#                if break_point == 0:
##                    new_block = []
#                    new_block.append(consistent_response_list[i])
#
#                else:
#                    new_block.append(consistent_response_list[i])
#
#        del block_list[0]

        #averages the score for each block
#        block_average_list = []
#        for i in range(len(block_list)):
#            window_average = windowed_average_response(block_list[i])
#            block_average.append(window_average)

    

#        make_csv(block_average_list)

        all_trial_parameter_results = experiment_and_learner.trial_by_trial_parameter_results

        print ("these are the all trial parameter results")
        #print (all_trial_parameter_results)

        file_formatting.make_output_file(
            all_trial_parameter_results, 'model_results.txt', num_cat, num_feat, num_val, 6)

            # 6 = number of parameters

        

        print ("consistent response lists")
        print (consistent_response_list)
        return consistent_response_list
        

def run_participant(

    trials          = 100,
    switch          = 50,
    num_cat         = 2,
    num_feat        = 6,
    num_val         = 2,
    cat_def_list    = [    [ [0,1],['n','n'],['n','n'],['n','n'],['n','n'],['n','n']  ],
                           [  ['n','n'],[0,1],['n','n'],['n','n'],['n','n'],['n','n'] ]    ],
    block_size      = 10,
    
    mu_2_k_min_1    =  0.000000,
    sig_2_k_min_1   =  1.000000,
    mu_hat_1_k_min_1= .1000000,
    mu_3_k_min_1    = .1000000,

    kappa           = 2.840000,
    omega           = -8.000000,
    sig_3_k         = .00001 
    
    #kappa           = 2.840000,
    #omega           = -4.000000,
    #sig_3_k         = .0019
    ):


                       

    

   results = simulate_single_participant_full_experiment(trials, switch, num_cat, num_feat,
                                                num_val, cat_def_list,   block_size,
                                                mu_2_k_min_1, sig_2_k_min_1,
                                                mu_hat_1_k_min_1, mu_3_k_min_1, kappa,
                                                omega, sig_3_k)

   return results
    


    # empirical starting values from HGF paper
    # mu_2_k_min_1    =  0.000000,
    # sig_2_k_min_1   =  1.000000,
    # mu_hat_1_k_min_1= .1000000,
    # mu_3_k_min_1    = .1000000,
    
    # kappa           = 2.840000,
    # omega           = -4.000000,
    # sig_3_k         = .0019000 ):
        
