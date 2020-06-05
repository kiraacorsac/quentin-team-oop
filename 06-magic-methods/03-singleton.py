class PlanetarySystem:
  def __init__(self, name, star, planets):
    self.name = name
    self.star = star
    self.planets = planets


class SolarSystem(PlanetarySystem):
  '''
  The one and only solar system
  Implements Singleton pattern
  '''

  __instance = None

  def __new__(cls):
      if cls.__instance is None:
          print('Creating the object')
          cls.__instance = PlanetarySystem("Solar System", "Sun", ["Mercury", "Venus", "Earth"]) 
      return cls.__instance


solarSystem = SolarSystem()
print(solarSystem.name)
solarSystem.planets.append("Mars")

solarSystem2 = SolarSystem()
print(solarSystem2.planets)
