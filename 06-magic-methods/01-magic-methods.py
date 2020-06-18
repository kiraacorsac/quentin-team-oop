from functools import total_ordering

@total_ordering
class Fractional:

  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator

  def __mul__(self, other):
    return Fractional(self.numerator * other.numerator, self.denominator * other.denominator)

  def __add__(self, other):
    if(self.denominator != other.denominator):
      raise Exception("Cannot add fractionals with different denominators")
    return Fractional(self.numerator + other.numerator, self.denominator)

  # I have used @total_orderding decorator - I don't need to implement other comparsions
  def __lt__(self, other):
    return self.toDecimal() < other.toDecimal()

  def __repr__(self):
    #simplification?
    return f"{self.numerator}/{self.denominator}"

  def toDecimal(self):
    return self.numerator / self.denominator

num1 = Fractional(1, 2)
num2 = Fractional(2, 1)
num3 = Fractional(3, 2)

print(num1 * num2)

print(num1 + num2 * Fractional(2, 2))

num3 += Fractional(6, 2)
print(num3)

# print(three - two)


print(num3 == Fractional(6, 2))
print(Fractional(7, 2) > Fractional(6, 2))