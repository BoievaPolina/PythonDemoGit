#1. Дано ціле число (int). Порахувати скільки нулів в цьому числі.
number = int(input("Введіть ціле число: "))
count_zeros = str(number).count('0')
print("Кількість нулів:", count_zeros)

#2. Дано ціле число (int). Порахувати скільки нулів в кінці цього числа. Наприклад для числа 1002000 - три нулі
number = int(input("Введіть ціле число: "))
count_trailing_zeros = len(str(number)) - len(str(number).rstrip('0'))
print("Кількість нулів в кінці:", count_trailing_zeros)

#3. Дан список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший элемент з my_list
#стоїть на останньому месці в new_list. Якщо my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = [1, 2, 3, 4]
new_list = my_list[1:] + my_list[:1]
print(new_list)

#4. Дана строка в якій є числа (разділяються пробілами).
#Наприклад "43 більше за 34, але меньше за 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) в цій строкі.
#Для даного прикладу відповідь - 133. (використайте split и перевірку isdigit)
text = "43 більше за 34, але меньше за 56"
numbers = [int(word) for word in text.split() if word.isdigit()]
total = sum(numbers)
print(total)

#5. Дана строка my_str. Разділіть цю строку на пари з двох символів и поместіть ці пари в список.
#Якщо строка має непарну кількість символів, останній символ останньої пари має
#бути підкресленням ('_'). Приклади: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
#(використовуйте зрізи довжиною 2 символи)
my_str = "abcde"
if len(my_str) % 2 != 0:
    my_str += '_'
pairs = [my_str[i:i+2] for i in range(0, len(my_str), 2)]
print(pairs)

#6. Дан список чисел. Порахуйте, скольки в цьому списку елементів,
#які більше за суму двох своїх сусідів (зліва и справа), и НАДРУКУЙТЕ КІЛЬКІСТЬ таких елементів.
#Крайні елементи списку не враховувати, оскільки в них недостньо сусідів.
#Для списка [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4 > 2+1, 5 > 1+3, 9>3+0.  напиши код на мові python
numbers = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0
for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] + numbers[i + 1]:
        count += 1
print(count)
