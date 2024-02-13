from sys import stdin

"""
lines = []
result = []
for line in stdin.readlines():
    line = line.rstrip('\n')
    lines.append(line)
for words in lines:
    if lines[-1] in words.lower():
        result.append(words)
print(*result[:result.index(result[-1])], sep='\n')
"""

# ----- Обновлю Ваш код так, чтобы он стал оптимальнее -----


lines = stdin.readlines()  # 1. Этой строкой кода, я заменил Ваш первый цикл
# В этой переменной все строки, включая сам запрос
# (он является последним элементом).

# 2. Теперь применим оператор упаковки/распаковки * (зведочка)
*headers, query = lines  # 3. Важно, также можно было не
# создавать переменную lines, написать следующем образом
# *headers, query = stdin.readlines(), но это уже Вам решать.

# headers - хранятся заголовки
# query - сам запрос

query = query.rstrip().lower()  # 4. Запрос очистим, и приводим
# к ниженму регистру

# 5. Тут уже обычная проверка в цикле.
result = []
for line in headers:
    if query in line.lower():
        result.append(line.rstrip('\n'))

print('\n'.join(result))
