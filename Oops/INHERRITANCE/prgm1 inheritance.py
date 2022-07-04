class A:
    def printa(self,num1):
        self.num1=num1
        print("Inside class A",self.num1)
class B(A):
    def printb(self,num2):
        self.num2=num2
        print("Inside class B",self.num2,self.num1)

b=B()
b.printa(60)
b.printb(40)

#here A is Parent class,base class,super class
#here B is child class,sub class,derived class