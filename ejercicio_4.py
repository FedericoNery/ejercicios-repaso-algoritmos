def procesarNumero(numero):
    NUMERO_SIETE = 7
    NUMERO_SIETE_DECIMAL = 0.7

    numeroAProcesar = numero
    while numeroAProcesar > NUMERO_SIETE:
        cociente = numeroAProcesar // 10
        resto = numeroAProcesar % 10
        if resto == NUMERO_SIETE:
            return True
        numeroAProcesar = numeroAProcesar // 10

    return numeroAProcesar == NUMERO_SIETE

def sevenBoom(numeros):
    NUMERO_SIETE = 7
    BOOM = "Boom!"
    NO_SE_ENCUENTRA_EL_NUMERO = "No se encuentra el número 7"

    for numero in numeros:
        if numero == NUMERO_SIETE:
            return BOOM
        if numero > NUMERO_SIETE:
            poseeElNumeroSiete = procesarNumero(numero)
            if poseeElNumeroSiete:
                return BOOM

    return NO_SE_ENCUENTRA_EL_NUMERO