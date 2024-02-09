from sys import stdin

total_sum = 0
for line in stdin.readlines():
    # example = line.rstrip('\n').split()  # здесь у вас строка очищается от
    # символа переход на новую строку и разбивается на элементы по пробелам

    # Далее из этого списка начинаете перебирать
    # числа (по сути из текущей строки)
    for num in line.rstrip('\n').split():
        total_sum += int(num)  # И суммируем

print(total_sum)
