class Garage:
  def __init__(self):
    self.car_list = []

  def park(self, car):
    self.car_list.append(car)

  def start_cars(self, color):
    for car in self.car_list:
      if car.color == color:
        car.start()

  def __repr__(self):
    return f"Cars in the garage: {self.car_list}"


class Car:
  def __init__(self, color, maker):
    self.color = color
    self.maker = maker
    self.motor_running = False

  def __repr__(self):
    return f"<{self.color} {self.maker}>: Motor running - {self.motor_running}"

  def start(self):
    self.motor_running = True



garage = Garage()

bmw = Car("white", "bmw")
audi = Car("silver", "audi")
nissan = Car("white", "nissan")


garage.park(bmw)
garage.park(audi)
garage.park(nissan)

print(garage)
garage.start_cars("white")
print(garage)
