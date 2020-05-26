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
# vs code still tries to autocomplete ".money"
# could lead to unexpected bugs
better_acc.money -= 10

