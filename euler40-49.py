#!/usr/bin/python
from euler.EulerUtils import add, isPermutation, isPrime
import math
import sys

 
def euler49():
  primesList = []
  for i in range(1000, 9999):
    if isPrime(i):
      primesList.append(i)
  
  answerList = []
  for i in primesList:
    ind_i = primesList.index(i)
    for ind_j in range(ind_i + 1, len(primesList)):
      j = primesList[ind_j]
      for ind_k in range(ind_j + 1, len(primesList)):
        k = primesList[ind_k]
        if k - j == j - i:
          answerList.append((i, j, k))
    if ind_i > len(primesList) - 3:
      continue
  for i in answerList:
    if isPermutation(i[0], i[1]) and isPermutation(i[1], i[2]):
      print i

def euler48():
  alist = []
  for i in range(1, 1000):
    alist.append(i ** i)
  print str(reduce(add, alist))[-10:] 


def main():
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored
  
  # euler49()
  # euler48()
  euler51()


if __name__ == '__main__':
  main()
