'''

'''
import my_model
import my_controller

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



def main():
    '''
    #todo
    '''
    ## todo get files from streamlit
    applicants_file, jobs_file, asiig_method =  my_model.parse_files()

    applicants = my_model.load_applicants(applicants_file)
    jobs = my_model.load_jobs(jobs_file)
    
    
    my_new_df_applicants, my_new_df_jobs = my_controller.get_dicts(applicants, jobs)
    my_df_applicants = my_new_df_applicants
    my_df_jobs = my_new_df_jobs
    #print(my_new_df_applicants, my_new_df_jobs)
    unique_applist, unique_joblist = my_controller.get_unique_lst(my_new_df_applicants, my_new_df_jobs)
    lst = my_controller.get_perm_apps(unique_applist, unique_joblist)
    
    ###print(naive_approach(lst,my_new_df_applicants,my_new_df_jobs))

    st.title("A software system for automatically selecting suitable candidates according to their qualifications ")
    def home(applicants,jobs,my_df_jobs,my_df_applicants):
        st.header('Home page')
        st.write(applicants,jobs,my_df_jobs,my_df_applicants)
    
    def example_1(my_df_jobs):
        st.header('Example Requirements:')
        st.write(my_df_jobs)
    def applicants_1(my_df_applicants):
        st.header('Example Applicants:')
        st.write(my_df_applicants)
        st.sidebar.title("Navigation")
    options = st.sidebar.radio('Pages',options=['Home','Requirements example','Applicants example',])

    if options == 'Home':
        home(applicants,jobs,my_df_jobs,my_df_applicants)
    elif options == 'Requirements example':
        example_1(my_df_jobs)
    elif options == 'Applicants example':
        applicants_1(my_df_applicants)

    uploaded_file = st.file_uploader('Upload you file here')

    if uploaded_file:
        data=pd.read_csv(uploaded_file)
        st.write(data)
    

if __name__=='__main__':
    main()