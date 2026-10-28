import random
import string
import itertools


def infinite_random_generator():
    """Бесконечный генератор случайных данных разных типов."""
    generators = [
        lambda: random.randint(0, 1000),
        lambda: round(random.uniform(0, 100), 2),
        lambda: ''.join(random.choices(string.ascii_lowercase, k=6)),
        lambda: random.choice([True, False]),
    ]
    for gen in itertools.cycle(generators):
        yield gen()


if __name__ == '__main__':
    gen = infinite_random_generator()
    print("Первые 12 случайных значений:")
    for _ in range(12):
        print(next(gen))
