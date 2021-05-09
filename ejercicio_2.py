def same_length(secuencia):

    bitDeInicial = secuencia[0]
    secuenciaSinInicial = secuencia[1:]
    contadorDeCeros = bitDeInicial == "0" if 1 else 0
    contadorDeUnos = bitDeInicial == "1" if 1 else 0
    esperarFinalizacionDeSecuencia = False

    for bit in secuenciaSinInicial:
        if bit == "0":
            contadorDeCeros += 1
        if bit == "1":
            contadorDeUnos += 1

        if bitDeInicial != bit:
            esperarFinalizacionDeSecuencia = True

        if bitDeInicial == bit and esperarFinalizacionDeSecuencia:
            contadorTemporalDeCeros = contadorDeCeros-1 if bit == "0" else contadorDeCeros
            contadorTemporalDeUnos = contadorDeUnos-1 if bit == "1" else contadorDeUnos

            if contadorTemporalDeCeros != contadorTemporalDeUnos:
                return False

            esperarFinalizacionDeSecuencia = False

            if bit == "0":
                contadorDeCeros = 1
                contadorDeUnos = 0

            if bit == "1":
                contadorDeUnos = 1
                contadorDeCeros = 0

    return contadorDeCeros == contadorDeUnos