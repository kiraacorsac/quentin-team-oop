class Account:
  def __init__(self, money):
    self.balance = money

  def add_money(self, money):
    self.balance += money

  def add_interest(self):
    self.balance *= 1.01


class SavingsAccount(Account):
  def add_interest(self):
    self.balance *= 1.02


account = Account(100)
account.add_money(1000.0)
print(account.balance)
account.add_interest()
print(account.balance)

print("Savings:")

savings_account = SavingsAccount(100)
savings_account.add_money(1000.0)
print(savings_account.balance)
savings_account.add_interest()
print(savings_account.balance)
