numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers_1 = numbers[:4]  # порядок чисел до None
numbers_2 = numbers[5:20]  # порядок чисел после None
numbers_sum = numbers_1 + numbers_2  # список чисел без None

None_arithmetic_mean = round(sum(numbers_sum) / len(numbers), 2)
numbers[4] = None_arithmetic_mean

print("Измененный список:", numbers)
