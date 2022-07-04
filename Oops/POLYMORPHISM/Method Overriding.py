#Method overriding
#Emthod overriding[same method name and same number of arguments]

class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside Add",self.num1+self.num2)

class Add2(Add):
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside Add2",self.num1+self.num2)

ob=Add2()
ob.sum(20,30)

#here child class over write parent class
