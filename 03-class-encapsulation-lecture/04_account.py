class Account:
  def __init__(self, starting_amount, owner_name):
    self.owner_name = owner_name
    self.__money = starting_amount

  def set_balance(self, new_amount):
    if new_amount >= 0:
      self.__money = new_amount
    else:
      raise Exception("Not enough money")

  def empty_account(self):
    self.__money = 0

lacos_account = Account(1000, "ladislav")

lacos_account.set_balance(100)
lacos_account.empty_account()
# lacos_account.set_balance(-100)

print(lacos_account)

