class Seat:
  def __init__(self):
    self.dirty = False

  def __repr__(self):
    return f"<Seat: isDirty={self.dirty}>"


class Car:
  def __init__(self):
    self.seats = [
      Seat(),
      Seat(),
      Seat(),
      Seat(),
      Seat()
    ]

  def use(self, people_amount):
    if people_amount > 5:
      raise Exception("Cannot seat more than 5 people")

    # current_person = 0
    # while current_person < people_amount:
    #   current_seat = self.seats[current_person]
    #   current_seat.dirty = True
    #   current_person += 1

    for current_person in range(people_amount):
      current_seat = self.seats[current_person]
      current_seat.dirty = True

  def __repr__(self):
    seat_string = ""
    for seat in self.seats:
      seat_string += str(seat) + "\n"
    return f"<Car: seats={seat_string}>"


bmw = Car()
bmw.use(3)

print(bmw)