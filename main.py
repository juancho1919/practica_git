#importacion de archivos
from functions import sumar_n
from calculos import area_c,area_t,area_cir

#programas
print("hola mundo")



while True:
    print("-------------------MENU------------------")
    print("opcion (1) area del triangulo" )
    print("opcion (2) area del cuadrado" )
    print("opcion (3) sumar" )
    print("opcion (4) area del circulo" )
    print("opcion (0) terminar" )
    
    opcion = input()
    if opcion == "1":
        base = int(input("digite la base: "))
        altura = int(input("digite la altura: "))
        print(area_t(base,altura))
    elif opcion == "2":
        lado = int(input("digite el lado del cuadrado: "))
        print(area_c(lado))
    elif opcion == "3":
        a = float(input("digite el primer numero: "))
        b = float(input("digite el segundo numero: "))
        resultado = sumar_n(a,b)
        print(resultado)
    elif opcion == "4":
        radio = str(input("digite el radio: "))
        print(area_cir(radio))
    else:
        opcion == "0"
        print("programa terminado")
        break




      





