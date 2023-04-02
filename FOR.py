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
if 203>1000:
    priceperkg = 10
    for kg in range(1, 11):
        kg = kg/10
        total_price = priceperkg * kg
        print(f"{kg} кг конфет стоят {total_price} Гривен")
#6
if 30>56:
    #price_per_kg = 100
    price_per_kg = 10
    for kg in range(12, 21, 2):
        cost = price_per_kg * (kg / 10)
        print(f"{kg/10} кг конфет стоят {cost} гривен")
 #7
if 12>31:
    A = int(input("Введите число A: "))
    B = int(input("Введите число B: "))
    D = 0
    for i in range(A, B+1):
        print(i)
        D += i
    print("Сумма чисел от", A, "до", B, "включительно равна", D)
#8
if 32>303:
    a  = 11
    b = 20
    D = 1
    for i in range(a, b+1):   
        D = D*i
    print(D)
#9
if 32>304:
    A = 11
    B = 21
    summ = 0
    for i in range(A, B):
        summ = summ+pow(i, 2)
    print(summ)
#10
if 32>305:
    N = 14
    summ = 0
    for i in range(N+1):
        summ = summ+1/i
    print(summ)
#11
if 230<304:
    N = 14
    summ = 0
    for i in range(0, N+1):
        summ = summ+pow(N+i, 2)
    print(summ)
#12
if 230>304:
    N = 5
    number = 12
    result = 1.1
    for i in range(N):
        result *= (number + i) / 10
        print((number + i) / 10)

    print("Результат : ", result)
#13
if 230>304:
    N = 13
    number = 12
    result = 1.1
    for i in range(N):
        a = (number+i) / 10
        if i% 2 == 1:
            n = 1 
        else:
            n = -1
        result = (result + a)*n
    print(result)
#14
if 230>304:
    N = 28
    summ = 0
    for i in range(1, N+1):
        summ = summ+(2*i-1)
    print(summ)
#15
A = 2
N = 4
num = A
for i in range(N-1):
    print(i)
    num = num*A
print(num)





    



            
