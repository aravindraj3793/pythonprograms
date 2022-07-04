#class Bank
#accntcreation[name,accno,minimumbal]
#withdraw[amount]
#deposit[amount]

class Bank:
    bank_name="SBI"
    def accntcreation(self,name,accno):
        self.name=name
        self.accno=accno
        self.minbal=2000
        self.totalbal=self.minbal

    def deposit(self,amount):
        self.amount=amount
        self.totalbal=self.minbal+self.amount
        print("your",Bank.bank_name,"account has been credited with ",self.amount)
        print("your total balance",self.totalbal)

    def withdraw(self,amountt):
        self.amountt=amountt
        self.totalbal=self.totalbal-self.amountt
        if(self.amountt<=self.minbal):
            print("Insufficient fund")
        else:
            print("Money is debited")

ob=Bank()
ob.deposit(1000)







