import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
bins = [20, 25, 30, 35, 40, 45, 50, 55, 60]
df = pd.read_csv("numpy/1000employee.csv")
age_group = df.groupby([pd.cut(df.Age, bins)]).size()
print(age_group)
age_group.plot(kind='bar')
plt.show()

'''
import pandas as pd
s2 = pd.Series(['a','b','c','d'])
print(s2)


s3 = pd.Series(['a','b','c','d'], index=[100, 101, 102, 103])
print(s3)


s4 = pd.Series(['Microsoft','Google','Apple','Facebook'], index=['MSFT', 'GOL', 'APL', 'FCB'])
print(s4)
'''

'''
def getMatrixSize():
    print("Enter N size of zigzag matrix:")
    rawN = int(input())
    N = 5
    if rawN is not None:
          if rawN > 4:
            N = rawN
    return N

def buildZigZag(N):
    arr = []
    num = arr
    for k in range(1, 2*N-2):
        if k < N:
         start = 0
        else:
         start = k - N + 1

    for i in range(start, (k-start)):
        j = k-i
        if k%2 == 0:
            arr[j][i] = num
        else:
            arr[i][j] = num
        num+=1
    return  arr

if __name__ == "__main__":
    N1 = getMatrixSize()
    result = buildZigZag(N1)
    for i in range(0,N1):
        for j in range(0,N1):
            print('{:4}'.format(result[i][j]),
        print())
'''




