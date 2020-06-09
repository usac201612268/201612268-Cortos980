
#Secuencia de Collatz: 
#Carne: 201612268  = 268 Numero 


CARNE = 268  # ultimos 3 digitos del carne
listaC = [] # lista donde se escribiran los resultados

def secuencia(valor1): #funcion que determina si es par o impar
    salidaT = 0 # definicion de la variable
    if valor1%2==0:  # condicional si es par hacer lo de la condicion N/2
        salidaT = int(valor1/2)
    else:
        salidaT = int(valor1*3 +1) # sino es PAR entonces es IMPAR
    return salidaT # valor de retorno de la funcion

listaTotal  = [] # definir una matriz total
j = 2   # definimos un valor para 
bandera = True  # bandera para terminar un ciclo
for i in range(0,CARNE):    # las veces que se escribira en la lista
    listaC = [] # vaciando la lista
    bandera = True  #reiniciando la bandera para que entre al ciclo de nuevo
    temporal = j    # valor para ingresar a la lista al principio una vez esta termine, este es el numero por el cual va la lista, su primer valor
    k = j   # numero que ingresara para ser evaluado en la funcion de PAR / Impar
    while bandera:  #ciclo para la escritura de la lista
        listaC.append(secuencia(k)) #añadiendo valores a la lista C
        if listaC[-1]==1: # si el ultimo valor es uno dejar de seguir buscando un valor
            j += 1  #aumento a numero a evaluar para el siguiente
            listaC.insert(0,temporal) # insertamos el valor evaluado al principo ya sea 2, 3, 4, 5
            listaTotal.append(listaC) # llenar una lista de "listasC"
            bandera = False # bandera para salir el ciclo
            print(listaC)
        else:
            k = listaC[-1] # tomar el ultimo valor de la lista para evaluarlo nuevamente en la funcion de PAR IMPAR

"""
def Escribir(fileName = "collatz.txt"): #funcion para escribir en el .txt
    archivo = open(fileName='w')
    archivo.write('Escribiendo o sobreescribiendo archivo')
    print("Un momento por favor en lo que se escribe el archivo")
    for i in range(2,len(listaTotal)):
        time.sleep(1)
    archivo.close()
    print("Escritura finalizada") """