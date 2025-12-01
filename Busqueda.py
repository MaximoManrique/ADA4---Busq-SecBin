
def linear_search(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1     
    return -1


def busqueda_hash(lista, objetivo):
   
    tabla_hash = {}
    
    
    for i, numero in enumerate(lista):
        tabla_hash[numero] = i
        
   
    if objetivo in tabla_hash:
        return tabla_hash[objetivo]
    else:
        return -1