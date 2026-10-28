def curry(func):
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more: curried(*(args + more))
    return curried


@curry
def add(a, b, c):
    return a + b + c


if __name__ == '__main__':
    print(add(1)(2)(3))      # 6
    print(add(1, 2)(3))      # 6
    print(add(1)(2, 3))      # 6
    print(add(1, 2, 3))      # 6

    multiply = curry(lambda a, b: a * b)
    double = multiply(2)
    print(double(5))         # 10
    print(double(10))        # 20
