import random


def insert_element_randomly_in_list(array, element):

    for i in range(len(array)):
            random_index = random.randint (0, range(len(array) - 1)  )
            features_and_values[i][random_value_for_feature] = element

    


def gen_instance(number_features, number_values):
    
    features_and_values = [[0 for j in range(number_values)] for i in range(number_features)]
                           
    for i in range(number_features):

        random_value_for_feature = random.randint (0, (number_values - 1))
        
        for j in range (number_values):
            if j == random_value_for_feature:
                features_and_values[i][j] = 1
            else:
                features_and_values[i][j] = 0

    return features_and_values



def check_list_contains_elements(element, array):

    #print("array")
    #print (array)
    #print ("element")
    #print (element)

    for i in range(len(array)):
        if array[i] == element:
            return 1
        else:
            pass
    return 0





def define_instance_as_category(instance, category_definition, number_features, number_values):

    #print ("this is the whole category definition")
    #print (category_definition)
    #print ("this is the instance")
    #print (instance)
    #print ("number of features")
    #print (number_features)

    for i in range(number_features):
        #print (i)
        #print ("this is the category definition at this point")
        #print (category_definition)
        val_present_is_used_for_definition = check_list_contains_elements(1, category_definition[i])

        if val_present_is_used_for_definition == 1:
            for j in range(number_values):
                #print (j)
                if category_definition[i][j] == 1:
                    instance[i][j] = 1
                elif category_definition[i][j] == 0:
                    instance[i][j] = 0

            #print("newly made feature")
            #print (instance[i])
        else:
            pass

    return instance

def define_instance_not_as_category(instance, category_definition, number_features, number_values):

    #print ("this is the whole category definition")
    #print (category_definition)
    #print ("this is the instance")
    #print (instance)
    #print ("number of features")
    #print (number_features)
    

    for i in range(number_features):
        #print (i)
        val_present_is_used_for_definition = check_list_contains_elements(1, category_definition[i])
        
        if val_present_is_used_for_definition == 1:
            for j in range(number_values):
                #print(j)
                if category_definition[i][j] == 1:
                    instance[i][j] = 0
                    
                elif category_definition[i][j] == 0:
                    instance[i][j] = 1
                    
                    # note, this is kludged, works ideally for binary defs, but not others?

            #print("this the defining feature and its associated values")
            #print (instance[i]) 
        else:
            pass

    return instance


def evaluate_instance_given_def(instance, category_definition):

    for i in range(number_features):
        val_present_is_used_for_definition = check_list_contains_elemen(1, category_definition[i])

        if val-present_is_used_for_definition == 1:
            for j in range(number_values):
                if category_definition[i][j] == 1:
                    if instance[i][j] != 1:
                        return 0
                    else:
                        pass
                else:
                    pass

    return 1


class category:

    def __init__ (self, name, category_def_string, num_feat, num_val):

        self.name = name
        self.cat_def = category_def_string
        self.num_feat = num_feat
        self.num_val  = num_val

    def gen_inst_of_cat(self):

        #print("instance of category function")

        first_inst = gen_instance(self.num_feat, self.num_val)
        #print (first_inst)
        instance_of_category = define_instance_as_category(first_inst, self.cat_def,self.num_feat, self.num_val)

        self.most_recent_generated_instance = instance_of_category
        
        return instance_of_category

    def gen_inst_not_in_cat(self):

        #print("instance not in category, function")

        first_inst = gen_instance(self.num_feat, self.num_val)
        #print (first_inst)
        instance_of_category = define_instance_not_as_category(first_inst, self.cat_def,self.num_feat, self.num_val)

        self.most_recent_generated_instance = instance_of_category
        
        return instance_of_category


    def evaluate_instance(self, instance):
        inst_is_cat = evaluate_instance_given_def(instance, self.cat_def)
        self.most_recent_evaluated = instance
        return inst_is_cat
        

    def get_cat_name(self):
        cat_name = self.name
        return cat_name

    def get_cat_def(self):
        cat_def = self.cat_def
        return cat_def

    def set_cat_def(self, new_def):
        self.cat_def = new_def
        

    def get_current_generated_instance(self):

        self.most_recent_generated_instance = instance_of_category
        return instance_of_category

    
        

        
        
                









            
    
