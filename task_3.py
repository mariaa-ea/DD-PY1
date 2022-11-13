from random import randint


def get_unique_list_numbers(len_length, left_lim, right_lim) -> list[int]:
    """
    функция возвращает список из уникальных элементов.
    если введенное значение количества элементов списка больше его длины 
    или оно отрицательное, то выдается ошибка ValueError.

    :param len_length: задаваемая пользователем длина списка
    :param left_lim: левый предел задаваемого интервала
    :param right_lim: правый предел задаваемого интервала

    левый предел всегда меньше правого!

    остальные:
    len_different: длина интервала (включая ноль) при условии, что левая граница < 0,
    а правая - больше
    len_plus_or_minus: разница между модулями значений границ одного знака (нужна в условии,
    для сравнения длины, которая вычисляется приплюсовыванием единицы)

    :return: список из уникальных элементов
    """
    unique_list_numbers = []
    len_different = abs(left_lim) + abs(right_lim) + 1
    len_plus_or_minus = abs(left_lim) - abs(right_lim)
    if len_length < 0:
        raise ValueError("Введите неотрицательное число! Количество элементов не может быть отрицательным!")
        
    while len(unique_list_numbers) < len_length:
        num = randint(left_lim, right_lim)
        if num not in unique_list_numbers:
            unique_list_numbers.append(num)
        if left_lim < 0 < right_lim:
            if len_length > len_different:
                raise ValueError("(1) Указанное количество уникальных элементов превышает длину списка!")
        else:
            if len_length > abs(len_plus_or_minus) + 1:
                raise ValueError("(2) Указанное количество уникальных элементов превышает длину списка!")

    return unique_list_numbers


list_unique_numbers = get_unique_list_numbers(15, -10, 10)
print(f"Список: {list_unique_numbers} - имеет длину: {len(list_unique_numbers)}")
print(f"Проверка на уникальность: {len(list_unique_numbers) == len(set(list_unique_numbers))}")
