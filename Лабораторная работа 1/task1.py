numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
newnumber = sum(numbers[:4]+numbers[5:])/len(numbers)
numbers[4] = newnumber
print("Измененный список:", numbers)
