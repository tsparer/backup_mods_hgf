#import category_and_learner_objects_3 as cl
import update_object_2_2 as u_o  # note the change in the update object normally is update_object_2_2
import numpy
import random
import bisect
import math



### This module contains the functions for constructing the links between a single category
### and a collection of features.  The category_feature_links object also contains code
### for predicting category membership based on available features
### and updating the strength of the links, given feedback.
### The first portion of this module is primarily housekeeping functions which are then used
### by the category_feature_link object.


def multiply_list(array):
    prod = 1
    for i in range(len(array)):
        #print ("current product is")
        #print (prod)
        #print ("multiplied by")
        #print (array[i])
        #print ("\n\n")
        prod = array[i]* prod

    #print(" \n product is")
    #print (prod)
    #print ("\n")

    if prod == 0:
        prod = (1 * (10**(-200))  )

    return prod



def gibbs_sample(weighted_list):

    i_sum = 0
    for i in range(len(weighted_list)):
        i_sum = i_sum + weighted_list[i]

    comparison = random.random()
    i = 0
    while comparison > 0:
        comparison = comparison - weighted_list[i]
        if comparison < 0:
            return_position_and_value = [i, weighted_list[i]]
            return return_position_and_value
        else:
            i = i + 1

def gibbs_sample_2(val_1, val_1_name, val_2, val_2_name):

    denom = val_1 + val_2
    num_1 = val_1/denom
    num_2 = val_2/denom

    test_value = random.random()

    if test_value <= num_1:
        return val_1_name
    else:
        return val_2_name

    





    


###############################

