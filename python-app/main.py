import calendar

print ("Дорбо пожаловать в календарь\n")

year = int(input("Пожалуйста, введите год: "))
month = int(input("Пожалуйста, введите номер любого месяца: "))

print(calendar.month(year, month))
print("Всего хорошего!")