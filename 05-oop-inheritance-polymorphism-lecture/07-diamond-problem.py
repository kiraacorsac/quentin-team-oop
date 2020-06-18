class D():
  def method(self):
    print("D")

class B(D):
  def method(self):
    print("B")

class C(D):
  def method(self):
    print("C")

class A(B, C):
  pass
  # def method(self):
  #   print("A")

a = A()
a.method()
