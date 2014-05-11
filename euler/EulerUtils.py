'''
Created on Mar 27, 2014

@author: jejoseph
'''
import math

def isPrime(number):
  if number ==2 or number == 3:
    return True
  if number == 4 or number ==1 :
    return False
  for i in range(2, int(number **.5)+1 ):
    if number % i == 0:
      return False
  return True

def add(a, b):
  return (a + b)

def multiply(a,b):
  return (a*b)

def isGreater(a,b):
  return a if a>=b else b

def isPerfectSquare(a):
  if int(math.sqrt(a)) * int(math.sqrt(a)) == a:
    return True
  else:
    return False 

def isPermutation(n1, n2):
  """ Returs if two input numbers are permutation of each other"""
  if len(str(n1)) != len(str(n2)):
    return False
  l1 = list(str(n1))
  for i in list(str(n2)):
    if i not in l1:
      return False
    l1.pop(l1.index(i))
  if len(l1) == 0:
    return True
  else:
    return False
  

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
  
def factorial(n):
  """Returns the facorial of a number"""
  if n ==1:
    return 1
  return n*factorial(n-1)

def combination(n,r):
  return (factorial(n) / (factorial(n-r) * factorial(r)) )
'''
def readHand(aHand):
  if isRoyalFlush(aHand):
    return 10
  if isStraightFlush(aHand):
    return 9+ (isStraightFlush(aHand)/10)
  if isFourKind(aHand):
    return 8+ (isFourKind(aHand)/10)
  if isFullHouse(aHand):
    return 7+ (isFullHouse(aHand)/10)
  if isFlush(aHand):
    return 6+ (isFlush(aHand)/10)
  if isStraight(aHand):
    return 5+ (isStraight(aHand)/10)
  if isThreeKind(aHand):
    return 4+ (isThreeKind(aHand)/10)
  if isTwoPair(aHand):
    return 3+ (isTwpPair(aHand)/10)
  if isPair(aHand):
    return 2+ (isPair(aHand)/10)
  else:
    return 1+ (highCard/10)
  
def isRoyalFlush(aHand):
  
def sortHand(aHand):
  for i in 
  '''

def isPalindrome(n):
  nList = list(str(n))
  for i in range(0,int(len(nList)/2)):
    if nList[i] != nList[-1*(i+1)]:
      return False
  return True

def isNotLychrel(n):
  i=0
  while i<50:
    i+=1
    if isPalindrome(n + invert(n)):
      return True
    else:
      n+=invert(n)
  return False

def invert(i):
  return int(str(i)[::-1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  