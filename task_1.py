from pprint import pprint


def get_a_value_in_various_number_systems(amount_of_numbers) -> list[dict[str, str | int]]:
    list_of_digits = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)}
                      for num in range(amount_of_numbers+1)]
    return list_of_digits


pprint(get_a_value_in_various_number_systems(15))
