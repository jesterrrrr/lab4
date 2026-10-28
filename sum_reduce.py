from functools import reduce


def sum_numbers(lst):
    return reduce(lambda x, y: x + y, lst)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Список: {numbers}")
    print(f"Сумма: {sum_numbers(numbers)}")
