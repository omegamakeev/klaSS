#Задание 1 
tourist_info = {
    "Фамилия": "Andriesh",
    "Страна": "Moldova",
    "Год": 2021,
    "Стоимость": 115000.00
}
print("\nИнфа")
for key, value in tourist_info.items():
    print(f"{key}: {value}")
    
tourist_info["Фамилия"] = input("\nВведите Фамилию: ")
tourist_info["Страна"] = input("Введите Страну: ")
tourist_info["Год"] = input("Введите год: ")
tourist_info["Стоимость"] = input("Введите стоимость: ")
print("\nИнфа")
for key, value in tourist_info.items():
    print(f"{key}: {value}")
    
#Задание 2 
A = float(input("Введите A: ")) #Ввод A
B = float(input("Введите B: ")) #Ввод B 
C = float(input("Введите C: ")) #Ввод C 
result = A * (B / 3.14) + (C * 3 + 5) #Решаем пример с наишими числами 
print(f"Ответ: {result}") #Выводим ответ на экран 
 
#Задание 3 
R, Y = map(float, input("Введите значение R и Y: ").split()) #Ввод Y И R на одной строке 
result1 = R ** Y + (Y / 2) #Решаем пример 
print(f"Ответ: {result1}") #Выводим ответ 



