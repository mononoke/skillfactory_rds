import numpy as np


def think_number(span):
    # загадываем число в пределах {span}
    return np.random.randint(span[0], span[1])


def guess_number(span):
    """Функция принимает диапозон чисел и возвращает число шагов, за которое
    удалось его угадать.

    Используем бинарный поиск: сначала берем число посередине
    загаданного диапозона, затем, отталкиваясь от того,
    больше или меньше загаданное число, на каждом шаге сокращаем диапозон
    поиска в 2 раза. На последних шагах сокращаем диапозон на единицу"""

    number = think_number(span)  # загаданное число
    step = 1  # количество шагов
    predict = (span[1] - 1) // 2  # средне-арифметическое в загаданном диапозоне {span}

    while number != predict:
        step += 1

        # на сколько нужно уменьшить/увеличить искомое число
        increment = round(100 / (2 ** step))
        if increment == 0:
            increment = 1

        if number > predict:
            predict = predict + increment
        else:
            predict = predict - increment

    return step


def benchmark(span):
    repetitions = 1000
    # Запускаем игру {repetitions} раз, чтобы узнать среднее количество шагов, за которое угадывается число

    steps = list()

    for i in range(repetitions + 1):
        steps.append(guess_number(span))

    average = sum(steps) / repetitions
    return average


average_steps_number = benchmark((1, 101))
round_steps_number = round(average_steps_number)
print(f"Ваш алгоритм угадывает число в среднем за {round_steps_number} ({average_steps_number}) попыток")
