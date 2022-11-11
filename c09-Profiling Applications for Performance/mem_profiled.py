from memory_profiler import profile


@profile
def calc_sum():
    sum = 0
    for i in range(100):
        sum = sum + i
    print(str(sum))


def say_hello():
    lst = []
    for i in range(10000):
        lst.append(i)


@profile
def calc_sum_hi():
    sum = 0
    for i in range(100):
        sum = sum + i
        say_hello()
    print(str(sum))


if __name__ == '__main__':
    calc_sum()
    calc_sum_hi()
