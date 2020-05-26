class Account:
  def __init__(self, starting_amount, owner_name):
    self.owner_name = owner_name
    self.money = starting_amount

  def set_balance(self, new_amount):
    if new_amount >= 0:
      self.money = new_amount
    else:
      raise Exception("Not enough money")

lacos_account = Account(1000, "ladislav")

lacos_account.set_balance(100)
# lacos_account.set_balance(-100)

lacos_account.money = -100
print(lacos_account.money)