class category_feature_links:

    def __init__ (self, cat_name, num_feat, num_val,

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

        self.active_links = [[0.0 for j in range(num_val)]for j in range(num_feat)]



        self.mu_hat_1_k_min_1 = mu_hat_1_k_min_1
        
        self.mu_2_k_min_1  = mu_2_k_min_1
        self.sig_2_k_min_1 = sig_2_k_min_1
        
        self.mu_3_k_min_1 =  mu_3_k_min_1
        self.sig_3_k      =  sig_3_k

        self.kappa =  kappa
        self.omega =  omega


        self.HGF_feat_and_val_list = [0.0 for i in range(num_feat)]   # number of objects to generate = # of features in instance.


        for i in range(self.num_feat):
            val_list_HGF = [0.0 for j in range(self.num_val)]         # generates an update object for each value(j) in feature(i).
            for j in range(num_val):
                link_name ='{0},{1}'.format(i,j)
                val_list_HGF[j] = u_o.update_single(link_name, mu_2_k_min_1,
                                            sig_2_k_min_1, mu_hat_1_k_min_1, mu_3_k_min_1,
                                                kappa, omega,sig_3_k )

            self.HGF_feat_and_val_list[i] = val_list_HGF


    def create_links(self, mu_2_k_min_1, sig_2_k_min_1, mu_hat_1_k_min_1,
             mu_3_k_min_1, kappa, omega, sig_3_k):


        
            self.mu_hat_1_k_min_1 = mu_hat_1_k_min_1
            
            self.mu_2_k_min_1  = mu_2_k_min_1
            self.sig_2_k_min_1 = sig_2_k_min_1
            
            self.mu_3_k_min_1 =  mu_3_k_min_1
            self.sig_3_k      =  sig_3_k

            self.kappa =  kappa
            self.omega =  omega


            self.HGF_feat_and_val_list = [0.0 for i in range(num_feat)]   # number of objects to generate = # of features in instance.

    
            for i in range(self.num_feat):
                val_list_HGF = [0.0 for j in range(self.num_val)]         # generates an update object for each value(j) in feature(i).
                for j in range(num_val):
                    link_name ='{0},{1}'.format(i,j)
                    val_list_HGF[j] = u_o.update_single(link_name, mu_2_k_min_1,
                                                sig_2_k_min_1, mu_hat_1_k_min_1, mu_3_k_min_1,
                                                    kappa, omega,sig_3_k )

                self.HGF_feat_and_val_list[i] = val_list_HGF

            #print (self.HGF_feat_and_val_list)

                #return?

                # check this list of lists?

    def get_value_weight_list(self, list_of_values):

    # returns a list of (inferred) feature weights for a list of update objects

        list_len = len(list_of_values)
    
        value_weight_list = [0.0 for i in range (list_len) ]

        for i in range(list_len):
            weight = list_of_values[i].get_mu_predicted()
            value_weight_list[i] = weight

        return value_weight_list


        

    def get_all_link_weights(self):

        list_of_link_weights = []

        for i in range(self.num_feat):
            current_feat = self.HGF_feat_and_val_list[i]
            #print ("this is current feature weights {0}".format(current_feat))
            link_strength_for_value_of_current_feature = self.get_value_weight_list(current_feat)

     
            list_of_link_weights.append(link_strength_for_value_of_current_feature)

        return  list_of_link_weights

    ############################################
    ############################################

    def get_dynamic_parameters_for_individual_values_in_feature(self, list_of_values):

    # returns a list of (inferred) feature weights for a list of update objects

        list_len = len(list_of_values)
    
        dynamic_parameter_list = [0.0 for i in range (list_len) ]

        for i in range(list_len):
            dynamic_parameters = list_of_values[i].get_dynamic_parameter_values()
            #print ("here are the dynamic parameters, looped from the cat_link obj")
            #print (dynamic_parameters)
            dynamic_parameter_list[i] = dynamic_parameters

        return dynamic_parameter_list


    def get_dynamic_parameters_for_all_links(self):

        list_of_dynamic_parameters = []

        for i in range(self.num_feat):
            current_feat = self.HGF_feat_and_val_list[i]
            #print ("this is current feature weights {0}".format(current_feat))
            dynamic_parameters_for_values_of_current_feature =  (
            self.get_dynamic_parameters_for_individual_values_in_feature(current_feat)
            )

            #if i == 0:
            #    print (dynamic_parameters_for_values_of_current_feature)

     
            list_of_dynamic_parameters.append(dynamic_parameters_for_values_of_current_feature)

            #print ("this is the list of parameters from the category link objects")
            #print (list_of_dynamic_parameters)
            
        return  list_of_dynamic_parameters

#####################################################

    def activate_links(self, inst):

        all_link_weights = self.get_all_link_weights()
        

        
        #print("this is instance")
        #print(inst)

        active_link_values = []
        for i in range (self.num_feat):
            feat           = inst[i]
#            print("this is current feature {0}".format(feat))
            links_for_feat = all_link_weights[i]
            

            for j in range(self.num_val):
                if feat[j] == 1:
                    active_link_values.append(links_for_feat[j])
                    self.active_links[i][j] = links_for_feat[j]

                else:
                    self.active_links[i][j] = 0

        #print ("all link weights")
        #print (all_link_weights)

        #print("links currently active")
        #print(self.active_links)

        return active_link_values
                
    def predict_category(self, inst):

        active_link_weights = self.activate_links(inst)
        weight_product      = multiply_list(active_link_weights)
        category_strength   = weight_product * self.c_prior

        return category_strength


    


    
    def update_links(self,feedback):

        #print ("feedback is")
        #print (feedback)

        for i in range(self.num_feat):
            #print ("\n \n \nfeature is")
            #print (i)
            for j in range(self.num_val):

#                print ("value is")
#                print (j)
#                print ("\n \n \n ")
                if self.active_links[i][j] > 0:
                    #print ("\n\n feature being updated is")
                    #print (i)
                    #print ("value being updated is")
                    #print (j)
                    #print (" (feedback) value being used for updating is")
                    #print (feedback)
                    self.HGF_feat_and_val_list[i][j].update(feedback)
                    





########################################################################################







#########################################################################################






class multi_category_learner:

    def __init__(self, number_of_categories, number_of_features, number_of_values):

        self.num_cat  = number_of_categories
        self.num_feat = number_of_features
        self.num_val  = number_of_values

        self.all_dynamic_parameters = []

        self.list_of_cat_and_links = [0 for i in range (number_of_features)]

        for i in range(number_of_categories):

            self.list_of_cat_and_links[i] = category_feature_links(i,number_of_features,
                                                                    number_of_values)



    def set_feature_value_strengths_and_piors_for_categories( mu_2_k_min_1,
            sig_2_k_min_1,  mu_hat_1_k_min_1, mu_3_k_min_1, kappa, omega, sig_3_k ):

        

        for i in range(self.num_cat):
            self.list_of_cat_and_links[i].create_links( mu_2_k_min_1,
                    sig_2_k_min_1,mu_hat_1_k_min_1, mu_3_k_min_1, kappa, omega, sig_3_k )


    def create_weighted_categories(self, inst):
        
        category_weights  = []
        for i in range(self.num_cat):
            
            current_cat_weight = self.list_of_cat_and_links[i].predict_category(inst)
            category_weights.append(current_cat_weight)

        #print (category_weights)
        

        self.category_weights = category_weights


    def select_category(self):

        sum_i = 0
        normalized_weights = []
        for i in range(len(self.category_weights)):
            sum_i = sum_i + self.category_weights[i]

        for i in range(len(self.category_weights)):
            normalized_weight = self.category_weights[i]/sum_i
            normalized_weights.append(normalized_weight)

        #print("normalized weights")
        #print (normalized_weights)

        self.selected_cat_and_weight = gibbs_sample(normalized_weights)

        self.selected_cat = self.selected_cat_and_weight[0]

        selected_cat = self.selected_cat_and_weight[0]

        return selected_cat

    def categorize_instance(self, instance):
        
        self.create_weighted_categories(instance)
        category_chosen = self.select_category()
        #print ("chosen category is")
        #print (category_chosen)
        return category_chosen

    def process_feedback(self, actual_category, feedback, feedback_type = 'category'):

        self.list_of_cat_and_links[self.selected_cat]


        #print ("\n\n category being updated is")
        #print (self.selected_cat)
        #print ("actual category is")
        #print (actual_category)
        #print(" feedback is")
        #print (feedback)
        
        

        if actual_category == 'none':
#            print("this is the feedback to be processed")
#            print (feedback)
            self.list_of_cat_and_links[self.selected_cat].update_links(feedback)

        else:
            if feedback == self.selected_cat:
                feedback = 1
            else:
                feedback = 0
                
            self.list_of_cat_and_links[self.selected_cat].update_links(feedback)

    def check_dynamic_parameters_for_all_categories(self):
        
        all_parameters = []
        
        for i in range(self.num_cat):
            current_cat = self.list_of_cat_and_links[i]
            new_parameter_values = current_cat.get_dynamic_parameters_for_all_links()
            all_parameters.append(new_parameter_values)

        self.all_dynamic_parameters = all_parameters


    def get_dynamic_parameters_for_all_categories(self):

        all_parameters = self.all_dynamic_parameters

        return all_parameters

        
            
            
            
    

        
            


    
















            
