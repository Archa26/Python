'''In a university, your attendance determines whether you will be allowed to
attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)",
don't actually divide or reduce the fraction to decimal'''

#import the required modules
from itertools import product

N1=5
N2=10

def find_possible_cases(n):
    '''considering 'A' for Absent and 'P' for present find all possible cases for input 'n' '''
    possible_cases=[ ''.join(roll) for roll in product(['A','P'], repeat = n)]
    # print("Possible number of days for input %d=%d"%(n,len(possible_cases)))
    find_probability(possible_cases,n)

def find_probability(possible_cases,n):
    '''find Probability that student will miss the graduation ceremony'''

    #Number of days were student missed class for 4 or more consecutive days
    absent_days=[s for s in possible_cases if 'AAAA' in s]
    # print("Number of absent days",len(absent_days))

    #Number of ways to attend classes over N days
    ways_to_attend=list(set(possible_cases) - set(absent_days))
    print("1.Number of ways to attend classes over %d days=%d"%(n,len(ways_to_attend)))

    not_attending=[i for i in ways_to_attend if i[-1]=='A']
    print("2.Probability that the student will miss the graduation "
          "ceremony",str(len(not_attending))+"/"+str(len(ways_to_attend)))

find_possible_cases(N1)
print("\n")
find_possible_cases(N2)


