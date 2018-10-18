
def make_csv(l1, file_name):

    file = open(file_name, 'a')

    for i in range(len(l1)):
        data = str(l1[i])

        file.write(data)
        file.write(', ')


    file.write('\n')
    file.close()


def make_output_file(trial_list, file_name, num_cat, num_feat, num_val, num_param):

    num_trial = len(trial_list)
    out_file = open(file_name, 'a')

    for trial in range(num_trial):
        out_file.write('\n')

        for cat in range(num_cat):
            for feat in range(num_feat):
                for val in range(num_val):                    
                    for param in range (num_param):

                        param_to_record = trial_list[trial][cat][feat][val][param]
                        param_string    = str(param_to_record)

                        out_file.write(param_string)
                        out_file.write(',  ')

        

    out_file.close()



def make_output_file_w_print_statements(trial_list, file_name, num_cat, num_feat, num_val, num_param):

    num_trial = len(trial_list)
    print ('initial num_trial is')
    print (num_trial)
    
    out_file = open(file_name, 'a')

    for trial in range(num_trial):
        out_file.write('\n')

        print ('num_trials' )
        print (num_trial)
        print ('trial is')
        print (trial)

        for cat in range(num_cat):

            print ('num_cat')
            print (num_cat)
            print ('cat is')
            print (cat)
            
            for feat in range(num_feat):

                print('num_feat')
                print(num_feat)
                print ('feat is')
                print (feat)
                
                for val in range(num_val):

                    print('num_val')
                    print(num_val)
                    print ('val is')
                    print (val)
                    
                    
                    for param in range (num_param):

                        print('num_param')
                        print(num_param)
                        print('param is')
                        print(param)

                        print (trial_list[trial][cat][feat][val][param])

                        param_to_record = trial_list[trial][cat][feat][val][param]
                        param_string    = str(param_to_record)

                        out_file.write(param_string)
                        out_file.write(',  ')

        print ('\n\n')

    out_file.close()



def test():
    
    file_name = 'test_file'
    #note additional parameter included to specify feat etc.
    
    num_cat    = 2
    num_feat   = 2
    num_val    = 2
    num_param  = 7


    trial_list = (
        [
            #trial 1
            [
                #cat 1
                [
                    #feat 1
                    [
                        #val 1
                        [
                            #parameters
                             ['t1, c1, f1, v1'] ,['f11'],['f12'],[3],[4],[5],[6] 
                        ],
                        
                        #val 2
                        [
                            #parameters
                            ['t1, c1, f1, v2' ],[7],[8],[9],[10],[],[11] 
                        ]
                    ],

                    #feat 2
                    [
                        #val 1
                        [
                            #parameters
                            ['t1, c1, f2, v1' ],[12],[13],[14],[15],[16],[17] 
                        ],
                        
                        #val 2
                        [
                            #parameters
                            ['t1, c1, f2, v2' ],[18],[19],[20],[21],[22],[23] 
                        ]
                    ]
                ],
                
                #cat 2
                [
                    #feat 1
                    [
                        #val 1
                        [
                            #parameters
                            ['t1, c2, f1, v1' ],[1],[2],[3],[4],[5],[6] 
                        ],
                        
                        #val 2
                        [
                            #parameters
                            ['t1, c2, f1, v2' ],[6],[4],[3],[1],[3],[4] 
                        ]
                    ],

                    #feat 2
                    [
                        #val 1
                        [
                            #parameters
                            ['t1, c2, f2, v1' ],[2],[3],[4],[5],[6],[67] 
                        ],
                        
                        #val 2
                        [
                            #parameters
                            ['t1, c2, f2, v2' ],[1],[2],[3],[4],[5],[6] 
                        ]
                    ]
                ]

            ],

            #trial 2
            [
                #cat 1
                [
                    #feat 1
                    [
                        #val 1
                        [
                            #parameters
                            ['t2, c1, f1, v1' ],[1],[2],[3],[4],[5],[78] 
                        ],
                        
                        #val 2
                        [
                            #parameters
                            ['t2, c1, f1, v2' ],[23],[34],[56],[67],[4],[4] 
                        ]
                    ],

                    #feat 2
                    [
                        #val 1
                        [
                            #parameters
                            ['t2, c1, f2, v1' ],[1],[2],[3],[4],[5],[4] 
                        ],
                        
                        #val 2
                        [
                            #parameters
                            ['t2, c1, f2, v2' ],[1],[1],[1],[1],[1],[1] 
                        ]
                    ]
                ],
                
                #cat 2
                [
                    #feat 1
                    [
                        #val 1
                        [
                            #parameters
                            ['t2, c2, f1, v1' ],[2],[2],[2],[2],[2],[2] 
                        ],
                        
                        #val 2
                        [
                            #parameters
                            ['t2, c2, f1, v2' ],[33],[3],[3],[3],[3],[3] 
                        ]
                    ],

                    #feat 2
                    [
                        #val 1
                        [
                            #parameters
                            ['t2, c2, f2, v1' ],[4],[4],[4],[4],[4],[4] 
                        ],
                        
                        #val 2
                        [
                            #parameters
                            ['t2, c2, f2, v2' ],[5],[5],[5],[5],[5],[5] 
                        ]
                    ]
                ]
            ]
        ]
        )

    make_output_file_w_print_statements(
            trial_list, file_name, num_cat, num_feat, num_val, num_param)

    return 1

                

            

                
                    


                    
                    
    
                        
    
    

    
