#Nucleotide content calculator
import re
def nuc_calulator(nuc):
    nuc=nuc.upper()
    A=len(re.findall('A',nuc))
    T=len(re.findall('T',nuc))
    G=len(re.findall('G',nuc))
    C=len(re.findall("C",nuc))
    print('A% =',A/len(nuc));print('T% =',T/len(nuc));print('G% =',G/len(nuc));print('C% =',C/len(nuc))
#An example
nuc_calulator('actggggAAActGGTaacGG')

#Human resource database
class staff:
    def __init__(self,fname,lname,location,role):
        self.fname=fname
        self.lname=lname
        self.location=location
        self.role=role
    def infomation(self):
        print('Full name: ',f'{self.fname} {self.lname}')
        print('Location: ',self.location)
        print('Role: ',self.role)
#An example
Rob_Young=staff('Rob','Young','Edinburgh','Faculty')
staff.infomation(Rob_Young)

#Chocolate bar affordability calculator
def Chocolate_caculator(money,price):
    number=int(money/price)
    change=money-number*price
    print(f'Number of cholate bar: {number}\nThe change left over: {change}')
    return [number,change]
#An example
Chocolate_caculator(100,3)
