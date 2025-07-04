"""PROYECTO LÓGICA: Katas de Python

Ejercicio 1:
Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
"""
def frecuencia_letra(cadena):
    """Calcula la frecuencia de cada letra en una cadena de texto.
    
    Args:
        cadena (str): Cadena de texto a analizar.
        
    Returns:
        dict: Un diccionario con las letras como claves y sus frecuencias como valores.
    """
    # Creamos un diccionario vacío
    dict_letras = {}
    # Con un bucle for iteramos por cada una de las letras del texto (eliminando espacios)
    for l in cadena.upper().replace(' ',''):
        # Contamos cada uno de los valores de la cadena
        conteo = cadena.upper().count(l)
        # Y vamos añadiendo en el diccionario cada letra con su conteo
        dict_letras[l] = conteo
    return dict_letras


"""Ejercicio 2:
Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
"""
lista_numeros = [2, 3, 6, 7, 3, 6, 8]
resultado_map = list(map(lambda x: x*2,lista_numeros))
resultado_map


"""Ejercicio 3:
Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
"""
lista_palabras1 = ["pimiento", "cebolla", "calabacin", "tomate", "uva"]
palabra1 = "pimiento"

def encontrar_palabra(lista, palabra_objetivo):
    """Busca una palabra exacta en una lista de palabras.
    
    Args:
        lista (list): Lista de palabras donde buscar.
        palabr_onjetivo (str): Palabra a buscar.
        
    Returns:
        list: Lista con las coincidencias exactas encontradas.
    """
    return[palabra for palabra in lista if palabra_objetivo in palabra]

encontrar_palabra(lista_palabras1,palabra1)


"""Ejercicio 4:
Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
"""
lista1= [2, 3, 5, 6, 1, 4]
lista2 = [1, 1, 5, 4, 3, 1]

def resta_listas(lista1, lista2):
    """Calcula la diferencia entre elementos correspondientes de dos listas.
    
    Args:
        lista1 (list): Primera lista de números.
        lista2 (list): Segunda lista de números.
        
    Returns:
        list: Lista con las diferencias entre elementos correspondientes.
    """
    resta_map = list(map(lambda x,y:x-y, lista1, lista2 ))
    return resta_map

resta_listas(lista1, lista2)


"""Ejercicio 5:
Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
"""
def evaluar_notas(notas, aprobado=5):
    """Calcula la media de una lista de notas y determina si está aprobado.
    
    Args:
        notas (list): Lista de notas numéricas.
        aprobado (float): Nota mínima para aprobar. Por defecto: 5.
        
    Returns:
        tuple: Tupla con la media y el estado (aprobado/suspenso).
    """
    media_notas= sum(notas) / len(notas) if notas else 0
    estado = "Aprobado" if media_notas >= aprobado else "Suspenso"
    return media_notas, estado

lista_notas = [5, 7, 8, 9, 10]
valor_aprobado = 5
evaluar_notas(lista_notas,valor_aprobado)


"""Ejercicio 6:
Escribe una función que calcule el factorial de un número de manera recursiva.
El factorial de un número es el resultado de multiplicar ese número por todos los números enteros positivos menores que él hasta llegar a 1.
"""
def calcular_factorial(numero):
    """Calcula el factorial de un número de forma recursiva.
    
    Args:
        numero (int): Número para calcular su factorial.
        
    Returns:
        int: El factorial del número.
    """
    if numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

calcular_factorial(7)


"""Ejercicio 7:
Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
"""
def tupla_to_string(tupla):
    """Convierte una lista de tuplas en una lista de strings.
    
    Args:
        tupla (list): Lista de tuplas a convertir.
        
    Returns:
        list: Lista de strings resultante.
    """
    return  list(map(lambda t: " ".join(map(str, t)), tupla))


"""Ejercicio 8:
Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
"""
input_1 = input("Introduce un número: ")
input_2 = input("Introduce otro número: ")

try:
    resultado = int(input_1) / int(input_2)
    print(f"El resultado de la división es {resultado}")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Has introducido un valor no numérico")


"""Ejercicio 9:
Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()
"""
def mascotas_permitidas(lista_mascotas):
    """Filtra una lista de mascotas excluyendo las prohibidas.
    
    Args:
        lista_mascotas (list): Lista de mascotas a filtrar.
        
    Returns:
        list: Lista de mascotas permitidas.
    """
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))


"""Ejercicio 10:
Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
"""
class ListaVaciaError(Exception):
    """Excepción personalizada que se lanza cuando se intenta calcular el promedio de una lista vacía.
    """
    pass

