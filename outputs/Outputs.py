class Output:
    def __init__(self, grose, net, csa=0, profit=0, anual=0, quarter=0, percent=0):
        self.net = net
        self.grose = grose
        self.csa = csa
        self.profit = profit
        self.anual = anual
        self.quarter = quarter
        self.percent = percent
        
    def Simple(self):
        combo = ((self.csa + self.profit) * .92)
        print ("grose income is", round(self.grose, 2))
        print ("deductions are ", round((self.net - self.grose), 2))
        print ("net pay is     ", round(self.net, 2))
        print ("monthly income ", round(((self.net*4) + combo), 2), end='')
        print ("\n")
        
    def Advanced(self):
        percent = self.percent
        combo = ((self.csa + self.profit) * percent)
        print ("with 93% average shop CSA bonus is  ", round(self.csa, 2))
        print ("with 100,000 profit, profit bonus is", round(self.profit, 2))
        print ("grose income is                     ", round(self.grose, 2))
        print ("deductions are                      ", round((self.net - self.grose), 2))
        print ("net pay is                          ", round(self.net, 2))
        print ("monthly income                      ", round(((self.net*4) + combo), 2))
        print ("anual income                        ", round(((self.net*52) + (combo * 12)), 2), end='')
        print ("\n")
    
    def Complete(self):
        percent = self.percent
        
        basicBonus = ((self.csa + self.profit) * percent)
        bigBonus = ((self.anual + (self.quarter * 4)) * percent)
        print ("with 93% average shop CSA bonus is  ", round(self.csa, 2))
        print ("with 100,000 profit, profit bonus is", round(self.profit, 2))
        print ("grose income is                     ", round(self.grose, 2))
        print ("deductions are                      ", round(((self.net - self.grose)), 2))
        print ("net pay is                          ", round(self.net, 2))
        print ("monthly income                      ", round(((self.net*4) + basicBonus), 2))
        print ("T% quartely is                      ", round(self.quarter, 2))
        print ("T% anual is                         ", round(self.anual, 2))
        print ("anual income                        ", round(((self.net*52) + (basicBonus * 12) + bigBonus), 2), end='')
        print ("\n")
        return 0
    
    def GroseCalc(hours, rate, erp=False):
        if hours <= 40:
            grose = hours * rate
        else:
            grose = 40 * rate
            grose += (hours - 40) * (rate * 1.5)
            
        percent = 1 - (Output.PercentCalc(grose))  
        
        tax = grose * percent
        net = grose - tax

        if erp:
            print ("while working erp:\n")
        return grose, net, percent
    
    def PercentCalc(grose):
        percent = 0
        if grose*52 <= 11000:
            percent = .90
        elif grose*52 <= 44725:
            percent = .88
        elif grose*52 <= 95375:
            percent = .78
        elif grose*52 <= 182100:
            percent = .76
        elif grose*52 <= 231251:
            percent = .68
            
        return percent
    
