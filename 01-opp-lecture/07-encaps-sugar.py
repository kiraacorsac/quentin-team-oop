class Account:
  def __init__(self, balance):
    self.__money = balance

  @property
  def money(self):
    return self.__money

  @money.setter
  def money(self, amount):
    if(amount > 0):
      self.__money = amount
    else:
      raise Exception("Not enough money")

acc = Account(10)

print(acc.money)
acc.money = -10