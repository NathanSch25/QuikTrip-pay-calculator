from outputs.Outputs import Output

class A2:
    def A2calc():
        hours = float(input("how many hours were worked: "))
        rate = 22.79

        tempList = []
        tempList = Output.GroseCalc(hours, rate), A2.TBonus2A()
        finalList = tempList[0][0], tempList[0][1], tempList[1][0], tempList[1][1], tempList[0][2]
        
        O1 = Output(finalList[0], finalList[1], ((hours*52) / 12), 4, finalList[2], finalList[3], finalList[4])
        O1.Complete()
        
    def TBonus2A():
        TBonusAnual = 0
        TBonusQuarter = 0
        off = -1
        
        while off < 0:
            off = int(input(" how many days have you requested off this year? "))
        print('\n \n \n')
        if off <=3:
            TBonusAnual = 3
            TBonusQuarter = 4
        elif off == 6:
            TBonusAnual = 3
            TBonusQuarter = 3
        elif off == 9:
            TBonusAnual = 2
            TBonusQuarter = 2
        elif off == 10:
            TBonusAnual = 2
            
        elif off == 11:
            TBonusAnual = 2
            
        elif off == 12:
            TBonusAnual = 2
            
        elif off == 13:
            TBonusAnual = 2
            
        elif off == 14:
            TBonusAnual = 1
            
        elif off >= 15:
            TBonusAnual = 1
            
        
        return (TBonusAnual, TBonusQuarter)
