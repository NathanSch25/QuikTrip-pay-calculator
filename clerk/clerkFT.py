from outputs.Outputs import Output

class ClerkFT:
    def FTcalc():
        hours = float(input("how many hours were worked: "))
        erp = False
        choice = ' '
        years = -1.1
        
        while years < 0:
            years = float(input("how many years have you worked: "))
        if years < 1:
            rate = 13.59
        elif years >= 4:
            rate = 16.26
        elif years >= 3:
            rate = 15.75
        elif years >= 2:
            rate = 15.06
        elif years >= 1:
            rate = 14.42

        while ((choice != 'y') and (choice != 'n')):
            choice = input("Are you working erp y or n: ")

        if choice == 'y':
            erp = True
            rate += 3
         
        tempList = []
        tempList = Output.GroseCalc(hours, rate, erp), ClerkFT.TBonusFT()
        finalList = tempList[0][0], tempList[0][1], tempList[1][0], tempList[1][1], tempList[0][2]
        
        print(finalList)
        O1 = Output(finalList[0], finalList[1], ((hours*52) / 12), 250, finalList[2], finalList[3], finalList[4])
        O1.Complete()
        
    def TBonusFT():
        TBonusAnual = 0
        TBonusQuarter = 0
        off = -1
        
        while off < 0:
            off = int(input(" how many days have you requested off this year? "))
        print('\n \n \n')
        if off <= 3:
            TBonusAnual = 1969.11
            TBonusQuarter = 246.14
        elif off == 6:
            TBonusAnual = 1772.21
            TBonusQuarter = 184.60
        elif off == 9:
            TBonusAnual = 1654.06
            TBonusQuarter = 123.07
        elif off == 10:
            TBonusAnual = 1535.91
            
        elif off == 11:
            TBonusAnual = 1437.45
            
        elif off == 12:
            TBonusAnual = 1319.30
            
        elif off == 13:
            TBonusAnual = 1201.15
            
        elif off == 14:
            TBonusAnual = 1102.70
            
        elif off >= 15:
            TBonusAnual = 984.56
            
        
        return (TBonusAnual, TBonusQuarter)