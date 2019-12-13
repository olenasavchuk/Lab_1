import copy

print("Буде створено двовимірний список розмірністю [n][n]")
while True:
    try:
        n = int(input("Введіть n: "))
        break
    except ValueError:
        print("Введіть ціле число")


while True:
    while True:
        try:
            print(f"Введіть через кому послідовність {n*n} цілих чисел : ")
            l =  list(map(int,input().split(",")))
            break
        except ValueError:
            print("Потрібно вводити цілі числа!")
    if len(l) == n*n:
        break
    else:
        print(f"Потрінбо ввести {n*n}!!! цілих чисел")

a = []
for i in range(n): 
    a.append([])
    for j in range(n): 
        a[i].append(l[i*n+j])

matrix = copy.deepcopy(a)

for i in range(n): 
    for j in range(n): 
        matrix[i][j] = matrix[n-j-1][n-i-1]

for r in a:
    print(r)

if a == matrix:
    print("Список симетричний відносно неголовної осі")
else:
    print("Список не симетричний відносно неголовної осі")

