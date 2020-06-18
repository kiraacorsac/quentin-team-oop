class Fractional:
  def __init__(self, numerator, denominator):
    self.numer  = numerator
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

half = Fractional(1, 2)
three_halfs = Fractional(3, 2)

result = half * three_halfs
      #  half.__mul__(three_halfs)
print(result.numer, result.denom)
result *= Fractional(3,1)
print(result.numer, result.denom)

print(half + Fractional(2, 3))


# number = 2
# number *= 4
# number = number * 4
# print(number)
