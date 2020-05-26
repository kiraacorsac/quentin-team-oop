class Fractional:
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator

  def __mul__(self, other):
    return Fractional(self.numerator * other.numerator, self.denominator * other.denominator)

  def __repr__(self):
    #simplification?
    return f"{self.numerator}/{self.denominator}"

half = Fractional(1, 2)
two = Fractional(2, 1)


print(half * two)
