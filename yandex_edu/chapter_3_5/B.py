from sys import stdin

"""
data = []
people = []
sum_new_growth = 0
sum_old_growth = 0
for line in stdin.readlines():
    line = line.rstrip()
    for num in line.rstrip('\n').split():
        if num.isdigit():
            data.append(int(num))
        else:
            people.append(num)
for i in range(len(data)):
    if i % 2 == 0:
        sum_old_growth += data[i]
    else:
        sum_new_growth += data[i]
medium_height = (sum_old_growth - sum_new_growth) // len(people)
print(abs(round(medium_height, 2)))
"""

# ----- Я предлагаю следующий вариант -----

# 1. Нам нужны только значение ростов,
# так что я буду игнорировать имена учеников.

data: list[str] = stdin.readlines()

# Для хранения ростов не нужно создавать
# целых список, можем их сразу складывать


total_prev_height: int = 0
total_new_height: int = 0
for line in data:
    # *_ первая переменная это имя, берем только последних два значения
    *_, prev_height, new_height = line.rstrip().split()

    total_prev_height += int(prev_height)
    total_new_height += int(new_height)

num_of_students: int = len(data)

result: float = (
        (total_new_height / num_of_students)
        - (total_prev_height / num_of_students)
)

print(round(result))
