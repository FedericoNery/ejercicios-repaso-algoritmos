def esta_dentro_de_lista_la_palabra(lista, palabra):
    for x in lista:
        if x == palabra:
            return True
    return False

def esta_dentro_de_lista_la_palabra_en_singular(lista, palabra):
    return esta_dentro_de_lista_la_palabra(lista, palabra)

def esta_dentro_de_lista_la_palabra_en_plural(lista, palabra):
    return esta_dentro_de_lista_la_palabra(lista, palabra + "s")

def pluralize(lista):
    setDePalabras = set()
    for palabra in lista:
        dentroDeLaListaEnSingular = esta_dentro_de_lista_la_palabra_en_singular(setDePalabras, palabra)
        dentroDeLaListaEnPlural = esta_dentro_de_lista_la_palabra_en_plural(setDePalabras, palabra)

        if (not dentroDeLaListaEnSingular) and (not dentroDeLaListaEnPlural):
            setDePalabras.add(palabra)
        elif dentroDeLaListaEnSingular and not dentroDeLaListaEnPlural:
            palabraPluralizada = palabra + "s"
            setDePalabras.discard(palabra)
            setDePalabras.add(palabraPluralizada)

    return setDePalabras