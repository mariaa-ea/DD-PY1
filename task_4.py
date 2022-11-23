import json


INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=', ', new_line='\n') -> list[dict] | None:
    f"""
    Функция открывает файл в режиме по умолчанию (чтения). 
    Читает первую строку, убирает переход на новую и создает список из слов, убирая {delimiter} между ними.
    Затем с помощью функции zip(), которая позволяет создать массив словарей по принципу ключ-значение, 
    где ключ - все значения списка read_headers, значение - высчитывается через цикл for: 
    берет строку в цикле, удаляет пробелы в конце и символы между значениями -> из них создается список, 
    а затем берется нужное значение и записывается в словарь.
    
    В случае, если не удается прочитать файл - выдается ошибка.
    
    :param filename: задаваемое пользователем имя файла для записи.
    :param delimiter: разделитель между значениями.
    :param new_line: разделитель строк. 
    
    Остальные: 
    read_headers: список из заголовков. 
    zipped_dict: список массива словарей.
    
    :return: zipped_dict, в случае ошибки при открытии файла - None.
    """
    try:
        with open(filename) as f:
            read_headers = f.readline().rstrip(new_line).split(delimiter)
            zipped_dict = [dict(zip(read_headers, row.strip().split(delimiter))) for row in f]
    except OSError:
        print(f"Прочитать файл '{filename}' не удалось!")
        return None
    return zipped_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

with open('output.json', 'w') as out_f:
    json.dump(csv_to_list_dict(INPUT_FILE), out_f, indent=4)
