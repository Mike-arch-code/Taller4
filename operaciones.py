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