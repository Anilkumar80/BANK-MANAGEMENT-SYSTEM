class bank:
    balance=50000
    def checkbalance(self):
        self.balance=self.balance
        print(self.balance)
    def deposit(self,amnt):
        c=amnt+self.balance
        print(c)
    def withdrawl(self,wdraw):
        e=wdraw+self.balance
        print(e)
a=bank()
choice=int(input("""1.CHECK BALANCE
2.DEPOSIT AMOUNT
3.WITHDRAWL AMOUNT"""))
if choice==1:
    a.checkbalance()
    pass
if choice==2:
    d=int(input("ENTER AMOUNT TO DEPOSIT:"))
    a.deposit(d)
else:
    print("NOT PROCCED")
if choice ==3:
    dw=int(input("ENTER AMOUNT TO WITHDRAWL:"))
    a.withdrawl(dw)