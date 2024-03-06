from outputs.Outputs import Output

class RA:
    def RAcalc():
        hours = float(input("how many hours were worked: "))
        choice = ' '
        years = -1.1
    
        while years < 0:
            years = float(input("how many years have you worked (0.0): "))
        if years < 1:
            rate = 15
        elif years >= 4:
            rate = 20.47
        elif years >= 3:
            rate = 19.06
        elif years >= 2:
            rate = 17.46
        elif years >= 1:
            rate = 16.52

        tempList = []
        tempList = Output.GroseCalc(hours, rate), RA.TBonusRA()
        finalList = tempList[0][0], tempList[0][1], tempList[1][0], tempList[1][1], tempList[0][2]
        
        print(finalList)
        O1 = Output(finalList[0], finalList[1], ((hours*52) / 12), 3, finalList[2], finalList[3], finalList[4])
        O1.Complete()
        
    def TBonusRA():
        TBonusAnual = 0
        TBonusQuarter = 0
        off = -1
        
        while off < 0:
            off = int(input(" how many days have you requested off this year? "))
        print('\n \n \n')
        if off <= 3:
            TBonusAnual = 3
            TBonusQuarter = 3
        elif off == 6:
            TBonusAnual = 2
            TBonusQuarter = 2
        elif off == 9:
            TBonusAnual = 2
            TBonusQuarter = 1
        elif off == 10:
            TBonusAnual = 2
            
        elif off == 11:
            TBonusAnual = 2
            
        elif off == 12:
            TBonusAnual = 2
            
        elif off == 13:
            TBonusAnual = 1
            
        elif off == 14:
            TBonusAnual = 1
            
        elif off >= 15:
            TBonusAnual = 1
            
        
        return (TBonusAnual, TBonusQuarter)
