class A(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return A(self.num + other.num)


def get_num(self):
    return self.num


A.get_num = get_num
