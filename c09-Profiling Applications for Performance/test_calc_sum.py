import time
import timeit


def calc_sum():
    sum = 0
    for i in range(0, 100):
        sum = sum + i
    return sum


def time_profile(func):
    """Decorator for timing the execution of a method."""

    def timer_func(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        total_time = end - start
        output_msg = "The method {func} took {total_time} to execute"
        print(output_msg.format(func=func, total_time=total_time))
        return value

    return timer_func


test_calc_sum_profiled = time_profile(calc_sum)

if __name__ == '__main__':
    print(timeit.timeit("calc_sum()", setup="from __main__ import calc_sum"))
