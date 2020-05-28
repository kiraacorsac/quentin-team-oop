# i can use some fancy syntax to do this too!
class Account4:
  def __init__(self, starting_money):
    # private attribute
    # self.__money = 0
    self.remaining_balance = starting_money
    # print(self.remaining_balance)

  @property
  def remaining_balance(self):
    print("calling getter")
    return self.__money

  # name it as the @property function
  @remaining_balance.setter
  def remaining_balance(self, amount):
    print("calling setter")
    #additional protection
    if(amount > 0):
      self.__money = amount
    else:
      raise Exception("Not enough money")

  def overdraw_account(self, amount):
    print(self.remaining_balance)
    self.__money = -amount

  def withdraw(self, amount):
    self.remaining_balance -= amount
    self.__money -= 1

even_better_acc = Account4(5)
print(even_better_acc.remaining_balance)

# even_better_acc.remaining_balance = even_better_acc.remaining_balance - 1
# print(even_better_acc.remaining_balance)
even_better_acc.remaining_balance -= 1 
print(even_better_acc.remaining_balance)
extracted_val = even_better_acc.remaining_balance - 1

# # works as expected
# even_better_acc.remaining_balance -= 1
# print(even_better_acc.remaining_balance)
# # raises exception
# even_better_acc.remaining_balance -= 10

# works as expected
# print(even_better_acc.balance)

# raises as expected
# print(even_better_acc.__money)