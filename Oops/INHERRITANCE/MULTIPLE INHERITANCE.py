#multiple inheritance

#Child class inherit more than one parent class

class A:
    def printa(self):
        print("inside class a")

class B:
    def printb(self):
        print("inside class b")

class C(A,B):
    def printc(self):
        print("inside class c")

ob=C()
ob.printa()
ob.printc()
ob.printb()