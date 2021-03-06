class Account3:
  def __init__(self, starting_money):
    # private attribute
    self.__money = starting_money

  def set_new_balance(self, amount):
    if(amount > 0):
      self.__money = amount
    else:
      raise Exception("Not enough money")

    
  def get_balance(self):
    return self.__money

even_better_acc = Account3(5)
# works as expected
even_better_acc.set_new_balance(1)
# raises custom exception 
even_better_acc.set_new_balance(10)

print(even_better_acc.__money)
print(even_better_acc.get_balance())