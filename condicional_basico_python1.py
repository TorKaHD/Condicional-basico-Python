# Comparación de números en Python, usando condicionales. Número 1.

def condicional_basico1 ():

    print ("Comparación de dos números")
    print ()

    c_numero1 = int (input ("Introduce el primer número..."))
    c_numero2 = int (input ("Introduce el segundo número..."))
    print ()

    # ---- Separación del código ----

    print ("----------------------------")
    print ()


    if c_numero1 > c_numero2:

        print ("El número 1 es más grande.")

        print ()

    elif c_numero1 < c_numero2: # "elif" es el "Else if" que se utilizan como condicional, otros lenguajes de programación como por ejemplo PHP.

        print ("El número 2 es más grande.")

        print ()

    elif c_numero1 == c_numero2:

        print ("Los dos números son iguales.")

        print ()

            # ---- Separación del código ----

    print ("----------------------------")
    print ()

condicional_basico1 ()
