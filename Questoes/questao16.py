dia = int(input("dia:"))
mes = int(input("mes:"))

if mes == 3 and dia >= 21 or mes == 4 and dia <= 20:
    print("Aries")
if mes == 4 and dia >= 21 or mes == 5 and dia <= 20:
    print("Touro")
if mes == 5 and dia >= 21 or mes == 6 and dia <= 20:
    print("Gemeos")
if mes == 6 and dia >= 21 or mes == 7 and dia <= 21:
    print("Cancer")
if mes == 7 and dia >= 22 or mes == 8 and dia <= 22:
    print("Leão")
if mes == 8 and dia >= 23 or mes == 9 and dia <= 23:
    print("Virgem")
if mes == 9 and dia >= 23 or mes == 10 and dia <= 22:
    print("Libra")
if mes == 10 and dia >= 23 or mes == 11 and dia <= 21:
    print("Escorpiao")
if mes == 11 and dia >= 22 or mes == 12 and dia <= 21:
    print("Sagitario")
if mes == 12 and dia >= 22 or mes == 1 and dia <= 20:
    print("Capricornio")
if mes == 1 and dia >= 21 or mes == 2 and dia <= 19:
    print("Aquario")
if mes == 2 and dia >= 20 or mes == 3 and dia <= 20:
    print("Peixes")

if mes == 3:
    if dia <= 20:
        print("peixes")
    else:
        print("aries")

if mes == 1:
    if dia <= 20:
        print("Capricornio")
    else:
        print("Aquario")