# Devon Taylor
# U1L1 - Big Rat
# Data Structures
# 9/4/24

from ratFunctions import *
import time

GOAL = 50000                # Target average weight (grams)
NUM_RATS = 20               # Max adult rats in the lab
INITIAL_MIN_WT = 200        # The smallest rat (grams)
INITIAL_MAX_WT = 600        # The chonkiest rat (grams)
INITIAL_MODE_WT = 300       # The most common weight (grams)
MUTATE_ODDS = 0.01          # Liklihood of a mutation
MUTATE_MIN = 0.5            # Scalar mutation - least beneficial
MUTATE_MAX = 1.2            # Scalar mutation - most beneficial
LITTER_SIZE = 8             # Pups per litter (1 mating pair)
GENERATIONS_PER_YEAR = 10   # How many generations are created each year
GENERATION_LIMIT = 500      # Generational cutoff - stop breeded no matter what

def createGen(selectedRats):
  pups = breed(selectedRats)
  mutPups = mutate(pups)
  mean = calculate_mean(mutPups)
  selectedRats = select(selectedRats, pups)

  return selectedRats, mean

def main():
  exprStart = time.time()

  genMeans = []
  gens = 0

  initPop = initial_population()
  pups = breed(initPop)
  mutPups = mutate(pups)
  mean = calculate_mean(mutPups)
  genMeans.append(mean)
  selectedRats = select(initPop, pups)

  biggestRat = ""
  target = False
  
  while target == False or gens > GENERATION_LIMIT:
    gen = createGen(selectedRats[0])
    genMeans.append(gen[1])
    gens += 1
    if fitness(genMeans[-1])[0] == True:
      if gen[0][0][0][0].__gt__(gen[0][0][1][0]):
        biggestRat = gen[0][0][0][0]
      else:
        biggestRat = gen[0][0][1][0]
      target = True
  
  exprEnd = time.time()

  print(f"\nFinal generation mean: {genMeans[-1]} grams\n")
  print(f"{gens} generations")
  print(f"Experiment length: {gens/10} years")
  print(f"Simulation duration: {round(exprEnd-exprStart, 4)}seconds\n")
  print(f"Chonkiest rat: ({biggestRat.getSex()}) {biggestRat} grams")
  line = ""
  num = 0
  for i in genMeans:
    if num % 10 != 0:
      line += str(i) + "\t"
      num += 1
    elif num % 10 == 0:
      line += "\n"
      num += 1
    else:
      line += str(i) + "\t"
  print(line)


if __name__ == "__main__":
  main()