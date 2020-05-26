class Account:
  def __init__(self, starting_amount, owner_name):
    self.owner_name = owner_name
    self.money = starting_amount


lacos_account = Account(1000, "ladislav")

print(lacos_account.money)
print(lacos_account.owner_name)

#incorrect state

new_money = -500
if(new_money > 0):
  lacos_account.money = new_money
else:
  print("negative money not allowed")
  
print(lacos_account.money)