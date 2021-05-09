def procesar(listaCaracteres, longitudCadenas, contador, listaResultante):
    if(contador >= len(listaCaracteres)):
        return listaResultante
    caracter = listaCaracteres[contador]
    for i in listaCaracteres:
        cadenaFormada = caracter + i
        listaResultante.append(cadenaFormada)
    return procesar(listaCaracteres, longitudCadenas, contador + 1, listaResultante)

def combinaciones(listaCaracteres, longitudCadenas):
    return procesar(listaCaracteres, longitudCadenas, 0, [])