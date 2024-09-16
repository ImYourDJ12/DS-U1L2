from random import uniform
from main import MUTATE_MIN, MUTATE_MAX

class Rat:
  def __init__(self, sex, weight):
    self.sex = sex
    self.weight = weight
    self.litters = 0

  def __str__(self):
    return str(self.weight)

  def __repr__(self):
    return str(self.weight)

  def getWeight(self):
    return self.weight

  def getSex(self):
    return self.sex

  def canBreed(self):
    if self.litters < 5:
      return False
    else:
      return True

  def mutate(self):
      mutSize = uniform(MUTATE_MIN, MUTATE_MAX)
      self.weight *= mutSize
      self.weight = round(self.weight)
      return self.weight

  def __lt__(self, other):
    return self.weight < other.weight

  def __gt__(self, other):
    return self.weight > other.weight
    
  def __le__(self, other):
    return self.weight <= other.weight

  def __ge__(self, other):
    return self.weight >= other.weight

  def __eq__(self, other):
    return self.weight == other.weight
  