def calcular_promedio(lista_numeros):
    """Calcula el promedio de una lista de números.
    
    Args:
        lista_numeros (list): Lista de números.
        
    Returns:
        float: Promedio de los números o mensaje de error si la lista está vacía.
    """
    if not lista_numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    else:
        return round(sum(lista_numeros) / len(lista_numeros),2)

#Uso
try:
    resultado = calcular_promedio([])
    print(f"El promedio es {resultado}")
except ListaVaciaError as e:
    print(f"Error: {e}")


"""Ejercicio 11:
Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
"""
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


"""Ejercicio 12:
Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
"""
def longitudes_palabras(frase):
    """Calcula la longitud de cada palabra en una frase.
    
    Args:
        frase (str): Frase a analizar.
        
    Returns:
        list: Lista con las longitudes de cada palabra.
    """
    return list(map(len, frase.split()))

frase_test = "Esta es una frase de prueba"
longitudes_palabras = longitudes_palabras(frase_test)
longitudes_palabras


"""Ejercicio 13:
Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()
"""
def mayus_minus_tuplas(conjunto):
    """Genera tuplas con versiones mayúscula y minúscula de cada letra.
    
    Args:
        conjunto (str): Conjunto de caracteres.
        
    Returns:
        list: Lista de tuplas (mayúscula, minúscula).
    """
    return list(map(lambda l: (l.upper(), l.lower()), set(conjunto.lower().replace(" ", ""))))

resultado_tuplas = mayus_minus_tuplas(frase_test)
resultado_tuplas


"""Ejercicio 14:
Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
"""
def palabras_con_letra(lista_palabras, letra):
    """Filtra palabras que comienzan con una letra específica.
    
    Args:
        lista_palabras (list): Lista de palabras.
        letra (str): Letra inicial a buscar.
        
    Returns:
        list: Lista de palabras que comienzan con la letra especificada.
    """
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))

resultado_palabras = palabras_con_letra(["Patata", "pimiento", "Amapola", "pijo", "Incendio"], "p")


"""Ejercicio 15:
Crea una función lambda que sume 3 a cada número de una lista dada.
"""
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))


"""Ejercicio 16:
Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
"""
cadena = "Vamos a por ello, no hay que rendirse aunque sea dificil. Sin miedo."
len(cadena)

def longitudes_palabras(cadena, longitud):
    """Genera una lista con las palabras más largas que una longitud dada.

    Args:
        cadena (string): Cadena de palabras.
        longitud (int): Numero que representa la longitud por la que se filtraran las palabras de la cadena (no incluido).

    Returns:
        Lista de palabras con una longitud mayor que la dada.
    """
    return list(filter(lambda x: len(x) > longitud, cadena.split()))

#Uso
resultado_cadena = longitudes_palabras(cadena,7)
resultado_cadena


"""Ejercicio 17:
Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos [572]. Usa la función reduce()
"""
from functools import reduce

def lista_numero(lista_digitos):
    """Devuelve un número formado a partir de una lista de numeros.

    Args:
        lista_digitos (lista): Lista de números.

    Returns:
        Numero compuesto por los números de la lista de digitos.
    """
    return reduce(lambda acc, d: acc * 10 + d, lista_digitos, 0)

#Uso
resultado_numero = lista_numero([4, 3, 6, 5, 7, 2])
print(resultado_numero)


"""Ejercicio 18:
Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
"""
# Creamos la lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "Marta", "edad": 21, "calificacion": 92},
    {"nombre": "Pedro", "edad": 23, "calificacion": 85},
    {"nombre": "Sofía", "edad": 20, "calificacion": 90}
]

# Usamos filter para extraer estudiantes con calificación >= 90
estudiantes_destacados = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))
estudiantes_destacados


"""Ejercicio 19:
Crea una función lambda que filtre los números impares de una lista dada.
"""
def numeros_impares(lista_numeros):
    """Filtra los números impares de una lista.
    
    Args:
        lista_numeros (list): Lista de números.
        
    Returns:
        list: Lista de números impares.
    """
    return list(filter(lambda x: x % 2 != 0, lista_numeros))

resultado_impares = numeros_impares([1, 2, 3, 4, 5, 6, 7, 8, 9])
resultado_impares


"""Ejercicio 20:
Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter().
"""
list(filter(lambda x: type(x) == int , ["pie", 2.5, 3, "hola", 4, 5.6, 6, "adios"]))


"""Ejercicio 21:
Crea una función que calcule el cubo de un número dado mediante una función lambda
"""

calcular_cubo = lambda x: x ** 3

#Uso
calcular_cubo(3)


