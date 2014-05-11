#!/usr/bin/python
from euler.EulerUtils import add, isPermutation, isPrime, primes
from euler.EulerUtils import combination, factorial, isPalindrome
from euler.EulerUtils import isNotLychrel, invert
import math
import sys


def euler51():
  fullList = primes(999999)
  fives=[i for i in fullList if len(str(i))==5 ]
  sixes=[i for i in fullList if len(str(i))==6 ]
  fours=[i for i in fullList if len(str(i))==4 ]
  
  
def euler52():
  x=1
  while 1:
    xList=[x*i for i in range(1,7)]
    if (isPermutation(xList[0], xList[1]) and
        isPermutation(xList[1], xList[2]) and
        isPermutation(xList[2], xList[3]) and
        isPermutation(xList[3], xList[4]) and
        isPermutation(xList[4], xList[5]) ):
      print xList
    x+=1

def euler53():
  bigList = []
  for n in range(11,101):
    for r in range(1,n):
      c= combination(n,r)
      if c>1000000:
        bigList.append(c)
  print len(bigList)
  
def euler54():
  file = open("Resources/PokerHands.txt","r")
  iWon=0
  heWon=0
  for line in file:
    myHand = line.split(" ")[:5]
    hisHand = line.split(" ")[5:-1]
    hisHand.append(line[-3:].replace('\n',''))
    isRoyalFlush()
  

def euler55():
  lychCount=10000
  for i in range(1,10001):
    if isNotLychrel(i):
      lychCount -= 1
  print lychCount
  

def euler56():
  max=1
  for i in range(1,100):
    for j in range(1,100):
      numberList=[int(n) for n in list(str(i**j))]
      number = reduce(add,numberList)
      if max<number:
        max=number
  print max

def euler58():
  
  return
def makeSpiral(n):
  return

def main():
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored
  euler56()
  
  # euler48()
#   euler52()


if __name__ == '__main__':
  main()
