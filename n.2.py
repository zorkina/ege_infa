# эта часть кода остается неизменной
f = open('2.txt')
a = []
number_of_lines = 0
for line in f:
    x, y = map(int, line.split())
    a.append((x, y))
    number_of_lines += 1
f.close()
count = 0

for i in range(number_of_lines):
    x, y = a[i]
    # прописываем новые условия
    # сначала для удобства начнем с простого и пропишем зеленое и красное условие
    if  -4 <= y <= 3 and  -1 <= x <= 3:
        # теперь синее и оранжевое
        if (y <= x + 2) and (y >= x - 4):
            count += 1
print(count)