"""Ejercicio 22:
Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().
"""
reduce(lambda x, y: x*y, [1, 2, 3, 4, 5])


"""Ejercicio 23:
Concatena una lista de palabras. Usa la función reduce().
"""
reduce(lambda x,y: x + " " + y, ["Hola", "que", "tal"])


"""Ejercicio 24:
Calcula la diferencia total en los valores de una lista. Usa la función reduce().
"""
reduce(lambda x,y: x-y, [10, 5, 2, 1])


"""Ejercicio 25:
Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""
def longitud_cadena(cadena):
    """Calcula la longitud de una cadena sin espacios.
    
    Args:
        cadena (str): Cadena de texto.
        
    Returns:
        int: Longitud de la cadena sin espacios.
    """
    return len(cadena.replace(" ", "")) # Eliminamos los espacios en blanco

resultado_lcadena = longitud_cadena("Hola, ¿cómo estás?")
resultado_lcadena


"""Ejercicio 26:
Crea una función lambda que calcule el resto de la división entre dos números dados.
"""
resto = lambda x, y: x % y
resto(10, 3)


"""Ejercicio 27:
Crea una función que calcule el promedio de una lista de números.
"""
def promedio_lista(lista_numeros):
    """Calcula el promedio de una lista de números.
    
    Args:
        lista_numeros (list): Lista de números.
        
    Returns:
        float: Promedio de los números o 0 si la lista está vacía.
    """
    return sum(lista_numeros) / len(lista_numeros) if lista_numeros else 0

resultado_promedio = promedio_lista([1, 2, 3, 4, 5])
resultado_promedio


"""Ejercicio 28:
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""
def primer_duplicado(lista):
    """Encuentra el primer elemento duplicado en una lista.
    
    Args:
        lista (list): Lista donde buscar duplicados.
        
    Returns:
        any: El primer elemento duplicado encontrado o None si no hay duplicados.
    """
    valores = []
    for i in lista:
        if i not in valores:
            valores.append(i)   
        else:
            return i

resultado_duplicado = primer_duplicado([1, 2, 3, 1,4, 2, 5, 3, 6])
resultado_duplicado


"""Ejercicio 29:
Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
"""
def censurar_cadena(variable):
    """Enmascara una cadena manteniendo visibles los últimos 4 caracteres.
    
    Args:
        variable: Variable a enmascarar.
        
    Returns:
        str: Cadena enmascarada con '#' excepto los últimos 4 caracteres.
    """
    s = str(variable)
    if len(s) <= 4:
        return s
    return "#" * (len(s) - 4) + s[-4:]

cadena_censurada = censurar_cadena("Contraseña")
cadena_censurada


"""Ejercicio 30:
Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
"""
def detectar_anagrama(palabra1, palabra2):
    """Determina si dos palabras son anagramas.
    
    Args:
        palabra1 (str): Primera palabra.
        palabra2 (str): Segunda palabra.
        
    Returns:
        bool: True si son anagramas, False en caso contrario.
    """
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

test_anagrama = detectar_anagrama("amor", "Roma")
test_anagrama


"""Ejercicio 31:
Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
"""
def encontrar_nombre(lista_nombres, nombre):
    """Busca un nombre en una lista sin distinguir mayúsculas y minúsculas.
    
    Args:
        lista_nombres (list): Lista de nombres.
        nombre (str): Nombre a buscar.
        
    Returns:
        str: Mensaje indicando si el nombre está o no en la lista.
    """
    nombres_normalizados = [n.lower() for n in lista_nombres]
    if nombre.lower() in nombres_normalizados:
        return f"El nombre {nombre} se encuentra en la lista"
    else:
        raise ValueError(f"El nombre {nombre} no se encuentra en la lista")

lista_nombres = ["Ana", "Luis", "Marta", "Pedro", "Sofía"]
nombre_a_buscar = "Marta"
resultado = encontrar_nombre(lista_nombres, nombre_a_buscar)
resultado


"""Ejercicio 32:
Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
"""
def buscar_puesto(nombre_completo, lista_empleados):
    """Busca un empleado en una lista y devuelve su posición.
    
    Args:
        nombre_completo (str): Nombre completo del empleado.
        lista_empleados (list): Lista de empleados.
        
    Returns:
        str: Mensaje con la posición del empleado o indicando que no trabaja aquí.
    """
    try:
        posicion = lista_empleados.index(nombre_completo)
        return f"{nombre_completo} trabaja aquí y ocupa la posición {posicion}"
    except ValueError:
        return f"{nombre_completo} no trabaja aquí"

