f = open('1.txt')
# пустой список для хранения пар чисел
a = []
# подсчет количества строк в файле
number_of_lines = 0
for line in f:
    # преобразуем строку в два числа x и y
    x, y = map(int, line.split())
    a.append((x, y))
    number_of_lines += 1
f.close()

# счетчик для подсчета ответа
count = 0

# проверяем каждую пару чисел в списке a
for i in range(number_of_lines):
    # проверяем, попадают ли числа x и y в диапазон от -3 до 3 включительно
    if -3 <= a[i][0] <= 3 and -3 <= a[i][1] <= 3:
        # если попадают, увеличиваем счетчик ответа
        count += 1

print(count)
