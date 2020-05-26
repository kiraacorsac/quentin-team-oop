# i can use some fancy syntax to do this too!
class Account4:
  def __init__(self, starting_money):
    # private attribute
    self.balance = starting_money

  @property
  def balance(self):
    return self.__money

  # name it as the @property function
  @balance.setter
  def balance(self, amount):
    #additional protection
    if(amount > 0):
      self.__money = amount
    else:
      raise Exception("Not enough money")

even_better_acc = Account4(5)
# works as expected
even_better_acc.balance -= 1
# raises exception
even_better_acc.balance -= 10

# works as expected
print(even_better_acc.balance)

# raises as expected
print(even_better_acc.__money)