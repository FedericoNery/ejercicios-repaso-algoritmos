# ejercicios-repaso-algoritmos
1. Dada una lista de palabras de forma singular, retornar un SET de esas palabras en forma plural si aparecen mas de una vez en la lista.
   
   pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" } 
   
   pluralize(["table", "table", "table"]) ➞ { "tables" } 
   
   pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }


2. Escribir una función que retorne True si cada secuencia consecutiva de unos es seguida por una secuencia consecutiva de ceros de la misma longitud

    same_length("110011100010") ➞ True

    same_length("101010110") ➞ False

    same_length("111100001100") ➞ True

    same_length("111") ➞ False


3. Crear una función que permita realizar una operación aritmética que incluya adición, sustracción, multiplicación y división teniendo como parámetro de la función los siguientes ejemplos: “12 + 24” , “23 - 21”, “12 // 12”, “12 * 21”
En el caso de la división por cero, retornar -1 o algún mensaje que diga que no se puede realizar la operación.

    arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

    arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

    arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

    arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
    
    ACLARACION: no necesariamente al dividir por cero tiene que devolver -1, esto es a criterio del programador 
   

4. Crear una función que tome un array de numeros y retorne la palabra “Boom!” si el dígito 7 aparece en el array. Sino, que retorne “No se encuentra el número 7 en el array” . 
 
    sevenBoom([1, 2, 3, 4, 5, 6, 7]) ➞ "Boom!" // El array contiene el número 7
   
    sevenBoom([8, 6, 33, 100]) ➞ “No se encuentra el número 7 en el array” // ninguno de los elementos contiene el número 7
   
    sevenBoom([2, 55, 60, 97, 86]) ➞ "Boom!" // 97 contiene el número 7.


5. Escribí una función que reciba dos parámetros: un string S y un integer R. La función debe devolver un string donde los caracteres consecutivos de S no se repitan más que R veces. Tiene que devolver un string con el texto limpio y la cantidad de caracteres repetidos correcta.
 
    "AAA", 2 => "AA"
   
    "AAAAAFFFFOOOA", 2 => "AAFFOOA"

    "111223333344", 1 => "1234"
   
    "AABB", 1 => "AB"


6. Escribir una función recursiva que reciba un conjunto de caracteres únicos, y un número 𝑘, e imprima todas las posibles cadenas de longitud 𝑘 formadas con los caracteres dados (permitiendo caracteres repetidos). 
   
    combinaciones(['a', 'b', 'c'], 2) -> ["aa", "ab", "ac", "ba", "bb", "bc", "ca" "cb" "cc"]

