class A(object):
    x = 1


class B(A):
    pass


class C(A):
    pass


print(A.x, B.x, C.x)  # 1 1 1

B.x = 2
print(A.x, B.x, C.x)  # 1 2 1

A.x = 3
print(A.x, B.x, C.x)  # 3 2 3  tại sao vậy?

'''
C doesn’t have its own x property, independent of A. 
Thus, references to C.x are in fact references to A.x

C kế thừa từ A, C không thực sự sở hữu thuộc tính x mà nó tham chiếu đến thuộc tính x của A
'''