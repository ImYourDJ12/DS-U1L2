# Devon Taylor
# U1L2 - Visualizing rat growth
# Data Structures
# 9/16/24

import matplotlib.pyplot as plt
from L1main import L1main

def drawGraph(big, small, average):

  for dataset in [big, small, average]:
    plt.plot(dataset)

    plt.title("Largest and Smallest Rats by Generation")
    plt.xlabel("Generations")
    plt.ylabel("Weight in Grams")

    plt.legend(["biggestRats", "smallestRats", "average"])
    plt.show()
    plt.savefig("ratPlot.png")
  

def readFiles(inPath):
  with open(inPath, 'r') as openFile:
    contents = openFile.read()
  return contents

def main():
  L1main()
  biggestRats = readFiles("biggestRats.txt")
  smallestRats = readFiles("smallestRats.txt")
  genAverages = readFiles("genAverages.txt")

  biggestRats = biggestRats.split()
  smallestRats = smallestRats.split()
  genAverages = genAverages.split()

  bigRats = []
  for i in biggestRats:
    if i == biggestRats[0]:
      i = i.replace(i[0], "")
    bigRats.append(int(i))

  smallRats = []
  for i in smallestRats:
    if i == smallestRats[0]:
      i = i.replace(i[0], "")
    smallRats.append(int(i))

  averages = []
  for i in genAverages:
    if i == genAverages[0]:
      i = i.replace(i[0], "")
    averages.append(int(i))

  drawGraph(bigRats, smallRats, averages)

if __name__ == "__main__":
  main()