#!/usr/bin/python
from euler.EulerUtils import add, isPermutation, isPrime, isGreater, multiply, isPerfectSquare
from euler.EulerUtils import primes
import math
import sys
from scipy.signal.waveforms import square

def euler7():
  primesList=[]
  counter=2
  while 1:
    if isPrime(counter):
      primesList.append(counter)
    counter += 1
    if len(primesList) == 10001:
      break
  print primesList[-1]

def euler8():
  
  L = []
  L.append("73167176531330624919225119674426574742355349194934")
  L.append("96983520312774506326239578318016984801869478851843")
  L.append("85861560789112949495459501737958331952853208805511")
  L.append("12540698747158523863050715693290963295227443043557")
  L.append("66896648950445244523161731856403098711121722383113")
  L.append("62229893423380308135336276614282806444486645238749")
  L.append("30358907296290491560440772390713810515859307960866")
  L.append("70172427121883998797908792274921901699720888093776")
  L.append("65727333001053367881220235421809751254540594752243")
  L.append("52584907711670556013604839586446706324415722155397")
  L.append("53697817977846174064955149290862569321978468622482")
  L.append("83972241375657056057490261407972968652414535100474")
  L.append("82166370484403199890008895243450658541227588666881")
  L.append("16427171479924442928230863465674813919123162824586")
  L.append("17866458359124566529476545682848912883142607690042")
  L.append("24219022671055626321111109370544217506941658960408")
  L.append("07198403850962455444362981230987879927244284909188")
  L.append("84580156166097919133875499200524063689912560717606")
  L.append("05886116467109405077541002256983155200055935729725")
  L.append("71636269561882670428252483600823257530420752963450")
  
  numbers = list(''.join(L))
  productList = []
  print numbers
  for index_i in range(len(numbers)):
    if index_i > len(numbers)-5:
      break
    number=[int(j) for j in numbers[index_i:index_i+5]]
    print number, index_i
    productList.append(reduce(multiply,number))
  print reduce(isGreater,productList)




def euler9():
#   a2 + b2 = c2; a+b+c=1000
    squaresList=[]
    for i in range(4,1000000):
      if isPerfectSquare(i):
        squaresList.append(i)
    for i in squaresList:
      for jIndex in range(squaresList.index(i)+1, len(squaresList)):
        j=squaresList[jIndex]
        potentialK=i+j
        if potentialK in squaresList and math.sqrt(i)+math.sqrt(j)+math.sqrt(potentialK) ==1000:
          print math.sqrt(i)*math.sqrt(j)*math.sqrt(potentialK)



def euler10():
  sum=0
  for i in range(200000):
    if isPrime(i):
      sum += i
  print sum

def euler10_():
  returnList = primes(2000000)
  
#   print returnList
  print reduce(add,returnList)
  
def main():
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored

#   euler7()
#   euler8()
#   euler9()
  euler10_()
if __name__ == '__main__':
  main()
