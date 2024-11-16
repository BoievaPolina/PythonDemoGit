#1) У вас є список my_list із значеннями типу int.
#Роздрукувати значення, які більше 100.
#Завдання виконати за допомогою циклу for.
print(1)
my_list = [52, 780, 20, 180, 101]

for value in my_list:
    if value > 100:
        print(value)

######################################################################
#2) У вас є список my_list зі значеннями типу int і порожній список my_results.
#Додати my_results ті значення, які більше 100.
#Роздрукувати список my_results.
#Завдання виконати за допомогою циклу for.
print(2)
my_list = [52, 780, 20, 180, 101]
my_results = []

for value in my_list:
    if value > 100:
        my_results.append(value)

print(my_results)

######################################################################
#3) У вас є список my_list із значеннями типу str. Створити новий список до якого помістити.
#елементи з my_list за таким правилом:
#Якщо строка стоїть на непарному місці my_list, то її замінити на обернену строку (Наприклад "qwe" на "ewq")
#Якщо на парному – залишити без зміни.
#Завдання зробити за допомогою циклу for та функції enumerate.
print(3)
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
new_list = []

for index, value in enumerate(my_list):
    if index % 2 == 0:
        new_list.append(value[::-1])
    else:
        new_list.append(value)

print(new_list)