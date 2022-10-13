list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# max_index = 0
# for i in range(len(list_numbers)):
#     max_value = list_numbers[max_index]
#     index_value = list_numbers[i]
#     if index_value > max_value:
#         max_index = i

max_index = 0
for pos, value in enumerate(list_numbers):
    max_value = list_numbers[max_index]
    if value > max_value:
        max_value = value
        max_index = pos

list_numbers[-1], list_numbers[max_index] = list_numbers[max_index], list_numbers[-1]
print(list_numbers)
