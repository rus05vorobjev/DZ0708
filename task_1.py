"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
from array import *
nums = array ("i",[])
n = int(input("Введите кол-во элементов первого множества: "))
for x in range(0, n):
    newValue = int(input("Введите число: "))
    nums.append(newValue)
nums2 = array ("i",[])    
m = int(input("Введите кол-во элементов второе множества: "))
for x in range(0, m):
    newValue2 = int(input("Введите число: "))
    nums2.append(newValue2)
nums.extend(nums2)   

print(*set(nums))    

