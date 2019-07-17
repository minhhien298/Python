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





