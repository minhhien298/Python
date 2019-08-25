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

# isIPv4Address
def isIPv4Address(s):
    p = s.split('.')
    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

# avoidObstacles
def avoidObstacles(input):
    i = 2
    while True:
        if all(x%i!=0 for x in input):
            return i
        i+=1

# boxBlurdq
def boxBlur(image):
    return   [[int(sum(sum(x[i:i+3]) for x in image[j:j+3])/9) for i in range(len(image[j])-2)]for j in range(len(image)-2)]

# boxBlurdq
def boxBlur(m):
    r = len(m)
    c = len(m[0])
    ans = []
    for i in range(1,r-1):
        row=[]
        for j in range(1,c-1):
            row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
        ans.append(row)
    return ans

# minesweeper
def minesweeper(matrix):
    def _3x3(i,j):
        return (matrix[i+x][j+y] for x in {-1,0,1} if 0 <= i+x < len(matrix)
                                 for y in {-1,0,1} if 0 <= j+y < len(matrix[0])
                                 if not x == y == 0)

    return [
            [ sum(elem for elem in _3x3(i,j)) for j in range(len(matrix[0]))]
             for i in range(len(matrix))
           ]

# arrayReplace
def arrayReplace(i, e, s):
    return [x if x!=e else s for x in i]
# evenDigitsOnly
def evenDigitsOnly(n):
    return all([int(i)%2==0 for i in str(n)])





