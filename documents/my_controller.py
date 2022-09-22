'''

'''
import my_model

import pandas as pd
import argparse
import itertools
from itertools import permutations
import math 
import streamlit as st
import numpy as np
from scipy.optimize import linear_sum_assignment
from munkres import Munkres
import sys

def fitting(lst,my_new_df_app,my_new_df_jobs):
    res_val=0.0 
    for comp in my_new_df_app[lst[0]]:
        mult = my_new_df_app[lst[0]][comp]* my_new_df_jobs[lst[1]][comp]
        if math.isnan(mult):
            mult=0.0
        res_val=res_val + mult
    return res_val


def utility(lst,my_new_df_app,my_new_df_jobs):
    '''
    '''
    res_util=0.0
    for comb in lst:
        res_util=res_util + fitting(comb,my_new_df_app,my_new_df_jobs)
    return res_util

#print(utility)


def naive_approach(lst, my_new_df_app,my_new_df_jobs):
    '''
    '''
    ress=0.0
    for l in lst:
        val=utility(l,my_new_df_app,my_new_df_jobs)
        if val > ress:
            ress=val
            ress_tpl=l
    return [ress,ress_tpl]


def get_unique_lst(my_new_df_applicants, my_new_df_jobs):
    '''
    '''
    unique_applist = sorted(list(set(my_new_df_applicants)))
    unique_joblist =  sorted(list(set(my_new_df_jobs)))
    return unique_applist, unique_joblist

def get_dicts(applicants, jobs):
    '''
    '''
    my_new_df_applicants= applicants.pivot(index='skill name',columns= 'applicant name',values = 'grade').to_dict()
    my_new_df_jobs = jobs.pivot(index='skill name',columns ='job name', values='grade').to_dict()
    
    return my_new_df_applicants, my_new_df_jobs

def get_perm_apps(unique_applist, unique_joblist):
    '''
    '''
    uniq_app_perm =  list(permutations(unique_applist))
    #print(uniq_app_perm)

    lst=[]
    for i in uniq_app_perm:
        lst.append(tuple(zip(i,unique_joblist)))
    #print(lst)
    return lst



def main():
    '''
    #todo
    '''
    applicants_file, jobs_file, asig_method =  my_model.parse_files()

    applicants = my_model.load_applicants(applicants_file)
    jobs = my_model.load_jobs(jobs_file)
    
    print(jobs)
    print("\n")
    print(applicants)
    
    my_new_df_applicants, my_new_df_jobs = get_dicts(applicants, jobs)
    print(my_new_df_applicants, my_new_df_jobs)
    unique_applist, unique_joblist = get_unique_lst(my_new_df_applicants, my_new_df_jobs)
    lst = get_perm_apps(unique_applist, unique_joblist)
    
    print(naive_approach(lst,my_new_df_applicants,my_new_df_jobs))

if __name__=='__main__':
    main()