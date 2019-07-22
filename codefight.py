# add
def add(param1, param2):
  return param1 + param2

# centuryFromYear
def centuryFromYear(year):
 a = year//100
 if year%100 != 0:
  return a +1
 else:
  return a

#checkPalindrome
def checkPalindrome(inputString):
    return inputString == inputString[::-1]

#adjacentElementsProduct
def adjacentElementsProduct(inputArray):
 return max(inputArray[i]*inputArray[i+1] for i in range(len(inputArray)-1))

#shapeArea
def shapeArea(n):
 return n**2 + (n-1)**2

#makeArrayConsecutive2
def makeArrayConsecutive2(statues):
 return max(statues)-min(statues)-len(statues)+1

#almostIncreasingSequence
def almostIncreasingSequence(sequence):
    fails1 = 0
    fails2 = 0

    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            fails1 = fails1 + 1

    for i in range(len(sequence) - 2):
        if sequence[i] >= sequence[i + 2]:
            fails2 = fails2 + 1

    if (fails1 < 2) and (fails2 < 2):

        return True
    else:
        return False

#matrixElementsSum
def matrixElementsSum(matrix):
 doc= len(matrix)
 ngang= len(matrix[0])
 total = 0
 for j in range(ngang):
  for i in range(doc):
   if matrix[i][j]>0:
      total += matrix[i][j]
   else:
      break
 return total

#allLongestStrings
def allLongestStrings(inputArray):
   return [i for i in inputArray if len(i) == len(max(inputArray, key = len ))]

# commonCharacterCount
def commonCharacterCount(s1, s2):
 return sum(min(s1.count(x),s2.count(x)) for x in set(s1))

#isLucky
def isLucky(n):
  lst = list(str(n))
  sochuso = len(lst)
  nua1 = map(int, lst[:int(sochuso/2)])
  nua2 = map(int, lst[int(sochuso/2):])
  return sum(nua1) == sum(nua2)


#almostIncreasingSequence
def almostIncreasingSequence(sequence):
    fails1 = 0
    fails2 = 0

    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            fails1 = fails1 + 1

    for i in range(len(sequence) - 2):
        if sequence[i] >= sequence[i + 2]:
            fails2 = fails2 + 1

    if (fails1 < 2) and (fails2 < 2):

        return True
    else:
        return False

# isLucky
def isLucky(n):
  lst = list(str(n))
  sochuso = len(lst)
  nua1 = map(int, lst[:int(sochuso/2)])
  nua2 = map(int, lst[int(sochuso/2):])
  return sum(nua1) == sum(nua2)

# sortByHeight
def sortByHeight(a):
    l = sorted([index for index in a if index != -1])
    for index in [index for index, value in enumerate(a) if value == -1]:
        l.insert(index, -1)
    return l


#reverseInParentheses
def reverseInParentheses(input):
    # return inputString.replace("(", "").replace(")", "")[::-1]
    char = list(input)
    mangtam = []
    for i, c in enumerate(char):
        if c == '(':
            mangtam.append(i)
        elif c == ')':
            j = mangtam.pop()
            char[j:i] = char[i:j:-1]
    return ''.join(c for c in char if c not in '()')

# alternatingSums
def alternatingSums(a):
    return [sum(a[::2]),sum(a[1::2])]
#areSimilarareSimilar
from collections import Counter as C
def areSimilar(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3

# arrayChange
def arrayChange(inputArray):
    i = 1
    sum = 0
    while i < len(inputArray):
        if inputArray[i] <= inputArray[i-1]:
            sum += (inputArray[i-1] - inputArray[i]) + 1
            inputArray[i] += (inputArray[i-1] - inputArray[i]) + 1
        i += 1
    return sum

# addBorder
def addBorder(picture):
    l = len(picture) + 2
    return ["*" * l] + [x.center(l, "*") for x in picture] + ["*" * l]

# palindromeRearranging
def palindromeRearranging(input):
    dict = {}
    for c in input:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1

    list = [l for l in dict if dict[l] % 2]
    if len(list) > 1:
        return False
    else:
        return True

# areEquallyStrong
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}

# arrayMaximalAdjacentDifference
def arrayMaximalAdjacentDifference(a):
    diffs=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)







