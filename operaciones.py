def producto_directo():

    while True:
        try:
            n = int(input("Dijite la catidad de  n numeros para los conjuntos:"))
            break
        except:
            print("El valor ingresado no es un número entero. Intente de nuevo.")

    v = [None] * n
    w = [None] * n
    
    i = 0
    while i < n:
        try:
            v[i] = float(input("Dijite 1 numero para el conjunto v :"))
            i += 1
        except ValueError:
            print("El valor ingresado no es un número real. Intente de nuevo.")
    i = 0
    while i < n:
        try:
            w[i] = float(input("Dijite 1 numero para el conjunto w :"))
            i += 1
        except ValueError:
            print("El valor ingresado no es un número real. Intente de nuevo.")


    producto = [a * b for a, b in zip(v, w)]

    print("Conjunto v:",v)
    print("Conjunto w:",w)
    print("Producto directo:",producto)


def promedio():
    numeros_conjunto = [None] * 8
    i = 0
    sum  = 0
    while i < 8:
        try:
            numeros_conjunto[i] = float(input("Dijite 1 numero: "))
            sum = sum + numeros_conjunto[i]
            i += 1
        except ValueError:
            print("El valor ingresado no es un número real. Intente de nuevo.")

    print("El conjunto de numeros es:",numeros_conjunto)

    promedio_numeros = sum / 8 

    print("El promedio es:",promedio_numeros)


def producto_punto():

    while True:
        try:
            n = int(input("Dijite la catidad de  n numeros para los conjuntos:"))
            break
        except:
            print("El valor ingresado no es un número entero. Intente de nuevo.")

    v = [None] * n
    w = [None] * n

    i = 0
    while i < n:
        try:
            v[i] = float(input("Dijite 1 numero para el conjunto v :"))
            i += 1
        except ValueError:
            print("El valor ingresado no es un número real. Intente de nuevo.")
    i = 0
    while i < n:
        try:
            w[i] = float(input("Dijite 1 numero para el conjunto w :"))
            i += 1
        except ValueError:
            print("El valor ingresado no es un número real. Intente de nuevo.")


    producto = sum(a * b for a, b in zip(v, w))

    print("Conjunto v:",v)
    print("Conjunto w:",w)

    print("El producto punto de los vectores es:",producto)