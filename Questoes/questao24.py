t1 = 1
t2 = 1
print("Os 20 primeiros termos da serie de Fibonacci")
print("Fibonacci = 1,1", end=",")

contador = 2
while contador < 20:
    t3 = t1 + t2
    print(f"{t3}", end=",")
    contador += 1
    t1, t2 = t2, t3
