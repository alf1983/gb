odd = 1
cubes = []
while odd < 1001:
    cubes.append(odd ** 3)
    odd += 2
sum_of_devs7 = 0
for current_item in cubes:
    hundred_billions = 0
    sum_of_digits = 0
    sum_of_digits += current_item // 100000000
    tens = 10000000
    while tens >= 10:
        sum_of_digits += (current_item % (tens * 10)) // tens
        tens /= 10
    sum_of_digits += current_item % 10
    if 0 == sum_of_digits % 7:
        sum_of_devs7 += current_item
indx = 0
sum2_of_devs7 = 0
while indx < (len(cubes)):
    cubes[indx] += 17
    indx += 1
for current_item in cubes:
    hundred_billions = 0
    sum_of_digits = 0
    sum_of_digits += current_item // 100000000
    tens = 10000000
    while tens >= 10:
        sum_of_digits += (current_item % (tens * 10)) // tens
        tens /= 10
    sum_of_digits += current_item % 10
    if 0 == sum_of_digits % 7:
        sum2_of_devs7 += current_item
print(sum_of_devs7)
print(sum2_of_devs7)