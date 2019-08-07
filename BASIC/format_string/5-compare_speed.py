import timeit


def old_format1():
    name = "Eric"
    age = 74
    '%s is %s.' % (name, age)


def old_format2():
    name = "Eric"
    age = 74
    '{} is {}.'.format(name, age)


def new_format():
    name = "Eric"
    age = 74
    f"{name} is {age}"


def main():
    print(timeit.timeit('old_format1()', 'from __main__ import old_format1'))

    print(timeit.timeit('old_format2()', 'from __main__ import old_format2'))

    print(timeit.timeit('new_format()', 'from __main__ import new_format'))

# Để hiểu rõ cách gọi timeit.timeit hãy xem link này https://stackoverflow.com/questions/54135771/timeit-valueerror-stmt-is-neither-a-string-nor-callable

if __name__ == '__main__':
    main()
