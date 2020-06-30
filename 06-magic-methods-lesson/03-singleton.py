class PlanetarySystem:
  __instances = []

  def __init__(self, star):
    self.__instances.append(self)
    self.star = star
    self.planets = []

  def add_planet(self, planet):
    self.planets.append(planet)

  def get_instances(self):
    return self.__instances


class SolarSystem:
  __instance = None
  
  def __new__(cls):
    if(SolarSystem.__instance is None):
      SolarSystem.__instance = PlanetarySystem("Sun")
    return SolarSystem.__instance


system = SolarSystem()
system.add_planet("Earth")

# print(system)


system2 = SolarSystem()


proxima = PlanetarySystem("Proxima Centauri")

print(proxima.get_instances())

# print(proxima.__dir__())
# print(system == system2)
# print(system.planets, system2.planets)
