# PROYECTO LÓGICA: Katas de Python

'''
1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
'''
def frecuencia_letra(cadena):
    ''' Esta función recibe una cadena de texto y devuelve un diccionario con la frecuencia de cada letra en la cadena, ignorando los espacios. 
        Args:
            cadena (str): La cadena de texto a analizar.
        Returns:
            dict_letras (dict): Un diccionario donde las claves son las letras y los valores son sus frecuencias en la cadena.
    '''
    # Creamos un diccionario vacío
    dict_letras = {}
    # Con un bucle for iteramos por cada una de las letras del texto (eliminando espacios)
    for l in cadena.upper().replace(' ',''):
        # Contamos cada uno de los valores de la cadena
        conteo = cadena.upper().count(l)
        # Y vamos añadiendo en el diccionario cada letra con su conteo
        dict_letras[l] = conteo
    return dict_letras


'''
2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función  map()
'''
lista_numeros = [2, 3, 6, 7, 3, 6, 8]

resultado_map = list(map(lambda x: x*2,lista_numeros))


'''
3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
'''
def encontrar_palabra(lista,palabra):
    ''' Esta función recibe una lista de palabras y una palabra objetivo, y devuelve una lista con todas las palabras que contienen la palabra objetivo.
        Args:
            lista (list): Lista de palabras a analizar.
            palabra (str): Palabra objetivo a buscar en la lista.
        Returns:
            lista_final (list): Lista de palabras que contienen la palabra objetivo.
    '''
    lista_final = []
    for e in lista:
        if e == palabra:
            lista_final.append(e)
        else:
            continue
    return lista_final


'''
4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función  map()
'''
def resta_listas(lista1, lista2):
    ''' Esta función recibe dos listas de números y devuelve una nueva lista con la diferencia entre los valores correspondientes de las dos listas.
        Args:
            lista1 (list): Primera lista de números.
            lista2 (list): Segunda lista de números.
        Returns:
            list: Lista con la diferencia entre los valores correspondientes de las dos listas.
    '''
    resta_map = list(map(lambda x,y:x-y, lista1, lista2 ))
    return resta_map


'''
5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
 La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
 Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
'''
def evaluar_notas(notas, aprobado):
    '''Funcion que calcula la media de una lista de notas y devuelve el resultado y la valoración de aprobado o no en funcion del valor de aprobado elegido por el usuario

    Args:
        notas (list): Listado de notas (valor númérico)
        aprobado (number): Numero entero o decimal

    Returns:
        Devuelve una tupla con el valor de la media y un stirng informando de si ese valor corresponde con un aprobado o un suspenso
    '''
    media_notas= sum(notas) / len(notas)
    resultado = []
    resultado.append(media_notas)

    if media_notas >= aprobado:
        resultado.append("Aprobado")    
    else:
        resultado.append("Suspenso")
    
    return tuple(resultado)  

'''
6. Escribe una función que calcule el factorial de un número de manera recursiva.
- El factorial de un número  es el resultado de multiplicar ese número por todos los números enteros positivos menores que él hasta llegar a 1.
'''
def calcular_factorial(numero):
    ''' Esta función calcula el factorial de un número de manera recursiva.
        Args:
            numero (int): El número del cual se desea calcular el factorial.
        Returns:
            int: El factorial del número.
    '''
    if numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)
    
'''
    7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
'''
def tupla_to_string(tupla):
    """Funcion que convierte una tupla en un string

    Args:
        tupla (tuple): Tupla a convertir

    Returns:
        str: Devuelve la tupla convertida en string
    """
    return  list(map(lambda t: " ".join(map(str, t)), tupla))

'''
8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero,
maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
'''
input_1 = input("Introduce un número: ")
input_2 = input("Introduce otro número: ")

try:
    resultado = int(input_1) / int(input_2)
    print(f"El resultado de la división es {resultado}")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Has introducido un valor no numérico")

'''
9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
'''
def mascotas_permitidas(lista_mascotas):
    """Funcion que filtra una lista de mascotas y devuelve una lista con las mascotas permitidas

    Args:
        lista_mascotas (list): Lista de mascotas a evaluar

    Returns:
        Lista de mascotas permitidas
    """
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

'''
10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
'''
def calcular_promedio(lista_numeros):
    """Funcion que calcula el promedio de una lista de números
    Args:
        lista_numeros (list): Lista de números a evaluar
    Returns :
        Devuelve el promedio de la lista (float) redondeado a 2 decimales
    """
    try:
        promedio = sum(lista_numeros) / len(lista_numeros)
        return round(promedio,2)
    except ZeroDivisionError:
        return "La lista está vacía"
    
'''
11. Escribe un programa que pida al usuario que introduzca su edad. 
Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones  adecuadamente.
'''
input_edad = input("Introduce tu edad: ")

try:
    edad = int(input_edad)
    if edad < 0:
        print ("La edad no puede ser negativa")
    elif edad > 120:
        print ("La edad no puede ser mayor de 120")
    else:
        print (f"Tienes {edad} años")

except ValueError:
    print("Has introducido un valor no numérico")

'''
12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función  map()
'''
def longitudes_palabras(frase):
    """Funcion que calcula la longitud de cada palabra en una frase y la devuelve como una lista

    Args:
        frase (str): Frase de entrada

    Returns:
        list: Una lista con la longitud de cada palabra
    """
    return list(map(len, frase.split()))

