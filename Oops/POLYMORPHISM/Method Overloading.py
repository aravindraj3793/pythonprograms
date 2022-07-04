#Method Overloading
#in python the Method Overloading is not supported


class Add:
    def sum(self, num1, num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)

class Add1:
    def sum(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)

ob=Add1()
ob.sum(4,5,6)

#here the method name is same in 2 class and it will take latest method