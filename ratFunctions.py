from main import *
from ratFile import *
from random import triangular, choice, random, uniform, shuffle


def initial_population():
  # Create the initial set of rats based on constants
  rats = [[],[]]
  mother = Rat("F", INITIAL_MIN_WT)
  father = Rat("M", INITIAL_MAX_WT)
  
  for r in range(NUM_RATS):
    if r < 10:
      sex = "M"
      ind = 0
    else:
      sex = "F"
      ind = 1
  
    wt = calculate_weight(sex, mother, father)
    R = Rat(sex, wt)
    rats[ind].append(R)
  
  return rats


def calculate_weight(sex, mother, father):
  '''Generate the weight of a single rat'''
  min = mother.getWeight()
  max = father.getWeight()
  # Use the triangular function from the random library to skew the 
  #baby's weight based on its sex
  
  if sex == "M":
    wt = int(triangular(min, max, max))
  else:
    wt = int(triangular(min, max, min))
  
  return wt


def mutate(pups):
  """Check for mutability, modify weight of affected pups"""
  for i in range(len(pups)):
    for rat in pups[i]:
      chance = random()
      if chance <= MUTATE_ODDS:
        rat.mutate()
  return pups  


def breed(rats):
  """Create mating pairs, create LITTER_SIZE children per pair"""
  children = [[],[]]
  shuffle(rats[0])
  shuffle(rats[1])

  for i in range(len(rats[0])):
    father = rats[0][i]
    father.litters += 1
    mother = rats[1][i]
    mother.litters += 1
    for e in range(LITTER_SIZE):
      sexes = ["M","F"]
      sex = choice(sexes)
      if sex == "M":
        ind = 0
      else:
        ind = 1
      wt = calculate_weight(sex, mother, father)
      R = Rat(sex, wt)
      children[ind].append(R)

  return children

def select(rats, pups):
  '''Choose the largest viable rats for the next round of breeding'''
  for rat in rats[0]:
    pups[0].append(rat)
  for rat in rats[1]:
    pups[1].append(rat)

  rats[0].clear()
  rats[1].clear()
  pups[0].sort(reverse=True)
  pups[1].sort(reverse=True)

  num = 0
  while len(rats[0])<10:
    rat = pups[0][num]
    if rat.litters > 5:
      num += 1
      continue
    else:
      rats[0].append(rat)
      num += 1

  num = 0
  while len(rats[1])<10:
    rat = pups[1][num]
    if rat.litters > 5:
      num += 1
      continue
    else:
      rats[1].append(rat)
      num += 1
  rats[0].sort(reverse=True)
  rats[1].sort(reverse=True)

  if rats[0][0].__gt__(rats[1][0]):
    largest = rats[0][0]
  else:
    largest = rats[1][0]

  return rats, largest

def calculate_mean(rats):
  '''Calculate the mean weight of a population'''
  sumWt = 0
  numRats = len(rats[0]) + len(rats[1])
  for rat in rats[0]:
    sumWt += rat.getWeight()
  for rat in rats[1]:
    sumWt += rat.getWeight()

  return sumWt // numRats

def fitness(mean):
  """Determine if the target average matches the current population's average"""
  return mean >= GOAL, mean
