from logger import BasicLogger

def newCustomer(name):
  logger = BasicLogger()
  logger += "New customer with name: " + name
  
