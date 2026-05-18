def divisoresDeUnNumero(numero):
    sumatoriaDeDivisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            sumatoriaDeDivisores += i
    return sumatoriaDeDivisores

num1 = int(input("Ingresá un número: "))
num2 = int(input("Ingresá otro número: "))

res1 = divisoresDeUnNumero(num1)
res2 = divisoresDeUnNumero(num2)

if  num2 == res1 and num1 == res2:
    print("Son números amigos!")
else:
    print("No son números amigos.")
