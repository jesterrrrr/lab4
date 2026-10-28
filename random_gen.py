import random


def random_generator(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)


if __name__ == '__main__':
    gen = random_generator(1, 100, 10)
    numbers = list(gen)
    print(f"10 случайных чисел от 1 до 100: {numbers}")