lista_empleados = ["Ana Peña", "Luis García", "Marta López", "Pedro Sánchez", "Sofía Martínez"]
empleado_a_buscar = "Marta López"
puesto_empleado = buscar_puesto(empleado_a_buscar, lista_empleados)
puesto_empleado


"""Ejercicio 33:
Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))
resultado_suma = sumar_listas([1, 2, 3], [4, 5, 6])
print(resultado_suma)


"""Ejercicio 34:
Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos métodos para manipular la estructura del árbol.
"""
class Arbol:
    """Clase que representa un árbol con un tronco y una lista de ramas."""

    def __init__(self):
        """Inicializa un árbol con tronco de longitud 1 y sin ramas."""
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.tronco += 1

    def nueva_rama(self):
        """Añade una nueva rama de longitud 1 al árbol."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas existentes."""
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina la rama en la posición especificada.

        Args:
            posicion (int): Índice de la rama a eliminar (comenzando desde 0).

        Raises:
            IndexError: Si la posición no es válida.
        """
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            raise IndexError("Posición de rama inválida")

    def info_arbol(self):
        """Devuelve información sobre el estado actual del árbol.

        Returns:
            dict: Diccionario con la longitud del tronco, el número de ramas
            y las longitudes de cada una.
        """
        return {
            "longitud_tronco": self.tronco,
            "num_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas.copy()
        }



"""Ejercicio 35:
Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
"""
# 1. Crear un árbol
arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad
arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2
arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
info = arbol.info_arbol()
print(info)


"""Ejercicio 36:
Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
"""
class UsuarioBanco:
    """Clase que representa un usuario de banco.
    
    Attributes:
        nombre (str): Nombre del usuario.
        saldo (float): Saldo actual.
        cuenta_corriente (bool): Indica si tiene cuenta corriente.
    """
    
    def __init__(self, nombre, saldo, cuenta_corriente):
        """Inicializa un usuario de banco.
        
        Args:
            nombre (str): Nombre del usuario.
            saldo (float): Saldo inicial.
            cuenta_corriente (bool): Indica si tiene cuenta corriente.
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    
    def retirar_dinero(self, cantidad):
        """Retira dinero del saldo del usuario.
        
        Args:
            cantidad (float): Cantidad a retirar.
        """
        if cantidad < 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
        return self.saldo
    
    def transferir_dinero(self, otro_usuario, cantidad):
        """Transfiere dinero desde otro usuario.
        
        Args:
            otro_usuario (UsuarioBanco): Usuario desde el que transferir.
            cantidad (float): Cantidad a transferir.
        """
        self.retirar_dinero(cantidad)
        otro_usuario.agregar_dinero(cantidad)
    
    def agregar_dinero(self, cantidad):
        """Añade dinero al saldo del usuario.
        
        Args:
            cantidad (float): Cantidad a añadir.
        """
        if cantidad < 0:
            raise ValueError("La cantidad debe ser positiva")
        self.saldo += cantidad
        return self.saldo


"""Ejercicio 37:
Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.
"""
def contar_palabras(texto):
    """Cuenta la frecuencia de cada palabra en un texto.
    
    Args:
        texto (str): Texto a analizar.
        
    Returns:
        dict: Diccionario con palabras y sus frecuencias.
    """
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        palabra_limpia = palabra.strip('.,;:"!?¡¿()').lower()
        contador[palabra_limpia] = contador.get(palabra_limpia, 0) + 1
    return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Reemplaza una palabra por otra en un texto.
    
    Args:
        texto (str): Texto original.
        palabra_original (str): Palabra a reemplazar.
        palabra_nueva (str): Nueva palabra.
        
    Returns:
        str: Texto con las palabras reemplazadas.
    """
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    """Elimina una palabra específica de un texto.
    
    Args:
        texto (str): Texto original.
        palabra_a_eliminar (str): Palabra a eliminar.
        
    Returns:
        str: Texto sin la palabra especificada.
    """
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    """Procesa un texto según la opción especificada.
    
    Args:
        texto (str): Texto a procesar.
        opcion (str): Opción de procesamiento ('contar', 'reemplazar', 'eliminar').
        *args: Argumentos adicionales según la opción.
        
    Returns:
        dict/str: Resultado del procesamiento según la opción.
        
    Raises:
        ValueError: Si la opción no es válida o faltan argumentos.
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se requieren dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se requiere un argumento: palabra_a_eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")

# Texto de ejemplo
texto_original = "El gato se subió al tejado. El perro ladró al gato. ¡Qué gato tan valiente!"

