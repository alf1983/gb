duration = input("Введите кол-во секунд от 1 до 20-ти: ")
duration = int(duration)
if duration < 1 or duration > 20:
    print(duration, "не от 1 до 20-ти!")
    duration = input("Введите кол-во секунд от 1 до 20-ти: ")
duration = int(duration)
if duration == 1:
    declension = "секунда"
elif 1 < duration < 5:
    declension = "секунды"
else:
    declension = "секунд"
print(duration, declension)
