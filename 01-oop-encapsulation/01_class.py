class Doggo:
    pass

# init class
rex = Doggo()
jake = Doggo()

second_jake = jake

print(rex == jake) # true or false? 
print(jake == second_jake)


# actally, everything is a class in python!
print(type(1))
print(type("hello world"))
print(type(print))
print(type(rex))