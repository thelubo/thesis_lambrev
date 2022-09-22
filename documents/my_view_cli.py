'''
TODO
'''
import my_model
import my_controller

import pandas as pd
import argparse
import itertools
from itertools import permutations
import math 

import numpy as np

import sys



def main():
    '''
    #todo
    '''


    applicants_file, jobs_file, asiig_method =  my_model.parse_files()

    applicants = my_model.load_applicants(applicants_file)
    jobs = my_model.load_jobs(jobs_file)
    
    print(jobs)
    print("\n")
    print(applicants)
    
    if asiig_method == 'naive':
        my_new_df_applicants, my_new_df_jobs = my_controller.get_dicts(applicants, jobs)
        unique_applist, unique_joblist = my_controller.get_unique_lst(my_new_df_applicants, my_new_df_jobs)
        lst = my_controller.get_perm_apps(unique_applist, unique_joblist)
        assignment_list = my_controller.naive_approach(lst,my_new_df_applicants,my_new_df_jobs)
       
    
    print(assignment_list)
    
    ##togo
    #save_csv('assigment_file', assignment_list)
    

if __name__=='__main__':
    main()