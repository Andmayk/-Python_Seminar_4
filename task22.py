# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

# str1 = "2 4 6 8 10 12 10 8 6 4 2"
# str2 = "3 6 9 12 15 18"

str1 = input(f"Введите числа первого набора через пробел их должно быть {n}: ")
str2 = input(f"Введите числа второго набора через пробел их должно быть {m}: ")

set1 = set(map(int, str1.split()))
set2 = set(map(int, str2.split()))

inter_section = set1.intersection(set2)

# на случай если множество получилось не отсортированное
sorted_list = []
sorted_list = list(inter_section)
sorted_list.sort()

print(*sorted_list)
