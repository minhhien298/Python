import numpy as np

def zigzag(n):
    def move(i, j):
        if j < (n - 1):
            return max(0, i - 1), j + 1
        else:
            return i + 1, j

    a = [[0] * n for _ in range(n)] #tao ma tran vuong n*n toan` 0
    x, y = 0, 0
    for v in range(n * n):
        a[y][x] = v
        if (x + y) & 1:
            x, y = move(x, y)
        else:
            y, x = move(y, x)
    return a

print(np.matrix(zigzag(10)))


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




