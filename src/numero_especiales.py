#Entrada

def solicitar_numero_inicial():
    numero_inicial = input("Ingrese el número inicial: ")
    while numero_inicial.isdecimal():
        numero_inicial = input("Ingrese el número inicial: ")
    return int(numero_inicial)

def solicitar_numero_final():
    numero_final = input("Ingrese el número final: ")
    while numero_final.isdecimal():
        numero_final = input("Ingrese el número final: ")
    return int(numero_final)

def solicitar_suma_de_pares_o_impares()->str:
    opcion_escogida = input("¿Desea calcular la suma de pares o impares? (pares/impares): ")
    while opcion_escogida.lower() != "pares" and opcion_escogida.lower() != "impares":
       opcion_escogida = input("¿Desea calcular la suma de pares o impares? (pares/impares): ")
    return opcion_escogida.lower()

#Procesado

def crear_rango(numero_inicial:int,numero_final:int)->list:
    rango_de_numeros = []
    if numero_inicial < numero_final:
        for numero in range(numero_inicial,numero_final+1):
            rango_de_numeros.append(numero)
        return rango_de_numeros

def sacar_multiplo_3(lista_numeros:list)-> bool:
    lista_sin_multiplos_de_3= []
    for posible_multiplo_de_3 in lista_numeros:
        if posible_multiplo_de_3 % 3 != 0:
            lista_sin_multiplos_de_3.append(posible_multiplo_de_3)
    return lista_sin_multiplos_de_3

def obtener_pares(lista_numeros:list)->list:
    lista_pares = []
    for par in lista_numeros:
        if par % 2 == 0:
            lista_pares.append(par)
    return lista_pares

def obtener_impares(lista_numeros:list)-> list:
    lista_impares = []
    for par in lista_numeros:
        if par % 2 != 0:
            lista_impares.append(par)
    return lista_impares

def suma_de_lista(lista_numeros:list)->int:
    return sum(lista_numeros)

#Salida
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    numero_inicial = solicitar_numero_inicial()
    numero_final = solicitar_numero_final()

    lista_de_numeros_sacados = crear_rango(numero_inicial, numero_final)
    opcion_suma = solicitar_suma_de_pares_o_impares()

    lista_sin_multiplo_de_3 = sacar_multiplo_3(lista_de_numeros_sacados)

    if opcion_suma == "impar":
        lista_impares = obtener_impares(lista_sin_multiplo_de_3)
        resultado_impares = suma_de_lista(lista_impares)
        print(resultado_impares)
    if opcion_suma == "par":
        lista_pares = obtener_pares(lista_sin_multiplo_de_3)
        resultado_pares = suma_de_lista(lista_pares)
        print(resultado_pares)

        