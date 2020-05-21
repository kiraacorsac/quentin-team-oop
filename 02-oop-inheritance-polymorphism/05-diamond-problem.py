class A:
    def method(self):
        print("method of A called")

class B(A):
    def method(self):
        print("method of B called")
    
class C(A):
    def method(self):
        print("method of C called")

class D(B,C): #order matters
    pass


d = D()
d.method()