# Why OOP?

# 1) Encapsulation
  # By bundling the data together, you always know what is where
  # By not allowing "free" access, your code is less prone to errors


class Account:
  def __init__(self, starting_money):
    # attributes
    self.money = starting_money

savings_account = Account(5)

# we can directly set the amount left on the account - this can lead to unexpected results.
savings_account.money -= 10