class Atm(object):
    def __init__(self,nameOfAtm,atm_card_number,pin_number):
        self.nameOfAtm=nameOfAtm
        self.atm_card_number=atm_card_number
        self.pin_number=pin_number

    def cashWithdrawl(self):
        money=input("Enter money you want to take out: ")
        print("Cash withdrawl= Rs" + money)

    def bankBalance(self):
        amount=input("Enter your bank balance: ")
        print("Bank balance is Rs"+ amount)

    def Loan(self):
        loan=input("Enter your loan: ")
        print("Your loan is Rs "+ loan)
        moneygiven=input("Enter money given: ")
        print("Money already given to bank=Rs" + moneygiven)
        abc=int(loan)-int(moneygiven)
        print("Money left to pay=Rs"+str(abc))
        
        

Axis=Atm("Axis","123456","700700")
print(Axis.nameOfAtm)
print(Axis.pin_number)
print(Axis.atm_card_number)
Axis.cashWithdrawl()
Axis.bankBalance()
Axis.Loan()


