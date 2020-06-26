class Fractional:
  def __init__(self, numerator, denominator):
    self.numer = numerator
    self.denom = denominator

  def __mul__(self, other):
    result_numerator = self.numer * other.numer
    result_denominator = self.denom * other.denom
    return Fractional(result_numerator,result_denominator)

  def __add__(self, other):
    if self.denom != other.denom:
      raise Exception("You can't add Fractionals with different denoms")
    result_numer = self.numer + other.numer
    result_denom = other.denom
    return Fractional(result_numer, result_denom)

  def __repr__(self):
    return f"<Fractional: {self.numer}/{self.denom}>"

  # <
  def __lt__(self, other):
    print("less than")
    value_self = self.numer / self.denom
    value_other = other.numer / other.denom
    return value_self < value_other

  def __le__(self, other):
    # value_self = self.numer / self.denom
    # value_other = other.numer / other.denom
    # return value_self == value_other or value_self < value_other
    print("less equal")
    return self < other or self == other

  # always override!
  def __eq__(self, other):
    print("equals")
    value_self = self.numer / self.denom
    value_other = other.numer / other.denom
    return value_self == value_other



half = Fractional(1, 2)
three_halfs = Fractional(3, 2)

result = half * three_halfs
      #  half.__mul__(three_halfs)
print(result.numer, result.denom)
result *= Fractional(3,1)
print(result.numer, result.denom)

print(Fractional(1,2))

# print(half + Fractional(2, 3))

print(Fractional(5, 2) <= Fractional(5, 2))

print(Fractional(1,2) == Fractional(32,2))
# Fractional(5,2).__eq__(Fractional(5,2))

# number = 2
# number *= 4
# number = number * 4
# print(number)
