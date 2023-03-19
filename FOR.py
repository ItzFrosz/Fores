#1
if 1 == 2:
    N = 10
    K = 20
    print(range (N))
    for x in range(N):
        print(K)
#2
if 2939>238489:
    A = 20
    B = 45
    i = 0
    for l in range(A,B+1):
        print(l)
        i = i+1
    print(i)
#3
if 4<3:
    A = 203
    B = 240
    B = B-1
    N = 0
    for l in range(B,A,-1):
        print(l)
        N = N+1
    print(N)

    A = 203
    B = 240
    B = B-1
    N = 0
    for l in range(B,A,-1):
        print(l)
        N = N+1
    print(N)

#4
if 4<3:
    priceperkg = float(input("Введите цену 1 кг конфет: "))

    for kg in range(1, 11):
        total_price = priceperkg * kg
        print(f"{kg} кг конфет стоят {total_price} Гривен")
#5
priceperkg = 10
for kg in range(1, 11):
    kg = kg/10
    total_price = priceperkg * kg
    print(f"{kg} кг конфет стоят {total_price} Гривен")
#6
#price_per_kg = 100
price_per_kg = 10
for kg in range(12, 21, 2):
    cost = price_per_kg * (kg / 10)
    print(f"{kg/10} кг конфет стоят {cost} гривен")
 #7
 
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
D = 0
for i in range(A, B+1):
    print(i)
    D += i
print("Сумма чисел от", A, "до", B, "включительно равна", D)
#8
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
proizvedenie = 1
for i in range(A, B+1):
    proizvedenie *= i
print("Произведение чисел от", A, "до", B, "включительно равно", proizvedenie)

    



            