# Contar palabras
conteo = procesar_texto(texto_original, "contar")
print("Conteo de palabras:")
print(conteo)

# Reemplazar 'gato' por 'conejo'
texto_reemplazado = procesar_texto(texto_original, "reemplazar", "gato", "conejo")
print("\nTexto con 'gato' reemplazado por 'conejo':")
print(texto_reemplazado)

# Eliminar la palabra 'al'
texto_eliminado = procesar_texto(texto_original, "eliminar", "al")
print("\nTexto con la palabra 'al' eliminada:")
print(texto_eliminado)


"""Ejercicio 38:
Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
"""
def clasificar_momento_del_dia(hora):
    """Clasifica el momento del día según la hora.
    
    Args:
        hora (int): Hora del día (0-23).
        
    Returns:
        str: Clasificación del momento del día.
    """
    if 0 <= hora <= 5 or 21 <= hora <= 23:
        return "Es de noche."
    elif 6 <= hora <= 12:
        return "Es de día."
    elif 13 <= hora <= 20:
        return "Es de tarde."
    else:
        return "Hora inválida. Debe estar entre 0 y 23."

try:
    entrada = input("Introduce la hora (0 a 23): ")
    hora = int(entrada)
    resultado = clasificar_momento_del_dia(hora)
    print(resultado)
except ValueError:
    print("Por favor, introduce un número entero válido.")


"""Ejercicio 39:
Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
"""
def calificacion_en_texto(nota):
    """Convierte una calificación numérica a texto.
    
    Args:
        nota (int): Calificación numérica (0-100).
        
    Returns:
        str: Calificación en texto.
    """
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Nota inválida. Debe estar entre 0 y 100."

try:
    entrada = input("Introduce la calificación (0 a 100): ")
    nota = int(entrada)
    resultado = calificacion_en_texto(nota)
    print("Resultado:", resultado)
except ValueError:
    print("Por favor, introduce un número entero válido.")


"""Ejercicio 40:
Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).
"""
def calcular_area(figura, datos):
    """Calcula el área de diferentes figuras geométricas.
    
    Args:
        figura (str): Tipo de figura ('rectangulo', 'triangulo', 'circulo').
        datos (tuple): Datos necesarios para el cálculo.
        
    Returns:
        float/str: Área calculada o mensaje de error.
    """
    figura = figura.lower()

    if figura == "rectangulo":
        if len(datos) != 2:
            return "Se necesitan base y altura para un rectángulo."
        base, altura = datos
        return base * altura

    elif figura == "triangulo":
        if len(datos) != 2:
            return "Se necesitan base y altura para un triángulo."
        base, altura = datos
        return (base * altura) / 2

    elif figura == "circulo":
        if len(datos) != 1:
            return "Se necesita el radio para un círculo."
        (radio,) = datos
        pi = 3.14
        return pi * radio ** 2

    else:
        return "Figura no reconocida. Usa 'rectangulo', 'triangulo' o 'circulo'."

print(calcular_area("rectangulo", (4, 5)))   # 20
print(calcular_area("triangulo", (3, 6)))    # 9.0
print(calcular_area("circulo", (2,)))        # 12.56


"""Ejercicio 41:
En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
- Solicita al usuario que ingrese el precio original de un artículo.
- Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
- Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
- Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
- Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
"""
try:
    # Paso 1: Solicitar el precio original
    precio = float(input("Introduce el precio original del artículo (€): "))

    if precio < 0:
        print("El precio no puede ser negativo.")
    else:
        # Paso 2: Preguntar por cupón
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        # Paso 3: Si tiene cupón, solicitar valor y aplicar
        if tiene_cupon == "sí" or tiene_cupon == "si":
            try:
                descuento = float(input("Introduce el valor del cupón de descuento (€): "))
                if descuento > 0:
                    precio_final = max(precio - descuento, 0)  # Evita que el precio final sea negativo
                    print(f"Descuento aplicado de {descuento:.2f}€. Precio final: {precio_final:.2f}€")
                else:
                    print("El valor del cupón debe ser mayor que 0. No se ha aplicado descuento.")
                    print(f"Precio final: {precio:.2f}€")
            except ValueError:
                print("Valor de descuento no válido. No se ha aplicado descuento.")
                print(f"Precio final: {precio:.2f}€")
        elif tiene_cupon == "no":
            print(f"Precio final sin descuento: {precio:.2f}€")
        else:
            print("Respuesta no válida. Se asume que no tienes cupón.")
            print(f"Precio final: {precio:.2f}€")

except ValueError:
    print("Por favor, introduce un número válido para el precio.") 