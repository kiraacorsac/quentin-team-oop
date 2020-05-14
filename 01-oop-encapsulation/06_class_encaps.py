class Account:
  def __init__(self, starting_money):
    # attributes
    self.money = starting_money

savings_account = Account(5)

# we can directly set the amount left on the account - this can lead to unexpected results.
savings_account.money -= 10

class Account2:
  def __init__(self, starting_money):
    # attributes
    self.money = starting_money

  def set_new_balance(self, amount):
    if(amount > 0):
      self.money = amount
    else:
      raise Exception("Not enough money")


better_acc = Account2(5)

# works as expected
better_acc.set_new_balance(10)

# did not *actually* take care of the problem
# could lead to unexpected bugs
better_acc.money -= 10


class Account3:
  def __init__(self, starting_money):
    # private attribute
    self.__money = starting_money

  def set_new_balance(self, amount):
    if(amount > 0):
      self.money = amount
    else:
      raise Exception("Not enough money")

  # i need a "getter" now
  def get_balance(self):
    return self.__money

even_better_acc = Account3(5)
# works as expected
even_better_acc.withdraw(1)
# raises custom exception 
even_better_acc.withdraw(10)

# raises exception
even_better_acc.__money -= 10


# i can use some fancy syntax to do this too!
class Account4:
  def __init__(self, starting_money):
    # private attribute
    self.balance = starting_money

  @property
  def balance(self):
    return self.__money

  @balance.setter
  def balance(self, amount):
    if(amount > 0):
      self.money = amount
    else:
      raise Exception("Not enough money")

even_better_acc = Account4(5)
# works as expected
even_better_acc.balance -= 1
# raises exception
even_better_acc.balance -= 10

