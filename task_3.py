from random import randint


def get_unique_list_numbers(len_length, left_lim, right_lim) -> list[int]:
    unique_list_numbers = []
    while len(unique_list_numbers) < len_length:
        num = randint(left_lim, right_lim)
        if num not in unique_list_numbers:
            unique_list_numbers.append(num)
        if len(unique_list_numbers) > abs(left_lim) + abs(right_lim) + 1:
            print("Заданное количество элементов списка больше длины "
                  "интервала! Исправьте введенные значения!")
            break
    return unique_list_numbers


list_unique_numbers = get_unique_list_numbers(15, -10, 10)
print(f"Список: {list_unique_numbers} - имеет длину: {len(list_unique_numbers)}")
print(f"Проверка на уникальность: {len(list_unique_numbers) == len(set(list_unique_numbers))}")
