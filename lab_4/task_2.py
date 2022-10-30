# def get_count_char(str_):
#     bukva_dict = {}
#     str_ = "".join(str_.lower().split())
#     for bukva in str_:
#         if bukva.isalpha():
#             if bukva in bukva_dict:
#                 bukva_dict[bukva] += 1
#             else:
#                 bukva_dict[bukva] = 1
#     bukva_dict = dict(sorted(bukva_dict.items()))
#     return bukva_dict

def get_count_char(str_):
    bukva_dict = {}
    str_ = "".join(str_.lower().split())
    str_ = "".join(bukva for bukva in str_ if bukva.isalpha())
    for bukva in str_:
        bukva_dict[bukva] = bukva_dict.get(bukva, 0) + 1
    bukva_dict = dict(sorted(bukva_dict.items()))
    return bukva_dict

def frequency_of_occurrence(str_):
    number_dict = {}
    for num, value in get_count_char(main_str).items():
        number_dict[num] = round(value/sum(get_count_char(main_str).values())*100, 2) 
    return number_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(frequency_of_occurrence(main_str))
