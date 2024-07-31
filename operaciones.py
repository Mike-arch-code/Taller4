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

    
    

    