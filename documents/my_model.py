'''
##TODO

'''
import pandas as pd
import argparse

def parse_files():
    '''
    ##TODO
    '''

    parser = argparse.ArgumentParser( description ='Viewing the contents of jobs.csv')
    parser.add_argument("-file", type = int, help="This will display the contents of the file depending on the number: 1-Jobs(displays Jobs)\n 2-Applicants(displays Applicants) \n 3-Both Jobs and Applicants(displays both Jobs and Applicants)")
    args = parser.parse_args()    

    if args.file == 1:
        print("\n")
        print(jobs)
        print("\n")
    elif args.file == 2:
        print("\n")
        print(applicants)
        print("\n")
    elif args.file == 3:
        print("\n")
        print(jobs)
        print("\n")
        print(applicants)
        print("\n")
        
    ## TODO
    applicants_file ='applicants.csv'
    jobs_file = 'jobs.csv'
    assig_method = 'naive'
    return applicants_file, jobs_file, assig_method

def load_applicants(applicants_file):
    '''
    ## TODO
    '''
    
    applicants = pd.read_csv (applicants_file)
    return applicants
    
def load_jobs(jobs_file):
    '''
    ## TODO
    '''

    jobs = pd.read_csv (jobs_file)
    return jobs


def main():
    '''
    ##TODO
    '''
    
    applicants_file, jobs_file = parse_files()
    
    applicants = load_applicants('applicants.csv')
    jobs =load_jobs('jobs.csv')

    print(jobs)
    print("\n")
    print(applicants)

if __name__=='__main__':
    main()