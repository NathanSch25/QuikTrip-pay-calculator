'''----------------#
Nathan R. Schober  |
02/09/2024         |
pay calculator     |
-----------------'''


from clerk.clerkPT import ClerkPT
from clerk.clerkFT import ClerkFT
from RA.ra import RA
from _2A._2a import A2
from _1A._1a import A1

import time

user = 0
while user != '-1':
    print("-1 end program")
    print("1 PT Clerk calculator")
    print("2 FT Clerk calculator")
    print("3 RA/NA calculator")
    print("4 2A calculator")
    print("5 1A calculator")
    
    user = input()
    if user == '1':
        ClerkPT.PTcalc()
        time.sleep(2)
    elif user == '2':
        ClerkFT.FTcalc()
        time.sleep(2)
    elif user == '3':
        RA.RAcalc()
        time.sleep(2)
    elif user == '4':
        A2.A2calc()
        time.sleep(2)
    elif user == '5':
        A1.A1calc()
        time.sleep(2)



