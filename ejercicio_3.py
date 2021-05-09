def extraerNumero(cadena):
    cadena_numero = ""
    indice = 0
    for i in cadena:
        if(i == " "):
            cadena = cadena[indice:]
            return cadena_numero
        cadena_numero = cadena_numero + i
        indice=+1


def extraerOperacion(cadena):
    for i in cadena:
        if(i == "+"):
            return "SUMA"
        if(i == "-"):
            return "RESTA"
        if(i == "*"):
            return "MULTIPLICACION"
        if(i == "/"):
            return "DIVISION"
    return "NO SE PUEDE HACER NINGUNA OPERACION"

def realizar_operacion(numeroA, operacion, numeroB):
    if(numeroB == 0):
        return "No se puede dividir por 0"
    if(operacion == "SUMA"):
        return numeroA + numeroB
    if (operacion == "RESTA"):
        return numeroA - numeroB
    if (operacion == "MULTIPLICACION"):
        return numeroA * numeroB
    if (operacion == "DIVISION"):
        return numeroA / numeroB

def operacion_aritmetica(cadena):
    indicePrimerEspacio = cadena.find(" ")
    cadenaPrimerNumero = cadena[:indicePrimerEspacio]
    numeroA = int(cadenaPrimerNumero)

    cadenaPosteriorPrimerNumero = cadena[(indicePrimerEspacio + 1) :]
    indiceSegundoEspacio = cadenaPosteriorPrimerNumero.find(" ")
    cadenaSegundoNumero = cadenaPosteriorPrimerNumero[(indiceSegundoEspacio + 1):]
    numeroB = int(cadenaSegundoNumero)

    cadenaOperacion = cadenaPosteriorPrimerNumero[0]
    operacion = extraerOperacion(cadenaOperacion)

    return realizar_operacion(numeroA, operacion, numeroB)