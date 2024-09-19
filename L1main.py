# Devon Taylor
# U1L1 - Big Rat
# Data Structures
# 9/4/24

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
  from ratFunctions import breed, mutate, calculate_mean, select
  pups = breed(selectedRats)
  mutPups = mutate(pups)

  # the bigs and the smalls
  mutPups[0].sort(reverse=True)
  mutPups[1].sort(reverse=True)

  if mutPups[0][0].__gt__(mutPups[1][0]):
    biggestRat = mutPups[0][0]
  else:
    biggestRat = mutPups[1][0]

  if mutPups[0][-1].__lt__(mutPups[1][-1]):
    smallestRat = mutPups[0][-1]
  else:
    smallestRat = mutPups[1][-1]

  mean = calculate_mean(mutPups)
  selectedRats = select(selectedRats, pups)

  return selectedRats, mean, biggestRat, smallestRat


def createFiles(outPath, contents):
  with open(outPath, 'w') as openFile:
    openFile.write(contents)

def L1main():
  from ratFunctions import initial_population, breed, mutate, calculate_mean, select, fitness
  import time
  exprStart = time.time()

  genMeans = []
  gens = 0

  # initial population
  initPop = initial_population()
  pups = breed(initPop)
  mutPups = mutate(pups)
  mean = calculate_mean(mutPups)
  genMeans.append(mean)
  selectedRats = select(initPop, pups)

  biggestRat = ""
  genBigRats = []
  genSmallRats = []
  target = False
  
  # continues generation
  while target == False or gens > GENERATION_LIMIT:
    gen = createGen(selectedRats[0])
    genBigRats.append(gen[2])
    genSmallRats.append(gen[3])

    genMeans.append(gen[1])
    gens += 1

    # biggestRat selection
    if fitness(genMeans[-1])[0] == True:
      if gen[0][0][0][0].__gt__(gen[0][0][1][0]):
        biggestRat = gen[0][0][0][0]
      else:
        biggestRat = gen[0][0][1][0]
      target = True
  

  # End Results
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

  bigRats = ""
  for rat in genBigRats:
    bigRats += str(rat) + " "
  smallRats = ""
  for rat in genSmallRats:
    smallRats += str(rat) + " "
  means = ""
  for rat in genMeans:
    means += str(rat) + " "

  createFiles("biggestRats.txt", bigRats)
  createFiles("smallestRats.txt", smallRats)
  createFiles("genAverages.txt", means)


#if __name__ == "__main__":
  #main()