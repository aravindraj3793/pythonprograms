#how to create methods in class

#methods (functions creates inside class)

#self : instance keyword

class Person:
    def reading(self):  #method1
        print("Reading books")
    def writing(self):  #method2
        print("Writing a book")

pe=Person()       #objects
pe.reading()
pe.writing()

pe1=Person()
pe1.writing()

