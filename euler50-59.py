#!/usr/bin/python
from euler.EulerUtils import add, isPermutation, isPrime
import math
import sys


def euler51():
  for i in range(100000, 999999):
    myList = [i * j for j in range(1, 6) ]
    # print myList
    if (isPermutation(myList[0], myList[1]) and  isPermutation(myList[1], myList[2]) and 
        isPermutation(myList[2], myList[3]) and  isPermutation(myList[3], myList[4])):
      print myList 



def main():
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored
  
  # euler49()
  # euler48()
  euler51()


if __name__ == '__main__':
  main()
