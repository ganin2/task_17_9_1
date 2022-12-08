spisok = input("Введите последовательность чисел через пробел: ")
spisok_list = [int(a) for a in spisok.split()]
if (' ' not in (spisok)):
    raise ValueError("Введены некорректные данные! Введите последовательность чисел через пробел!")

num = int(input("Введите любое число: "))
if num % 1 == 0:
    spisok_list.append(num)
    print("Список до сортировки: ", spisok_list)
min = 0
def spisok_sort(spisok_list):
    for i in range(len(spisok_list)):  # проходим по всему массиву
        min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(spisok_list)):
            if spisok_list[j] < spisok_list[min]:
                min = j
        if i != min:  # если индекс не совпадает с минимальным, меняем
            spisok_list[i], spisok_list[min] = spisok_list[min], spisok_list[i]
    return spisok_list
print("Список после сортировки:", spisok_sort(spisok_list))

def binary_search(spisok_list, num, low, high):
    middle = (low + high) // 2
    if low > high:
            return f'Номер позиции элемента, который меньше введенного числа: {middle}\n'\
                   f'Номер позиции элемента, который больше или равен введенному числу: {middle + 1}'
    elif spisok_list[middle] == num:
            return f'Номер позиции элемента, который меньше введенного числа: {middle - 1}\n'\
                   f'Номер позиции элемента, который больше или равен введенному числу: {middle}'
    elif spisok_list[middle] > num:
            return binary_search(spisok_list, num, low, middle - 1)
    else:
            return binary_search(spisok_list, num, middle + 1, high)
print(binary_search(spisok_list, num, 0, len(spisok_list)-1))