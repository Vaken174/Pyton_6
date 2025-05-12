def calculate_average(number_list: list) -> float | str:
    
    valid_numbers = []
    for element in number_list:
        if isinstance(element, (int, float)):
            valid_numbers.append(element)
        else:
            try:
                parsed_number = float(element)
                valid_numbers.append(parsed_number)
            except (ValueError, TypeError):
                return "Bad request"
    
    average_value = round(sum(valid_numbers) / len(valid_numbers), 2)
    return average_value


assert calculate_average([1, 1]) == 1
assert calculate_average([1, 2, 3, 4, 5]) == 3
assert calculate_average([-1, 1]) == 0
assert calculate_average([10, 20, 30, 40]) == 25

assert calculate_average([2.5, 3.5]) == 3.0
assert calculate_average([1.5, 2.5, 3.5]) == 2.5
assert calculate_average([0.1, 0.2, 0.3]) == 0.2

assert calculate_average(["1", "2", "3"]) == 2
assert calculate_average(["10.5", "20.5"]) == 15.5

assert calculate_average(["a", "b", "c"]) == "Bad request"
assert calculate_average([1, 2, "three"]) == "Bad request"


print("Все тесты прошли успешно!")