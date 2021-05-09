def formarCadenaConCaracter(caracterInicial, numeroRepeticiones):
    if(numeroRepeticiones == 0):
        return ""
    return caracterInicial + formarCadenaConCaracter(caracterInicial, numeroRepeticiones - 1)

def repeticiones(cadena, numeroRepeticiones):
    caracterInicial = cadena[0]
    cadena = cadena[1:]
    contadorRepeticiones = 0
    cadenaGenerada = ""
    seFormoCadenaTemporal = False
    index = 0
    for caracter in cadena:
        if(seFormoCadenaTemporal and caracter != caracterInicial):
            seFormoCadenaTemporal = False

        if(caracter == caracterInicial):
            contadorRepeticiones+=1

        if(contadorRepeticiones == numeroRepeticiones and caracter == caracterInicial and  not seFormoCadenaTemporal):
            cadenaGenerada = cadenaGenerada + formarCadenaConCaracter(caracterInicial, numeroRepeticiones)
            seFormoCadenaTemporal = True

        if(caracter != caracterInicial):
            caracterInicial = caracter
            contadorRepeticiones = 1
            if (contadorRepeticiones == numeroRepeticiones and not seFormoCadenaTemporal):
                cadenaGenerada = cadenaGenerada + formarCadenaConCaracter(caracterInicial, numeroRepeticiones)
                seFormoCadenaTemporal = True
            if ((len(cadena) - index) <= numeroRepeticiones and not seFormoCadenaTemporal):
                cadenaGenerada = cadenaGenerada + formarCadenaConCaracter(caracterInicial, (len(cadena) - index))

        index += 1

    return cadenaGenerada