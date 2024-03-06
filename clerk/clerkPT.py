
from outputs.Outputs import Output

class ClerkPT:
    def PTcalc():
        hours = float(input("how many hours were worked: "))
        erp = False
        grose = 0.0
        tax = 0.0
        net = 0.0
        choice = ' '
        years = -1.1
    
        while years < 0:
            years = float(input("how many years have you worked: "))
        if years < 1:
            rate = 13.59
        elif years >= 3:
            rate = 16.94
        elif years >= 2:
            rate = 15.81
        elif years >= 1:
            rate = 14.39

        while ((choice != 'y') and (choice != 'n')):
            choice = input("Are you working erp y or n: ")
        print("\n\n\n")

        if choice == 'y':
            erp = True
            rate += 3

        tList = ()
        tList = Output.GroseCalc(hours, rate, erp)
        O1 = Output(tList[0], tList[1], ((hours*52) / 12), 1, tList[2])
        O1.Advanced()
        
