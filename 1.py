duration = input("Input duration: ")
duration = int(duration)
minutes = 0
hours = 0
days = 0
seconds = duration % 60
minutes = duration // 60
if minutes > 60:
    hours = minutes // 60
    minutes = minutes % 60
    if hours > 24:
        days = hours // 24
        hours = hours % 24
if days > 0:
    print(days, "дней", end=" ")
if hours > 0:
    print(hours, "часов", end=" ")
if minutes > 0:
    print(minutes, "минут и", end=" ")
print(seconds, "секунд")
