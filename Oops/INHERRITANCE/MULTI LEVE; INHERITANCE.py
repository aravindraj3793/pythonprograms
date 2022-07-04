#Multi Level Inheritance

#it is similar to Mutiple inheritance

class A:
    def printa(self):
        print("inside class a")

class B(A):
    def printb(self):
        print("inside class b")

class C(B):
    def printc(self):
        print("inside class c")

ob=C()
ob.printb()
ob.printa()
ob.printc()
