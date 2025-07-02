
#region GUÍA DEL CURSO DE PYTHON: FUNDAMENTOS Y PROYECTOS

#-----------------------------------------------------------------------------------------------------------------------
# GUÍA DEL CURSO DE PYTHON: FUNDAMENTOS Y PROYECTOS
#
# Basado en el libro "Python Crash Course, 3rd Edition" de Eric Matthes.
# Esta guía es una compilación de los conceptos, ejemplos de código y ejercicios de los primeros capítulos
# para servir como un recurso de estudio y práctica en un solo archivo ejecutable.
#
# Cada capítulo está delimitado por #region y #endregion para facilitar el plegado en VS Code y otros editores.
# Al final de cada capítulo, se incluye un bloque de 10 "Ejercicios Desafío" que usan solo
# los conceptos vistos hasta ese punto.
#
# Creado por: Tu Asistente Gemini
# Fecha: 30 de junio de 2025
#-----------------------------------------------------------------------------------------------------------------------
#endregion

# ======================================================================================================================
# PARTE I: CONCEPTOS BÁSICOS
# ======================================================================================================================


#region CAPÍTULO 1: INTRODUCCIÓN Y CONFIGURACIÓN

# ======================================================================================================================
#region CAPÍTULO 1: INTRODUCCIÓN Y CONFIGURACIÓN
# ======================================================================================================================
#
# Este capítulo se enfoca en la configuración del entorno de programación, que incluye la instalación de Python
# y un editor de texto como VS Code. Se recomienda Python 3.9 o superior.
#
# Concepto clave:
# - El programa "Hello World" es una tradición para verificar que el entorno de desarrollo funciona correctamente.
#   Su ejecución exitosa confirma que Python está instalado y configurado para correr scripts.
#

### Ejemplo de código: "Hello World" (hello_world.py)
# Guarda este código en un archivo llamado `hello_world.py` y ejecútalo desde tu terminal
# o editor para verificar tu instalación de Python.

# print("Hello Python world!")


### Ejercicios de Práctica (TRY IT YOURSELF)
# Estos ejercicios del Capítulo 1 son de naturaleza exploratoria y no requieren código complejo.
print("\n" + "="*80)
print("=== CAPÍTULO 1: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

# 1-1. python.org:
# Explora la página de inicio de Python (https://python.org) para familiarizarte con los recursos disponibles.

# 1-2. Hello World Typos:
# Introduce intencionalmente errores de escritura en tu archivo `hello_world.py`
# (por ejemplo, olvidando comillas o paréntesis) y observa los mensajes de error.
# Esto te ayuda a familiarizarte con la sintaxis estricta de Python y los tracebacks.

# 1-3. Infinite Skills:
# Piensa en 3 programas que te gustaría construir si tuvieras habilidades de programación ilimitadas.
# Escríbelos como un plan en un cuaderno de ideas. Es un gran hábito para mantenerte motivado.

print("\n(Los ejercicios del Capítulo 1 no tienen código para ejecutar. Revisa los comentarios anteriores.)")
#endregion
#region === INICIO EJERCICIOS DESAFÍO CAPÍTULO 1 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 1 ===")
print("="*80)

# 1. Investigación de Python:
#    Nombra tres áreas diferentes donde Python es ampliamente utilizado.
#    (No requiere código, solo investigación y respuesta como comentario).

# 2. Diferencia entre Intérprete y Script:
#    Explica brevemente la diferencia entre ejecutar código Python directamente en el intérprete
#    (línea por línea) y ejecutar un script (`.py` file).

# 3. Importancia del Editor de Texto:
#    ¿Por qué se recomienda usar un editor de texto como VS Code en lugar de un bloc de notas simple para Python?
#    Menciona al menos dos beneficios.

# 4. Primeros Pasos de Depuración:
#    Si tu programa `hello_world.py` no funciona, ¿cuáles serían los primeros tres pasos que intentarías para solucionar el problema?

# 5. Planificación de Proyecto Simple:
#    Piensa en una tarea simple que te gustaría automatizar en tu computadora (ej. renombrar archivos, organizar fotos).
#    Describe en un comentario qué harías y qué información necesitaría tu "programa" para empezar.

# 6. Filosofía de "Baterías Incluidas":
#    Investiga qué significa la frase "Python viene con baterías incluidas" en el contexto de la programación.

# 7. Obtención de Ayuda:
#    Si te atascas en un problema de configuración o en un concepto básico, ¿dónde buscarías ayuda en línea (sin usar foros avanzados o sitios de preguntas y respuestas aún)?

# 8. Compatibilidad de Versiones:
#    ¿Por qué es importante saber qué versión de Python estás usando (por ejemplo, Python 2 vs. Python 3)?

# 9. Ventajas de Python para Principiantes:
#    Menciona dos razones por las cuales Python es un buen lenguaje de programación para principiantes.

# 10. Tu Motivación:
#     En una o dos oraciones, explica qué te motiva más a aprender a programar en Python.
#     (No requiere código).


print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 1 ===")
print("="*80 + "\n")
#endregion
#endregion

#region CAPÍTULO 2: VARIABLES Y TIPOS DE DATOS SIMPLES

# ======================================================================================================================
# CAPÍTULO 2: VARIABLES Y TIPOS DE DATOS SIMPLES
# ======================================================================================================================
#
# Este capítulo introduce los conceptos fundamentales de variables y los tipos de datos básicos en Python.
#
# Conceptos clave:
# - Variables: Nombres que se refieren a valores en la memoria. Pueden ser reasignadas en cualquier momento.
# - Strings: Secuencias de caracteres. Se definen con comillas simples ('') o dobles ("").
# - Métodos de Strings: Funciones que operan sobre strings, como `.title()`, `.upper()`, `.lower()`, `.strip()`, etc.
# - f-strings: Una forma poderosa de insertar valores de variables directamente en un string. Se prefixa con `f`.
# - Números: Enteros (`int`) y flotantes (`float`). Se pueden realizar operaciones matemáticas (+, -, *, /, **).
#   La división (`/`) siempre devuelve un flotante.
# - Comentarios: Notas en el código que son ignoradas por el intérprete. Se usa `#`.
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 2: CONCEPTOS Y EJEMPLOS ===")
print("="*80)

print("--- 2.1 Variables ---")
# Una variable es una etiqueta que apunta a un valor.
message = "Hola, esta es una variable."
print(message)

# Puedes cambiar el valor de una variable en cualquier momento.
message = "El valor de la variable ha sido cambiado."
print(message)


print("\n--- 2.2 Strings ---")
# Uso de comillas simples y dobles para definir strings.
string1 = "Esto es un string con comillas dobles."
string2 = 'Esto es un string con comillas simples.'
print(string1)
print(string2)

# Métodos para cambiar mayúsculas y minúsculas.
name = "ada lovelace"
print(f"Original: {name}")
print(f"title(): {name.title()}") # Cada palabra con mayúscula inicial.
print(f"upper(): {name.upper()}") # Todo en mayúsculas.
print(f"lower(): {name.lower()}") # Todo en minúsculas.

# Usando f-strings para insertar variables.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"\nUsando f-string: Hello, {full_name.title()}!")

# Espacios en blanco (`whitespace`): tabulaciones (`\t`) y nuevas líneas (`\n`).
print("\nLista de lenguajes:\n\tPython\n\tC\n\tJavaScript")

# Eliminando espacios en blanco extra.
favorite_language = ' python '
print(f"Original:   '{favorite_language}'")
print(f"lstrip():   '{favorite_language.lstrip()}'") # Elimina espacios a la izquierda.
print(f"rstrip():   '{favorite_language.rstrip()}'") # Elimina espacios a la derecha.
print(f"strip():    '{favorite_language.strip()}'")  # Elimina espacios en ambos lados.

# Eliminando prefijos y sufijos.
url = 'https://www.google.com'
print(f"URL sin prefijo: {url.removeprefix('https://')}")
filename = 'reporte.txt'
print(f"Nombre de archivo sin sufijo: {filename.removesuffix('.txt')}")


print("\n--- 2.3 Números ---")
# Operaciones con enteros.
print(f"Suma: {2 + 3}")
print(f"Resta: {10 - 2}")
print(f"Multiplicación: {2 * 4}")
print(f"División: {16 / 2}") # La división siempre devuelve un flotante.
print(f"Exponente: {2**3}")

# Guiones bajos para legibilidad en números grandes.
universe_age = 14_000_000_000
print(f"Edad del universo: {universe_age}")

# Asignación múltiple en una sola línea.
x, y, z = 0, 0, 0
print(f"Asignación múltiple: x={x}, y={y}, z={z}")

# Constantes (por convención, se nombran en mayúsculas).
MAX_CONNECTIONS = 5000
print(f"Valor de la constante: {MAX_CONNECTIONS}")

print("\n--- 2.4 Comentarios ---")
# Los comentarios son líneas que comienzan con #.
# Son útiles para explicar el código o para desactivar temporalmente una línea.
print("Esta línea se ejecuta, el comentario no.") # Este es un comentario.


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 2: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

### Ejercicio 2-1. Simple Message
# Asigna un mensaje a una variable y luego imprime ese mensaje.
simple_message_ex = "Hola, este es un mensaje."
print(f"2-1: {simple_message_ex}")

### Ejercicio 2-2. Simple Messages
# Asigna un mensaje a una variable, imprímelo, cambia su valor y vuelve a imprimirlo.
message_ex2 = "Este es el primer mensaje del ejercicio 2-2."
print(f"2-2: {message_ex2}")
message_ex2 = "Este es el nuevo mensaje del ejercicio 2-2."
print(f"2-2: {message_ex2}")

### Ejercicio 2-3. Personal Message
# Usa una variable para el nombre y crea un mensaje personalizado.
name_ex = "Eric"
message_ex = f"Hello {name_ex}, would you like to learn some Python today?"
print(f"2-3: {message_ex}")

### Ejercicio 2-4. Name Cases
# Usa una variable para un nombre y muéstralo en diferentes formatos de capitalización.
name_cases_ex = "ada lovelace"
print(f"2-4: Lowercase: {name_cases_ex.lower()}")
print(f"2-4: Uppercase: {name_cases_ex.upper()}")
print(f"2-4: Title case: {name_cases_ex.title()}")

### Ejercicio 2-5. Famous Quote
# Imprime una cita famosa con su autor, incluyendo las comillas.
print('2-5: Albert Einstein once said, "A person who never made a mistake never tried anything new."')

### Ejercicio 2-6. Famous Quote 2
# Usa variables para el autor y la cita, luego crea un mensaje y imprímelo.
famous_person_ex = "Albert Einstein"
quote_ex = "A person who never made a mistake never tried anything new."
message_from_quote_ex = f'{famous_person_ex} once said, "{quote_ex}"'
print(f"2-6: {message_from_quote_ex}")

### Ejercicio 2-7. Stripping Names
# Muestra un nombre con espacios en blanco y luego utiliza las funciones para eliminarlos.
name_with_whitespace_ex = "\t\n  John Doe  \n\t"
print(f"2-7: Original:\n'{name_with_whitespace_ex}'")
print(f"2-7: lstrip():\n'{name_with_whitespace_ex.lstrip()}'")
print(f"2-7: rstrip():\n'{name_with_whitespace_ex.rstrip()}'")
print(f"2-7: strip():\n'{name_with_whitespace_ex.strip()}'")

### Ejercicio 2-8. File Extensions
# Utiliza el método `removesuffix()` para eliminar una extensión de archivo.
filename_ex = 'python_notes.txt'
print(f"2-8: {filename_ex.removesuffix('.txt')}")

### Ejercicio 2-9. Number Eight
# Realiza operaciones aritméticas que resulten en el número 8.
print(f"2-9: Suma: {5+3}")
print(f"2-9: Resta: {10-2}")
print(f"2-9: Multiplicación: {4*2}")
print(f"2-9: División: {int(16/2)}")

### Ejercicio 2-10. Favorite Number
# Almacena un número favorito en una variable y crea un mensaje para revelarlo.
favorite_number_ex = 7
message_fav_number_ex = f"Mi número favorito es el {favorite_number_ex}."
print(f"2-10: {message_fav_number_ex}")

### Ejercicio 2-11. Adding Comments
# Este ejercicio requiere que añadas tus propios comentarios a tus programas.
print("\n2-11: Revisa el código de esta guía para ver ejemplos de comentarios. ¡Añádelos a tus propios scripts!")

### Ejercicio 2-12. Zen of Python
# Este ejercicio se realiza en la terminal de Python.
print("2-12: Para este ejercicio, abre tu terminal Python y escribe 'import this' para ver los principios de diseño de Python.")



# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 2 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 2 ===")
print("="*80)

# 1. Calculadora Simple de Área:
#    Crea variables para la longitud y el ancho de un rectángulo (números enteros o flotantes).
#    Calcula el área del rectángulo y guárdala en una nueva variable.
#    Imprime el área usando un mensaje f-string.
#    Ejemplo: "El área del rectángulo con longitud 5 y ancho 10 es 50."
longitud = 12.5
ancho = 8
area = longitud * ancho
print(f"1. El área del rectángulo con longitud {longitud} y ancho {ancho} es {area}.")

# 2. Manipulación de Nombre Completo:
#    Crea dos variables, `nombre` y `apellido`.
#    Crea una tercera variable `nombre_completo` combinándolas.
#    Imprime `nombre_completo` en:
#    a) Mayúsculas.
#    b) Minúsculas.
#    c) Título de caso (inicial de cada palabra en mayúscula).
nombre = "carlos"
apellido = "gomez"
nombre_completo = f"{nombre} {apellido}"
print(f"2a. Nombre completo en mayúsculas: {nombre_completo.upper()}")
print(f"2b. Nombre completo en minúsculas: {nombre_completo.lower()}")
print(f"2c. Nombre completo en título de caso: {nombre_completo.title()}")

# 3. Mensaje Multilínea y Tabulaciones:
#    Usa una sola variable de tipo string para almacenar el siguiente poema (o frase larga)
#    asegurándote de que cada línea nueva y tabulación se muestre correctamente al imprimir:
#    "El Python es:\n\t- Simple\n\t- Versátil\n\t- Potente"
poema_python = "El Python es:\n\t- Simple\n\t- Versátil\n\t- Potente"
print(f"3. {poema_python}")

# 4. Formateador de Precios:
#    Crea una variable `precio_unitario` (ej. 15.75) y `cantidad` (ej. 3).
#    Calcula el `total`.
#    Imprime el `total` en un mensaje f-string con un símbolo de moneda y un mensaje descriptivo.
#    Asegúrate de que el total tenga solo dos decimales si Python lo muestra con más (investiga cómo hacerlo).
#    Nota: Para los decimales, se espera usar un método de string, no redondeo numérico aún.
precio_unitario = 15.75
cantidad = 3
total = precio_unitario * cantidad
print(f"4. El total de la compra es: ${total:.2f}")

# 5. Corrector de Formato de URL:
#    Una variable `url_su_cadena` contiene una URL con espacios en blanco al principio y al final,
#    y quizás con "www." o "http://" al inicio (ej. "  http://www.ejemplo.com  ").
#    Limpia la URL para que solo muestre el dominio principal (ej. "ejemplo.com").
#    Imprime la URL original y la limpia.
url_su_cadena = "  http://www.ejemplo.com  "
url_limpia = url_su_cadena.strip().removeprefix("http://").removeprefix("https://").removeprefix("www.")
print(f"5. URL original: '{url_su_cadena}'")
print(f"   URL limpia: '{url_limpia}'")

# 6. Juego de Palabras con Variables:
#    Crea tres variables de string: `adjetivo`, `sustantivo`, `verbo`.
#    Imprime una frase graciosa o creativa usando estas tres variables y f-strings.
adjetivo = "brillante"
sustantivo = "unicornio"
verbo = "bailó"
print(f"6. El {adjetivo} {sustantivo} {verbo} felizmente bajo la luna.")

# 7. Contador de Edad en Meses y Días:
#    Crea una variable `edad_años` (número entero).
#    Calcula e imprime cuántos meses y aproximadamente cuántos días ha vivido esa persona.
edad_años = 30
meses_vividos = edad_años * 12
dias_vividos = edad_años * 365 # Aproximado, sin considerar años bisiestos.
print(f"7. Una persona de {edad_años} años ha vivido aproximadamente {meses_vividos} meses y {dias_vividos} días.")

# 8. Generador de Nombre de Archivo:
#    Crea variables `proyecto` y `version` (strings).
#    Crea una variable `nombre_archivo` que combine estos elementos y el sufijo ".zip".
#    Imprime el `nombre_archivo`.
#    Ejemplo: `proyecto`="mi_app", `version`="1.0" -> `nombre_archivo`="mi_app_v1.0.zip"
proyecto = "mi_app"
version = "1.0"
nombre_archivo = f"{proyecto}_v{version}.zip"
print(f"8. El nombre del archivo generado es: {nombre_archivo}")

# 9. Cadena de Transformación de String:
#    Toma un string (ej. "  python es divertido  ").
#    Realiza en una sola línea de código las siguientes operaciones:
#    a) Eliminar espacios en blanco de ambos extremos.
#    b) Convertir la primera letra de cada palabra a mayúscula.
#    c) Añadir un signo de exclamación al final.
#    Imprime el resultado.
cadena_original = "  python es divertido  "
cadena_transformada = cadena_original.strip().title() + "!"
print(f"9. Cadena original: '{cadena_original}'")
print(f"   Cadena transformada: '{cadena_transformada}'")

# 10. Cálculos de Descuento:
#     Un producto cuesta `$75.50`. Se aplica un descuento del `15%`.
#     Calcula el precio final después del descuento.
#     Imprime el precio original, el porcentaje de descuento y el precio final, formateando los precios a dos decimales.
precio_original = 75.50
porcentaje_descuento = 0.15
descuento = precio_original * porcentaje_descuento
precio_final = precio_original - descuento
print(f"10. Precio original: ${precio_original:.2f}, Descuento: {porcentaje_descuento*100:.0f}%, Precio final: ${precio_final:.2f}")

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 2 ===")
print("="*80 + "\n")

#endregion

#region CAPÍTULO 3: INTRODUCCIÓN A LAS LISTAS

# ======================================================================================================================
# CAPÍTULO 3: INTRODUCCIÓN A LAS LISTAS
# ======================================================================================================================
#
# Este capítulo presenta las listas, colecciones ordenadas de elementos.
#
# Conceptos clave:
# - Listas: Se definen con corchetes `[]` y sus elementos están separados por comas.
# - Indexación: Los elementos se acceden por su posición, que comienza en 0.
#   - `lista[0]` es el primer elemento. `lista[-1]` es el último.
# - Modificar elementos: Se puede cambiar un elemento por su índice.
# - Añadir elementos: `append()` para añadir al final, `insert()` para añadir en cualquier posición.
# - Eliminar elementos:
#   - `del`: Elimina un elemento por su índice permanentemente.
#   - `pop()`: Elimina y devuelve el último elemento. Puede eliminar por índice.
#   - `remove()`: Elimina un elemento por su valor.
# - Organizar listas:
#   - `sort()`: Ordena la lista permanentemente.
#   - `sorted()`: Devuelve una copia ordenada sin modificar la original.
#   - `reverse()`: Invierte el orden de la lista permanentemente.
# - Longitud de la lista: `len(lista)` devuelve el número de elementos.
# - Errores de índice: `IndexError` si intentas acceder a un índice fuera de rango.
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 3: CONCEPTOS Y EJEMPLOS ===")
print("="*80)

print("--- 3.1 Creando y accediendo a listas ---")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f"Lista completa: {bicycles}")
print(f"Primer elemento (índice 0): {bicycles[0].title()}")
print(f"Último elemento (índice -1): {bicycles[-1].title()}")


print("\n--- 3.2 Modificando, añadiendo y eliminando elementos ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"Original: {motorcycles}")

# Modificar un elemento.
motorcycles[0] = 'ducati'
print(f"Modificado: {motorcycles}")

# Añadir elementos.
motorcycles.append('honda') # Añade al final.
print(f"Después de append(): {motorcycles}")
motorcycles.insert(0, 'kawasaki') # Inserta en el índice 0.
print(f"Después de insert(): {motorcycles}")

# Eliminar elementos.
del motorcycles[0] # Elimina por índice.
print(f"Después de del: {motorcycles}")

popped_motorcycle = motorcycles.pop() # Elimina y devuelve el último elemento.
print(f"Lista después de pop(): {motorcycles}")
print(f"Elemento eliminado con pop(): {popped_motorcycle.title()}")

motorcycles.remove('yamaha') # Elimina por valor.
print(f"Después de remove(): {motorcycles}")


print("\n--- 3.3 Organizando una lista ---")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Lista original: {cars}")

# Ordenar permanentemente.
cars.sort()
print(f"Ordenado permanentemente con sort(): {cars}")
cars.sort(reverse=True)
print(f"Ordenado en orden inverso con sort(): {cars}")

# Ordenar temporalmente.
cars_temp = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\nLista original para sorted(): {cars_temp}")
print(f"Ordenado temporalmente con sorted(): {sorted(cars_temp)}")
print(f"Lista original después de sorted(): {cars_temp} (sin cambios)")

# Invertir el orden permanentemente.
cars_rev = ['bmw', 'audi', 'toyota', 'subaru']
cars_rev.reverse()
print(f"\nOrden invertido permanentemente con reverse(): {cars_rev}")


print("\n--- 3.4 Longitud de una lista y errores de índice ---")
print(f"La longitud de la lista de coches es: {len(cars)}")

# Ejemplo de IndexError (comentado para evitar el error al ejecutar).
# my_list = [1, 2, 3]
# print(my_list[3]) # Intentar acceder al índice 3 en una lista de 3 elementos causa un IndexError.


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 3: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

### Ejercicio 3-1. Names
# Almacena nombres en una lista y accede a cada uno individualmente.
names = ['Ana', 'Juan', 'Sofia']
print(f"3-1: {names[0]}")
print(f"3-1: {names[1]}")
print(f"3-1: {names[2]}")

### Ejercicio 3-2. Greetings
# Crea un mensaje personalizado para cada nombre en la lista anterior.
for name in names:
    print(f"3-2: Hola, {name}, ¿cómo estás hoy?")

### Ejercicio 3-3. Your Own List
# Crea una lista de tus modos de transporte favoritos y haz declaraciones sobre ellos.
transportations = ['Honda motorcycle', 'Tesla car', 'Yamaha bicycle']
print(f"3-3: Me gustaría tener una {transportations[0].lower()}.")
print(f"3-3: El {transportations[1].lower()} es muy moderno.")
print(f"3-3: Me gusta montar mi {transportations[2].lower()} por la mañana.")

### Ejercicio 3-4. Guest List
# Crea una lista de invitados a una cena y envíales una invitación.
guest_list = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
print("\n3-4: Lista inicial de invitados:")
for guest in guest_list:
    print(f"Estimado/a {guest}, te invito a cenar a mi casa.")

### Ejercicio 3-5. Changing Guest List
# Modifica la lista de invitados porque uno no puede asistir.
print(f"\n3-5: Lamentablemente, {guest_list[1]} no puede asistir.")
guest_list[1] = 'Leonardo da Vinci' # Reemplazando un invitado.
print("\n3-5: Nueva lista de invitados:")
for guest in guest_list:
    print(f"Estimado/a {guest}, te re-invito a cenar. ¡Te esperamos!")

### Ejercicio 3-6. More Guests
# Simula encontrar una mesa más grande y añade más invitados.
print("\n3-6: ¡Buenas noticias! Encontré una mesa de cena más grande.")
guest_list.insert(0, 'Ada Lovelace') # Añadir al principio.
guest_list.insert(2, 'Galileo Galilei') # Añadir al medio.
guest_list.append('Nikola Tesla') # Añadir al final.
print("\n3-6: Lista de invitados actualizada:")
for guest in guest_list:
    print(f"Estimado/a {guest}, ¡te invito a cenar! Tenemos más espacio.")

### Ejercicio 3-7. Shrinking Guest List
# Recorta la lista de invitados a solo dos personas.
print("\n3-7: Lo siento, la mesa no llegará a tiempo. Solo puedo invitar a dos personas.")
while len(guest_list) > 2: # Usando pop() para eliminar invitados.
    removed_guest = guest_list.pop()
    print(f"3-7: Lo siento, {removed_guest}, no podré invitarte a cenar.")
print("\n3-7: Los dos invitados restantes son:")
for guest in guest_list:
    print(f"3-7: Estimado/a {guest}, ¡todavía estás invitado a cenar!")
# Elimina los últimos dos con del.
del guest_list[0]
del guest_list[0]
print(f"\n3-7: Lista final de invitados: {guest_list}. ¡Está vacía!")

### Ejercicio 3-8. Seeing the World
# Almacena una lista de lugares y muestra diferentes formas de ordenarla.
locations = ['tokyo', 'paris', 'new york', 'machu picchu', 'cairo']
print("\n3-8: Lista original:")
print(locations)
print("\n3-8: Lista ordenada temporalmente:")
print(sorted(locations))
print("3-8: Lista original nuevamente:")
print(locations)
print("\n3-8: Lista ordenada temporalmente en orden inverso:")
print(sorted(locations, reverse=True))
print("3-8: Lista original nuevamente:")
print(locations)
locations.reverse()
print("\n3-8: Lista con orden invertido permanentemente:")
print(locations)
locations.reverse()
print("3-8: Lista de vuelta a su orden original:")
print(locations)
locations.sort()
print("\n3-8: Lista ordenada alfabéticamente (permanente):")
print(locations)
locations.sort(reverse=True)
print("3-8: Lista ordenada alfabéticamente inversa (permanente):")
print(locations)

### Ejercicio 3-9. Dinner Guests
# Usa `len()` para contar el número de invitados.
guest_list_3_9 = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
print(f"\n3-9: Estoy invitando a {len(guest_list_3_9)} personas a cenar.")

### Ejercicio 3-10. Every Function
# Crea una lista y usa todas las funciones de lista introducidas en el capítulo.
things = ['mountain', 'river', 'country', 'city', 'language']
print("\n3-10: Lista original:")
print(things)
things.append('desert') # append()
print(f"Después de append(): {things}")
things.insert(0, 'ocean') # insert()
print(f"Después de insert(): {things}")
del things[0] # del
print(f"Después de del: {things}")
popped_item = things.pop() # pop()
print(f"Después de pop(): {things}")
things.remove('river') # remove()
print(f"Después de remove(): {things}")
print(f"Longitud de la lista: {len(things)}") # len()
print(f"Lista ordenada temporalmente: {sorted(things)}") # sorted()
things.sort() # sort()
print(f"Lista ordenada permanentemente: {things}")
things.reverse() # reverse()
print(f"Lista invertida permanentemente: {things}")

### Ejercicio 3-11. Intentional Error
# Este ejercicio requiere que generes un error de índice a propósito.
print("\n3-11: Este código genera un IndexError, está comentado para evitar el error al ejecutar.")
# my_list = [1, 2, 3]
# print(my_list[3]) # Esto causa un IndexError porque el índice 3 está fuera de rango.




# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 3 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 3 ===")
print("="*80)

# 1. Gestión de Playlist Musical:
#    Crea una lista `playlist` con al menos 5 canciones (strings).
#    a) Imprime la playlist completa.
#    b) Mueve la primera canción al final de la playlist.
#    c) Elimina una canción específica por su nombre.
#    d) Inserta una nueva canción en la segunda posición.
#    e) Imprime la playlist final ordenada alfabéticamente de forma permanente.
playlist = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine", "Hey Jude"]
print(f"1a. Playlist original: {playlist}")
primera_cancion = playlist.pop(0)
playlist.append(primera_cancion)
print(f"1b. Playlist con primera canción al final: {playlist}")
playlist.remove("Hotel California")
print(f"1c. Playlist sin 'Hotel California': {playlist}")
playlist.insert(1, "Don't Stop Me Now")
print(f"1d. Playlist con nueva canción insertada: {playlist}")
playlist.sort()
print(f"1e. Playlist final ordenada: {playlist}")

# 2. Lista de Tareas Pendientes:
#    Crea una lista `tareas` con 4-5 tareas.
#    a) Imprime "Tareas pendientes:" y cada tarea.
#    b) Marca una tarea como "Completada" (modificando el string en la lista).
#    c) Añade una nueva tarea al final.
#    d) Elimina la primera tarea.
#    e) Imprime la lista de tareas ordenada inversamente de forma temporal.
tareas = ["Comprar víveres", "Llamar al banco", "Enviar email", "Estudiar Python"]
print("\n2a. Tareas pendientes:")
for tarea in tareas:
    print(f"- {tarea}")
tareas[0] = "Comprar víveres (Completada)"
print(f"2b. Tarea marcada como completada: {tareas}")
tareas.append("Hacer ejercicio")
print(f"2c. Nueva tarea añadida: {tareas}")
del tareas[0]
print(f"2d. Primera tarea eliminada: {tareas}")
print(f"2e. Tareas ordenadas inversamente (temporal): {sorted(tareas, reverse=True)}")

# 3. Registro de Puntajes:
#    Crea una lista `puntajes` con 6-8 puntajes de juegos (números).
#    a) Imprime los puntajes en su orden original.
#    b) Imprime los 3 puntajes más altos (sin modificar la lista original).
#    c) Elimina el puntaje más bajo de la lista de forma permanente.
#    d) Añade un nuevo puntaje.
#    e) Imprime la lista final ordenada de menor a mayor.
puntajes = [1500, 2300, 800, 3100, 1900, 2700]
print(f"\n3a. Puntajes originales: {puntajes}")
print(f"3b. Los 3 puntajes más altos: {sorted(puntajes, reverse=True)[:3]}")
puntajes.sort()
puntajes.pop(0) # Elimina el más bajo después de ordenar.
print(f"3c. Puntaje más bajo eliminado: {puntajes}")
puntajes.append(2500)
print(f"3d. Nuevo puntaje añadido: {puntajes}")
puntajes.sort()
print(f"3e. Puntajes finales ordenados: {puntajes}")

# 4. Inventario de Frutas:
#    Crea una lista `frutas_inventario` con 4-5 frutas.
#    a) Imprime el inventario.
#    b) Elimina la fruta del medio usando `pop()` y un índice calculado con `len()`.
#    c) Añade dos frutas nuevas.
#    d) Verifica si una fruta específica está en el inventario.
#    e) Imprime el inventario final en orden alfabético inverso permanente.
frutas_inventario = ["Manzana", "Banana", "Cereza", "Dátil", "Fresa"]
print(f"\n4a. Inventario de frutas: {frutas_inventario}")
indice_medio = len(frutas_inventario) // 2
fruta_media = frutas_inventario.pop(indice_medio)
print(f"4b. Fruta eliminada del medio: {fruta_media}. Inventario: {frutas_inventario}")
frutas_inventario.append("Uva")
frutas_inventario.append("Kiwi")
print(f"4c. Dos frutas nuevas añadidas: {frutas_inventario}")
fruta_buscada = "Banana"
if fruta_buscada in frutas_inventario:
    print(f"4d. Sí, {fruta_buscada} está en el inventario.")
else:
    print(f"4d. No, {fruta_buscada} no está en el inventario.")
frutas_inventario.sort(reverse=True)
print(f"4e. Inventario final en orden inverso: {frutas_inventario}")

# 5. Lista de Deseos (Wishlist):
#    Crea una lista `wishlist` con 3-4 ítems.
#    a) Imprime la wishlist.
#    b) Cambia el primer ítem por otro.
#    c) Elimina el último ítem usando `del`.
#    d) Añade un ítem al principio.
#    e) Imprime la longitud final de la wishlist.
wishlist = ["Laptop gaming", "Viaje a Japón", "Cámara fotográfica"]
print(f"\n5a. Wishlist original: {wishlist}")
wishlist[0] = "Consola de nueva generación"
print(f"5b. Primer ítem cambiado: {wishlist}")
del wishlist[-1]
print(f"5c. Último ítem eliminado: {wishlist}")
wishlist.insert(0, "Libro de Python")
print(f"5d. Ítem añadido al principio: {wishlist}")
print(f"5e. Longitud final de la wishlist: {len(wishlist)}")

# 6. Ciudades Visitadas (Orden):
#    Crea una lista `ciudades_visitadas` con al menos 5 ciudades en un orden aleatorio.
#    a) Imprime la lista original.
#    b) Crea una copia ordenada alfabéticamente (sin modificar la original) e imprímela.
#    c) Ordena la lista original alfabéticamente de forma permanente e imprímela.
#    d) Invierte el orden de la lista original de forma permanente e imprímela.
#    e) Vuelve a invertirla para que regrese a un orden diferente al original (pero no necesariamente el primer original) y imprímela.
ciudades_visitadas = ["Londres", "París", "Tokio", "Roma", "Nueva York", "Berlín"]
print(f"\n6a. Ciudades visitadas original: {ciudades_visitadas}")
print(f"6b. Copia ordenada: {sorted(ciudades_visitadas)}")
ciudades_visitadas.sort()
print(f"6c. Original ordenada permanentemente: {ciudades_visitadas}")
ciudades_visitadas.reverse()
print(f"6d. Original invertida permanentemente: {ciudades_visitadas}")
ciudades_visitadas.reverse() # Vuelve a invertir.
print(f"6e. Original nuevamente invertida: {ciudades_visitadas}")

# 7. Gestión de Invitados con Pop y Del Mixto:
#    Comienza con una lista de 4 invitados.
#    a) Elimina al segundo invitado usando `pop()` y un mensaje.
#    b) Elimina al último invitado usando `del`.
#    c) Añade un nuevo invitado en la posición que elijas.
#    d) Imprime la lista final de invitados.
invitados_evento = ["Ana", "Beto", "Carlos", "Diana"]
print(f"\n7a. Invitados iniciales: {invitados_evento}")
invitado_eliminado_pop = invitados_evento.pop(1) # Elimina a Beto.
print(f"7a. Invitado eliminado con pop(): {invitado_eliminado_pop}. Lista: {invitados_evento}")
del invitados_evento[-1] # Elimina a Diana.
print(f"7b. Invitado eliminado con del: {invitados_evento}")
invitados_evento.insert(1, "Elena")
print(f"7c. Invitado añadido: {invitados_evento}")
print(f"7d. Lista final de invitados: {invitados_evento}")

# 8. Números Favoritos:
#    Crea una lista `numeros_favoritos` con 5 números.
#    a) Imprime el número más pequeño y el más grande en la lista.
#    b) Añade un número a la lista.
#    c) Elimina dos ocurrencias del mismo número (si lo hay, si no, elimina dos números cualquiera).
#    d) Ordena la lista de forma permanente de mayor a menor.
numeros_favoritos = [7, 3, 15, 2, 8]
print(f"\n8a. Números favoritos: {numeros_favoritos}")
print(f"   Número más pequeño: {min(numeros_favoritos)}")
print(f"   Número más grande: {max(numeros_favoritos)}")
numeros_favoritos.append(10)
print(f"8b. Número añadido: {numeros_favoritos}")
if 7 in numeros_favoritos:
    numeros_favoritos.remove(7)
if 8 in numeros_favoritos:
    numeros_favoritos.remove(8)
print(f"8c. Después de eliminar dos números: {numeros_favoritos}")
numeros_favoritos.sort(reverse=True)
print(f"8d. Lista ordenada de mayor a menor: {numeros_favoritos}")

# 9. Cadena de Restaurantes (Lista de Strings):
#    Crea una lista `restaurantes` con 4-5 nombres de restaurantes.
#    a) Imprime el nombre del segundo restaurante.
#    b) Modifica el nombre del cuarto restaurante.
#    c) Añade un nuevo restaurante al principio.
#    d) Elimina el último restaurante.
#    e) Imprime la lista en orden alfabético temporal.
restaurantes = ["La Taberna", "El Gourmet", "Pizza Pazza", "Burger Joint"]
print(f"\n9a. Segundo restaurante: {restaurantes[1]}")
restaurantes[3] = "The New Grill"
print(f"9b. Cuarto restaurante modificado: {restaurantes}")
restaurantes.insert(0, "Café Central")
print(f"9c. Nuevo restaurante al principio: {restaurantes}")
restaurantes.pop() # Elimina el último, que ahora es "The New Grill"
print(f"9d. Último restaurante eliminado: {restaurantes}")
print(f"9e. Lista en orden alfabético temporal: {sorted(restaurantes)}")

# 10. Estados de un Proyecto (Conteo):
#     Crea una lista `estados_proyecto` con 7-10 elementos que representen fases (ej. "Inicio", "Desarrollo", "Pruebas", "Despliegue", "Finalizado").
#     Asegúrate de que algunos estados se repitan.
#     a) Imprime la lista completa.
#     b) Elimina todas las ocurrencias de un estado específico (ej. "Pruebas") usando un bucle `while` y `remove()`.
#     c) Añade un nuevo estado.
#     d) Imprime la lista final y su longitud.
estados_proyecto = ["Inicio", "Desarrollo", "Pruebas", "Desarrollo", "Pruebas", "Despliegue", "Finalizado"]
print(f"\n10a. Estados del proyecto: {estados_proyecto}")
while "Pruebas" in estados_proyecto:
    estados_proyecto.remove("Pruebas")
print(f"10b. Estados sin 'Pruebas': {estados_proyecto}")
estados_proyecto.append("Mantenimiento")
print(f"10c. Nuevo estado añadido: {estados_proyecto}")
print(f"10d. Lista final de estados: {estados_proyecto}")
print(f"    Longitud final: {len(estados_proyecto)}")

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 3 ===")
print("="*80 + "\n")

#endregion

#region CAPÍTULO 4: TRABAJANDO CON LISTAS

# ======================================================================================================================
# CAPÍTULO 4: TRABAJANDO CON LISTAS
# ======================================================================================================================
#
# Este capítulo se centra en los bucles (`for`) para iterar a través de listas y trabajar con porciones de datos.
#
# Conceptos clave:
# - Bucle `for`: Ejecuta un bloque de código para cada elemento en una lista. La indentación define el bloque.
# - Listas numéricas:
#   - `range(start, end)`: Genera una secuencia de números. `end` no está incluido.
#   - `list(range(...))`: Convierte un `range` en una lista.
#   - `min()`, `max()`, `sum()`: Funciones para estadísticas básicas.
# - Comprensión de listas (`List Comprehensions`): Una sintaxis concisa para crear listas. `[expresion for item in iterable]`.
# - Porciones de listas (`Slicing`): Permite seleccionar un subconjunto de elementos. `lista[inicio:fin]`.
# - Copiar una lista: `nueva_lista = lista[:]` para crear una copia independiente.
# - Tuplas: Listas inmutables (no se pueden modificar). Se definen con paréntesis `()`.
# - Estilo de código (PEP 8):
#   - 4 espacios de indentación.
#   - Líneas de código de menos de 80 caracteres.
#   - Líneas en blanco para agrupar bloques de código.
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 4: CONCEPTOS Y EJEMPLOS ===")
print("="*80)

print("--- 4.1 Bucle for ---")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# La indentación determina el alcance del bucle.
for magician in magicians:
    print(f"{magician.title()}, ¡ese fue un gran truco!")
    print(f"No puedo esperar para ver tu próximo truco, {magician.title()}.\n")

# Las líneas sin indentación se ejecutan después de que el bucle termina.
print("¡Gracias a todos! Ese fue un gran espectáculo de magia.")


print("\n--- 4.2 Listas numéricas ---")
# Usando range().
print("Números del 1 al 4:")
for value in range(1, 5): # El 5 no está incluido.
    print(value)

# Creando una lista a partir de range().
numbers = list(range(1, 6))
print(f"Lista de números: {numbers}")

# Usando el tercer argumento para el paso.
even_numbers = list(range(2, 11, 2))
print(f"Números pares: {even_numbers}")


print("\n--- 4.3 Comprensión de listas (List Comprehensions) ---")
# Creación de una lista de cuadrados de forma concisa.
squares_comp = [value**2 for value in range(1, 11)]
print(f"Lista de cuadrados: {squares_comp}")


print("\n--- 4.4 Slicing (Porciones de listas) ---")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f"Primeros 3 elementos: {players[0:3]}")
print(f"Elementos del medio: {players[1:4]}")
print(f"Desde el principio hasta el índice 4: {players[:4]}")
print(f"Desde el índice 2 hasta el final: {players[2:]}")
print(f"Últimos 3 elementos: {players[-3:]}")

# Bucle a través de una porción de la lista.
print("\nLos primeros tres jugadores de mi equipo son:")
for player in players[:3]:
    print(f"- {player.title()}")


print("\n--- 4.5 Copiando una lista ---")
# Crear una copia real para que los cambios en una no afecten a la otra.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # Usando slicing para copiar.
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f"Mis comidas favoritas: {my_foods}")
print(f"Las comidas favoritas de mi amigo: {friend_foods}")


print("\n--- 4.6 Tuplas ---")
# Las tuplas son inmutables. Se definen con paréntesis `()`.
dimensions = (200, 50)
print(f"Dimensión 1: {dimensions[0]}")
print(f"Dimensión 2: {dimensions[1]}")
# Intentar modificar un elemento de una tupla resultaría en un TypeError.
# dimensions[0] = 250 # Esto generaría un error.
# Pero puedes reasignar la tupla completa.
dimensions = (400, 100)
print(f"Nuevas dimensiones: {dimensions}")


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 4: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

### Ejercicio 4-1. Pizzas
# Itera a través de una lista de pizzas y muestra una declaración para cada una.
pizzas = ['pepperoni', 'hawaiana', 'queso']
for pizza in pizzas:
    print(f"4-1: Me gusta la pizza de {pizza}.")
print("4-1: ¡Realmente amo la pizza!")

### Ejercicio 4-2. Animals
# Itera a través de una lista de animales con una característica común.
animals = ['perro', 'gato', 'loro']
for animal in animals:
    print(f"4-2: Un {animal} sería una gran mascota.")
print("4-2: ¡Cualquiera de estos animales sería una gran mascota!")

### Ejercicio 4-3. Counting to Twenty
# Usa un bucle `for` para imprimir los números del 1 al 20.
print("\n4-3: Contando hasta 20:")
for num in range(1, 21):
    print(f"4-3: {num}")

### Ejercicio 4-4. One Million
# Crea una lista con los números hasta un millón y (opcionalmente) imprímelos.
print("\n4-4: Se ha omitido la impresión de un millón de números para evitar una salida muy larga.")
# million_numbers = list(range(1, 1_000_001))
# for number in million_numbers:
#    print(number)

### Ejercicio 4-5. Summing a Million
# Usa `min()`, `max()` y `sum()` en una lista de un millón de números.
print("\n4-5: Sumando un millón:")
million_numbers = list(range(1, 1_000_001))
print(f"4-5: Mínimo: {min(million_numbers)}")
print(f"4-5: Máximo: {max(million_numbers)}")
print(f"4-5: Suma: {sum(million_numbers)}")

### Ejercicio 4-6. Odd Numbers
# Crea una lista de números impares usando `range()` y un bucle `for`.
print("\n4-6: Números impares del 1 al 20:")
odd_numbers = list(range(1, 20, 2))
for odd_num in odd_numbers:
    print(f"4-6: {odd_num}")

### Ejercicio 4-7. Threes
# Crea una lista de múltiplos de 3.
print("\n4-7: Múltiplos de 3:")
threes = list(range(3, 31, 3))
for three in threes:
    print(f"4-7: {three}")

### Ejercicio 4-8. Cubes
# Crea una lista de los primeros 10 cubos usando un bucle.
print("\n4-8: Cubos:")
cubes = []
for number in range(1, 11):
    cubes.append(number**3)
for cube in cubes:
    print(f"4-8: {cube}")

### Ejercicio 4-9. Cube Comprehension
# Crea la misma lista de cubos usando una comprensión de lista.
print("\n4-9: Cubos con list comprehension:")
cubes_comp = [number**3 for number in range(1, 11)]
print(f"4-9: {cubes_comp}")

### Ejercicio 4-10. Slices
# Demuestra porciones de una lista.
print("\n4-10: Porciones de la lista de pizzas:")
print(f"Los primeros tres elementos son: {pizzas[:3]}")
print(f"Tres elementos del medio son: {pizzas[1:4]}")
print(f"Los últimos tres elementos son: {pizzas[-3:]}")

### Ejercicio 4-11. My Pizzas, Your Pizzas
# Crea una copia independiente de una lista para evitar modificaciones compartidas.
pizzas_mine = ['pepperoni', 'hawaiana', 'queso']
pizzas_friend = pizzas_mine[:]
pizzas_mine.append('vegetariana')
pizzas_friend.append('barbacoa')
print("\n4-11: Mis pizzas favoritas:")
for pizza in pizzas_mine:
    print(f"- {pizza}")
print("\n4-11: Las pizzas favoritas de mi amigo:")
for pizza in pizzas_friend:
    print(f"- {pizza}")

### Ejercicio 4-12. More Loops
# Utiliza bucles `for` para imprimir listas.
print("\n4-12: Usando bucles para imprimir las listas de comidas:")
print("\nMis comidas favoritas:")
for food in my_foods:
    print(f"- {food}")
print("\nLas comidas favoritas de mi amigo:")
for food in friend_foods:
    print(f"- {food}")

### Ejercicio 4-13. Buffet
# Trabaja con una tupla para simular un menú inmutable.
print("\n4-13: Buffet del restaurante:")
buffet_foods = ('pollo', 'carne', 'ensalada', 'patatas', 'fruta')
for food in buffet_foods:
    print(f"- {food}")
# Intentar modificar un elemento de una tupla resultaría en un TypeError.
# buffet_foods[0] = 'pescado' # Esto genera un TypeError.
print("\n4-13: El menú ha cambiado.")
buffet_foods = ('pollo', 'pescado', 'pasta', 'patatas', 'postre') # Reescribe la tupla.
for food in buffet_foods:
    print(f"- {food}")

### Ejercicio 4-14. PEP 8
# Visita el sitio web de la guía de estilo de Python para familiarizarte con las convenciones.
print("\n4-14: Este ejercicio requiere visitar el sitio web de PEP 8.")

### Ejercicio 4-15. Code Review
# Revisa tus propios scripts para asegurarte de que cumplen con las guías de estilo de PEP 8.
print("\n4-15: Revisa tu propio código y aplícale el estilo de PEP 8 (indentación, longitud de línea, etc.).")

# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 4 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 4 ===")
print("="*80)

# 1. Generador de Secuencia Fibonacci:
#    Crea una lista vacía.
#    Usa un bucle `for` y `range()` para generar los primeros 10 números de la secuencia de Fibonacci.
#    La secuencia comienza con 0 y 1, y cada número siguiente es la suma de los dos anteriores.
#    Almacena cada número en la lista. Imprime la lista resultante.
fib_sequence = [0, 1]
for _ in range(8): # Ya tenemos 2, necesitamos 8 más para un total de 10.
    next_fib = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib)
print(f"1. Secuencia Fibonacci (primeros 10): {fib_sequence}")

# 2. Suma de Números Pares e Impares en un Rango:
#    Crea dos listas vacías: `pares` e `impares`.
#    Usa un bucle `for` con `range()` para iterar del 1 al 50.
#    Si un número es par, añádelo a la lista `pares`; si es impar, añádelo a `impares`.
#    Finalmente, imprime la suma de los números en cada lista.
pares = []
impares = []
for num in range(1, 51):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"2. Suma de números pares (1-50): {sum(pares)}")
print(f"   Suma de números impares (1-50): {sum(impares)}")

# 3. Analizador Básico de Frase:
#    Dada una frase (string), conviértela a una lista de palabras.
#    Imprime la cantidad total de palabras.
#    Imprime las primeras 3 palabras.
#    Imprime las últimas 2 palabras.
#    Imprime la lista de palabras ordenada alfabéticamente (temporalmente).
frase_analizar = "Python es un lenguaje de programación muy popular y divertido"
palabras = frase_analizar.split()
print(f"3. Frase original: '{frase_analizar}'")
print(f"   Cantidad total de palabras: {len(palabras)}")
print(f"   Primeras 3 palabras: {palabras[:3]}")
print(f"   Últimas 2 palabras: {palabras[-2:]}")
print(f"   Palabras ordenadas (temporalmente): {sorted(palabras)}")

# 4. Multiplicación de Elementos de Lista:
#    Dada una lista de números, calcula el producto de todos sus elementos.
#    Ejemplo: `[1, 2, 3, 4]` -> `24`
numeros_producto = [5, 2, 3, 4]
producto_total = 1
for numero in numeros_producto:
    producto_total *= numero # Multiplicación acumulativa.
print(f"4. Producto de los elementos de {numeros_producto}: {producto_total}")

# 5. Generador de Tablas de Multiplicar (Básica):
#    Usa dos bucles `for` anidados para imprimir la tabla de multiplicar del 1 al 5.
#    Cada fila debe ser para un número (ej. "Tabla del 1:", "1 x 1 = 1", etc.).
print("\n5. Tablas de multiplicar del 1 al 5:")
for i in range(1, 6):
    print(f"--- Tabla del {i} ---")
    for j in range(1, 6):
        print(f"    {i} x {j} = {i*j}")

# 6. Tupla de Coordenadas y Redefinición:
#    Define una tupla `punto_inicial` con dos coordenadas (ej. (10, 20)).
#    Imprime las coordenadas.
#    Intenta (en un comentario) modificar una coordenada para demostrar la inmutabilidad.
#    Luego, redefine la tupla completa para que `punto_inicial` apunte a nuevas coordenadas (ej. (30, 40)).
#    Imprime las nuevas coordenadas.
punto_inicial = (10, 20)
print(f"6. Punto inicial: {punto_inicial}")
# punto_inicial[0] = 5 # Esto daría un TypeError: 'tuple' object does not support item assignment
punto_inicial = (30, 40)
print(f"   Nuevo punto (tupla redefinida): {punto_inicial}")

# 7. Filtrado de Palabras por Longitud:
#    Dada una lista de palabras, crea una nueva lista que contenga solo las palabras
#    con una longitud mayor a 5 caracteres, usando una comprensión de lista.
#    Imprime ambas listas.
palabras_filtrar = ["casa", "computadora", "sol", "programación", "gato", "elefante"]
palabras_largas = [palabra for palabra in palabras_filtrar if len(palabra) > 5]
print(f"7. Palabras originales: {palabras_filtrar}")
print(f"   Palabras con más de 5 caracteres: {palabras_largas}")

# 8. Generador de Gráficos de Barras Simples (Conceptual):
#    Dada una lista de números enteros (ej. [3, 5, 2, 4]).
#    Usa un bucle `for` para imprimir una "barra" de asteriscos para cada número.
#    Ejemplo:
#    ***
#    *****
#    **
#    ****
datos_barras = [3, 5, 2, 4]
print("\n8. Gráfico de barras simple:")
for valor in datos_barras:
    print("*" * valor)

# 9. Lista de Números Invertidos:
#    Crea una lista de números del 1 al 10.
#    Crea una nueva lista que contenga los mismos números pero en orden inverso,
#    usando una comprensión de lista con `range()`.
numeros_1_a_10 = list(range(1, 11))
numeros_invertidos_comp = [num for num in range(10, 0, -1)]
print(f"9. Números del 1 al 10: {numeros_1_a_10}")
print(f"   Números invertidos (comprensión de lista): {numeros_invertidos_comp}")

# 10. Simulación de una Pila (Stack) con Lista:
#     Crea una lista `pila` vacía.
#     Añade 3 elementos a la pila (simulando `push`).
#     Imprime el elemento superior de la pila (sin eliminarlo).
#     Elimina y imprime los 2 elementos superiores de la pila (simulando `pop`).
#     Imprime la pila final.
pila = []
pila.append("libro A") # Push.
pila.append("libro B")
pila.append("libro C")
print(f"\n10. Pila inicial: {pila}")
print(f"    Elemento superior: {pila[-1]}")
elemento_pop1 = pila.pop() # Pop.
elemento_pop2 = pila.pop()
print(f"    Elementos eliminados: {elemento_pop1}, {elemento_pop2}")
print(f"    Pila final: {pila}")

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 4 ===")
print("="*80 + "\n")

#endregion

#region CAPÍTULO 5: IF STATEMENTS (Declaraciones if)

# ======================================================================================================================
# CAPÍTULO 5: IF STATEMENTS (Declaraciones if)
# ======================================================================================================================
#
# Este capítulo enseña a usar pruebas condicionales para tomar decisiones en el código.
#
# Conceptos clave:
# - Pruebas condicionales: Expresiones que se evalúan como `True` o `False`.
# - Operadores: `==` (igual), `!=` (diferente), `>` (mayor), `<` (menor), `>=` (mayor o igual), `<=` (menor o igual).
# - Lógica booleana: `and` (ambas condiciones deben ser verdaderas) y `or` (al menos una debe ser verdadera).
# - Cadenas condicionales:
#   - `if`: Ejecuta un bloque si la condición es `True`.
#   - `if-else`: Ejecuta un bloque si la condición es `True`, y otro si es `False`.
#   - `if-elif-else`: Permite probar múltiples condiciones en una cadena. Solo se ejecuta el primer bloque que es `True`.
# - Múltiples `if` independientes: Permite que se ejecuten múltiples bloques de código si sus condiciones son verdaderas.
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 5: CONCEPTOS Y EJEMPLOS ===")
print("="*80)

print("--- 5.1 Pruebas condicionales ---")
car = 'bmw'
print(f"¿El coche es 'bmw'? {car == 'bmw'}") # True
print(f"¿El coche es 'audi'? {car == 'audi'}") # False

# Ignorando mayúsculas y minúsculas con `.lower()`.
car_case = 'Audi'
print(f"Comparación ignorando mayúsculas/minúsculas: {car_case.lower() == 'audi'}")

# Operador de desigualdad.
topping = 'mushrooms'
if topping != 'anchovies':
    print("¡No pongas anchoas!")

# Múltiples condiciones con `and` y `or`.
age_0 = 22
age_1 = 18
print(f"Ambos son mayores de 21? {age_0 >= 21 and age_1 >= 21}") # False
print(f"Al menos uno es mayor de 21? {age_0 >= 21 or age_1 >= 21}") # True

# Verificando la pertenencia a una lista con `in` y `not in`.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(f"¿Hay champiñones? {'mushrooms' in requested_toppings}")
print(f"¿No hay pepperoni? {'pepperoni' not in requested_toppings}")


print("\n--- 5.2 if, if-else, if-elif-else ---")
# `if` simple.
age = 19
if age >= 18:
    print("Eres lo suficientemente mayor para votar.")
    print("¿Ya te registraste para votar?")

# `if-else`.
age_vote = 17
if age_vote >= 18:
    print("Puedes votar.")
else:
    print("Lo siento, eres demasiado joven para votar.")

# `if-elif-else`.
age_admission = 12
if age_admission < 4:
    price = 0
elif age_admission < 18:
    price = 25
else:
    price = 40
print(f"El costo de tu entrada es de ${price}.")

# Múltiples `if` independientes.
print("\n--- Múltiples if independientes ---")
requested_toppings_pizza = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings_pizza:
    print("Añadiendo champiñones.")
if 'pepperoni' in requested_toppings_pizza: # Esta condición se comprueba siempre.
    print("Añadiendo pepperoni.")
if 'extra cheese' in requested_toppings_pizza:
    print("Añadiendo extra queso.")
print("¡Pizza lista!")


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 5: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

### Ejercicio 5-1. Conditional Tests
# Escribe 10 pruebas condicionales que se evalúen como True o False.
car_ex_5_1 = 'subaru'
print(f"\n5-1: ¿El coche es 'subaru'? Predigo True. Resultado: {car_ex_5_1 == 'subaru'}")
print(f"¿El coche es 'audi'? Predigo False. Resultado: {car_ex_5_1 == 'audi'}")
# Más ejemplos de tests:
num_test = 10
print(f"¿10 > 5 y 10 < 15? Predigo True. Resultado: {num_test > 5 and num_test < 15}")
fruits_test = ['apple', 'banana']
print(f"¿'banana' está en la lista? Predigo True. Resultado: {'banana' in fruits_test}")
print(f"¿'grape' no está en la lista? Predigo True. Resultado: {'grape' not in fruits_test}")
text_test = "Python"
print(f"¿'python' en minúsculas es igual a 'python'? Predigo True. Resultado: {text_test.lower() == 'python'}")
is_active = False
print(f"¿`is_active` es True? Predigo False. Resultado: {is_active}")


### Ejercicio 5-2. More Conditional Tests
# Más pruebas, incluyendo numéricas y de listas.
print("\n5-2: Más tests condicionales:")
# Strings con .lower()
print(f"String case-insensitive: {'Manzana'.lower() == 'manzana'}")
# Numéricos
number_ex = 25
print(f"Número > 20: {number_ex > 20}")
print(f"Número <= 25: {number_ex <= 25}")
# and/or
age_test_1 = 15; age_test_2 = 20
print(f"15>10 and 20<30: {age_test_1 > 10 and age_test_2 < 30}")
print(f"15>20 or 20<15: {age_test_1 > 20 or age_test_2 < 15}")
# Listas
fruits = ['apple', 'banana', 'orange']
print(f"'banana' está en la lista: {'banana' in fruits}")
print(f"'grape' no está en la lista: {'grape' not in fruits}")

### Ejercicio 5-3. Alien Colors #1
# Simula disparar a un alien y gana puntos.
alien_color_1 = 'green'
if alien_color_1 == 'green':
    print("\n5-3: ¡Acabas de ganar 5 puntos!")
alien_color_1 = 'yellow' # Versión que no pasa el test.
if alien_color_1 == 'green':
    print("5-3: ¡Acabas de ganar 5 puntos! (No se imprimirá nada)")

### Ejercicio 5-4. Alien Colors #2
# Usa una cadena `if-else` para asignar puntos.
alien_color_2 = 'green'
if alien_color_2 == 'green':
    print("\n5-4: Ganaste 5 puntos por disparar al alien.")
else:
    print("5-4: Ganaste 10 puntos.")
alien_color_2 = 'red'
if alien_color_2 == 'green':
    print("5-4: Ganaste 5 puntos por disparar al alien.")
else:
    print("5-4: Ganaste 10 puntos.")

### Ejercicio 5-5. Alien Colors #3
# Usa una cadena `if-elif-else` para asignar diferentes puntos por color.
alien_color_3 = 'yellow'
if alien_color_3 == 'green':
    print("\n5-5: Ganaste 5 puntos.")
elif alien_color_3 == 'yellow':
    print("5-5: Ganaste 10 puntos.")
elif alien_color_3 == 'red':
    print("5-5: Ganaste 15 puntos.")
# Prueba con otros colores para verificar los otros elif:
alien_color_3 = 'green'
if alien_color_3 == 'green':
    print("\n5-5: (Test Green) Ganaste 5 puntos.")
elif alien_color_3 == 'yellow':
    print("5-5: Ganaste 10 puntos.")
elif alien_color_3 == 'red':
    print("5-5: Ganaste 15 puntos.")
alien_color_3 = 'red'
if alien_color_3 == 'green':
    print("\n5-5: (Test Red) Ganaste 5 puntos.")
elif alien_color_3 == 'yellow':
    print("5-5: Ganaste 10 puntos.")
elif alien_color_3 == 'red':
    print("5-5: Ganaste 15 puntos.")


### Ejercicio 5-6. Stages of Life
# Determina la etapa de la vida de una persona según su edad.
age_life = 25
if age_life < 2:
    stage = "un bebé"
elif age_life < 4:
    stage = "un(a) niño(a) pequeño(a)"
elif age_life < 13:
    stage = "un(a) niño(a)"
elif age_life < 20:
    stage = "un(a) adolescente"
elif age_life < 65:
    stage = "un(a) adulto(a)"
else:
    stage = "un(a) anciano(a)"
print(f"\n5-6: La persona es {stage}.")

### Ejercicio 5-7. Favorite Fruit
# Usa una serie de `if` independientes para verificar si una fruta está en una lista.
favorite_fruits = ['apple', 'banana', 'strawberry']
if 'banana' in favorite_fruits:
    print("\n5-7: ¡Realmente te gusta el plátano!")
if 'apple' in favorite_fruits:
    print("5-7: ¡Realmente te gusta la manzana!")
if 'grape' in favorite_fruits: # Esto no se imprimirá.
    print("5-7: ¡Realmente te gusta la uva!")
if 'strawberry' in favorite_fruits:
    print("5-7: ¡Realmente te gusta la fresa!")

### Ejercicio 5-8. Hello Admin
# Saluda a los usuarios, dando un saludo especial al administrador.
usernames_ex = ['admin', 'jaden', 'alice', 'bob']
for user_ex in usernames_ex:
    if user_ex == 'admin':
        print("\n5-8: Hello admin, ¿te gustaría ver un informe de estado?")
    else:
        print(f"5-8: Hello {user_ex.title()}, gracias por iniciar sesión de nuevo.")

### Ejercicio 5-9. No Users
# Verifica si la lista de usuarios está vacía antes de iterar.
usernames_empty = []
if usernames_empty:
    for user_ex in usernames_empty:
        print(f"Hello {user_ex.title()}.")
else:
    print("\n5-9: ¡Necesitamos encontrar algunos usuarios!")

### Ejercicio 5-10. Checking Usernames
# Simula la verificación de nombres de usuario únicos, ignorando el caso.
current_users = ['john', 'maria', 'peter', 'sarah', 'admin']
new_users = ['john', 'MARIA', 'jessica', 'luis', 'ana']
current_users_lower = [user.lower() for user in current_users]
print("\n5-10: Verificando nuevos usuarios:")
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"El nombre de usuario '{new_user}' ya ha sido usado. Por favor, elige uno nuevo.")
    else:
        print(f"El nombre de usuario '{new_user}' está disponible.")

### Ejercicio 5-11. Ordinal Numbers
# Imprime los números ordinales correctamente (1st, 2nd, 3rd, etc.).
numbers_ordinal = list(range(1, 10))
print("\n5-11: Números ordinales:")
for num_ord in numbers_ordinal:
    if num_ord == 1:
        suffix = "st"
    elif num_ord == 2:
        suffix = "nd"
    elif num_ord == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{num_ord}{suffix}")

### Ejercicio 5-12. Styling if Statements
# Revisa tus programas para asegurarte de que sigues la guía de estilo para las declaraciones `if`.
print("\n5-12: Revisa tu código y asegúrate de que tiene un espaciado adecuado alrededor de los operadores.")

### Ejercicio 5-13. Your Ideas
# Piensa en nuevas ideas de programas y regístralas.
print("\n5-13: Este es un buen momento para registrar ideas de proyectos. ¡Sigue pensando!")

# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 5 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 5 ===")
print("="*80)

# 1. Sistema de Calificaciones (Letras):
#    Dada una puntuación numérica (0-100), asigna una calificación en letra usando `if-elif-else`:
#    - 90-100: A
#    - 80-89: B
#    - 70-79: C
#    - 60-69: D
#    - Menos de 60: F
#    Prueba con varias puntuaciones.
puntuacion = 85
if puntuacion >= 90:
    calificacion = 'A'
elif puntuacion >= 80:
    calificacion = 'B'
elif puntuacion >= 70:
    calificacion = 'C'
elif puntuacion >= 60:
    calificacion = 'D'
else:
    calificacion = 'F'
print(f"1. Puntuación: {puntuacion}, Calificación: {calificacion}")

# 2. Descuento por Edad y Tipo de Cliente:
#    Calcula el precio de una entrada basada en `edad` y `tipo_cliente` ("regular", "vip").
#    - Menos de 5 años: Gratis.
#    - 5 a 17 años: $10 (regular), $8 (vip).
#    - 18 a 64 años: $20 (regular), $15 (vip).
#    - 65 o más: $12 (regular), $10 (vip).
#    Prueba varias combinaciones.
edad_cliente = 30
tipo_cliente = "vip"
precio_entrada = 0

if edad_cliente < 5:
    precio_entrada = 0
elif edad_cliente >= 5 and edad_cliente <= 17:
    if tipo_cliente == "vip":
        precio_entrada = 8
    else:
        precio_entrada = 10
elif edad_cliente >= 18 and edad_cliente <= 64:
    if tipo_cliente == "vip":
        precio_entrada = 15
    else:
        precio_entrada = 20
else: # edad_cliente >= 65
    if tipo_cliente == "vip":
        precio_entrada = 10
    else:
        precio_entrada = 12
print(f"2. Edad: {edad_cliente}, Tipo: {tipo_cliente}, Precio de entrada: ${precio_entrada}")

# 3. Verificador de Año Bisiesto:
#    Dado un `año` (número entero), determina si es un año bisiesto.
#    Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
#    Imprime si el año es bisiesto o no.
anio = 2024
es_bisiesto = False
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    es_bisiesto = True
if es_bisiesto:
    print(f"3. El año {anio} es bisiesto.")
else:
    print(f"3. El año {anio} no es bisiesto.")

# 4. Verificador de Contraseña Simple:
#    Crea una variable `contrasena_guardada` y `contrasena_ingresada`.
#    Verifica:
#    - Si `contrasena_ingresada` coincide con `contrasena_guardada` (case-sensitive).
#      Si no coincide, imprime "Contraseña incorrecta."
#    - Si la contraseña es correcta, imprime "Acceso concedido."
#    - Si `contrasena_ingresada` es "admin" (ignoring case), imprime "Acceso de administrador.".
contrasena_guardada = "MiPass123"
contrasena_ingresada = "mipass123"
if contrasena_ingresada == contrasena_guardada:
    print("4. Acceso concedido.")
elif contrasena_ingresada.lower() == "admin":
    print("4. Acceso de administrador.")
else:
    print("4. Contraseña incorrecta.")

# 5. Clasificador de Números:
#    Dado un `numero`, clasifícalo como:
#    - "Positivo y par"
#    - "Positivo e impar"
#    - "Negativo y par"
#    - "Negativo e impar"
#    - "Cero"
numero_clasificar = -7
if numero_clasificar == 0:
    print(f"5. El número {numero_clasificar} es Cero.")
elif numero_clasificar > 0:
    if numero_clasificar % 2 == 0:
        print(f"5. El número {numero_clasificar} es Positivo y par.")
    else:
        print(f"5. El número {numero_clasificar} es Positivo e impar.")
else: # numero_clasificar < 0
    if numero_clasificar % 2 == 0:
        print(f"5. El número {numero_clasificar} es Negativo y par.")
    else:
        print(f"5. El número {numero_clasificar} es Negativo e impar.")

# 6. Juego de Piedra, Papel o Tijera (Un Turno):
#    Simula un turno del juego. Crea dos variables: `jugador1` y `jugador2` (con valores "piedra", "papel", "tijera").
#    Determina el ganador o si es un empate.
jugador1 = "piedra"
jugador2 = "papel"
print(f"6. Jugador 1: {jugador1}, Jugador 2: {jugador2}")
if jugador1 == jugador2:
    print("   ¡Es un empate!")
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
     (jugador1 == "papel" and jugador2 == "piedra") or \
     (jugador1 == "tijera" and jugador2 == "papel"):
    print("   ¡Jugador 1 gana!")
else:
    print("   ¡Jugador 2 gana!")

# 7. Verificador de Disponibilidad de Productos:
#    Dada una lista de `productos_disponibles` y una lista de `productos_solicitados`.
#    Itera sobre `productos_solicitados`. Para cada producto, imprime si está disponible o no.
productos_disponibles = ["manzana", "banana", "leche", "pan"]
productos_solicitados = ["manzana", "agua", "leche", "queso"]
print("\n7. Verificador de disponibilidad:")
for producto in productos_solicitados:
    if producto in productos_disponibles:
        print(f"   '{producto.title()}' está disponible.")
    else:
        print(f"   Lo siento, '{producto.title()}' no está disponible.")

# 8. Decisor de Estado de Temperatura:
#    Dada una `temperatura` (int o float), clasifica el ambiente:
#    - Menos de 0: "Congelando"
#    - 0 a 10: "Muy frío"
#    - 11 a 20: "Frío"
#    - 21 a 30: "Templado"
#    - Más de 30: "Caluroso"
temperatura = 22.5
if temperatura < 0:
    estado = "Congelando"
elif temperatura <= 10:
    estado = "Muy frío"
elif temperatura <= 20:
    estado = "Frío"
elif temperatura <= 30:
    estado = "Templado"
else:
    estado = "Caluroso"
print(f"8. La temperatura es {temperatura}°C. El ambiente está: {estado}.")

# 9. Verificador de Contenido Sensible (Palabra Clave):
#    Dada una `frase` y una lista de `palabras_prohibidas`.
#    Verifica si alguna palabra prohibida está en la frase (ignorando mayúsculas y minúsculas).
#    Si se encuentra alguna, imprime "Contenido no permitido."
#    De lo contrario, imprime "Contenido seguro."
frase_analizar_2 = "Este es un comentario con una palabra mala."
palabras_prohibidas = ["mala", "ofensivo", "ilegal"]
es_seguro = True
for palabra_prohibida in palabras_prohibidas:
    if palabra_prohibida in frase_analizar_2.lower():
        es_seguro = False
        break # Detiene el bucle si encuentra una palabra prohibida.
if es_seguro:
    print("9. Contenido seguro.")
else:
    print("9. Contenido no permitido.")

# 10. Calculadora de Envío:
#     Calcula el costo de envío basado en el `peso_kg` del paquete y la `distancia_km`.
#     - Costo base: $5.
#     - Por cada kg adicional (más allá del primero): $2.
#     - Por cada 100 km adicionales (más allá de los primeros 100 km): $3.
#     - Si el peso es 0 o menos, o la distancia es 0 o menos, imprime un mensaje de error.
peso_kg = 3.5
distancia_km = 250
costo_envio = 0
if peso_kg <= 0 or distancia_km <= 0:
    print("10. Error: El peso y la distancia deben ser mayores que cero.")
else:
    costo_envio = 5 # Costo base.
    if peso_kg > 1:
        costo_envio += (peso_kg - 1) * 2
    if distancia_km > 100:
        costo_envio += ((distancia_km - 100) // 100) * 3
    print(f"10. El costo de envío para {peso_kg}kg y {distancia_km}km es: ${costo_envio:.2f}")

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 5 ===")
print("="*80 + "\n")

#endregion

#region CAPÍTULO 6: DICCIONARIOS

# ======================================================================================================================
# CAPÍTULO 6: DICCIONARIOS
# ======================================================================================================================
#
# Este capítulo introduce los diccionarios, que almacenan colecciones de pares clave-valor.
#
# Conceptos clave:
# - Diccionario: Una colección no ordenada de pares clave-valor encerrada en `{}`.
# - Acceso y modificación: Usa la clave entre corchetes para acceder o asignar un valor.
# - `del`: Elimina un par clave-valor.
# - `get()`: Accede a un valor de forma segura, devolviendo un valor por defecto si la clave no existe.
# - Iterar:
#   - `items()`: Para bucles sobre pares clave-valor.
#   - `keys()`: Para bucles sobre las claves.
#   - `values()`: Para bucles sobre los valores.
# - Anidamiento (`Nesting`): Almacenar una colección dentro de otra (ej. una lista en un diccionario).
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 6: CONCEPTOS Y EJEMPLOS ===")
print("="*80)

print("--- 6.1 Un diccionario simple ---")
alien_0 = {'color': 'green', 'points': 5}
print(f"El color del alien es: {alien_0['color']}")
print(f"Los puntos del alien son: {alien_0['points']}")

print("\n--- 6.2 Añadiendo, modificando y eliminando ---")
# Añadir nuevos pares.
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f"Diccionario modificado: {alien_0}")
# Modificar un valor.
alien_0['color'] = 'yellow'
print(f"Color modificado: {alien_0['color']}")
# Eliminar un par.
del alien_0['points']
print(f"Después de eliminar 'points': {alien_0}")

print("\n--- 6.3 Usando get() para acceder de forma segura ---")
alien_0_no_points = {'color': 'green'}
# Si la clave no existe, devuelve el valor por defecto ('No point value assigned.').
points = alien_0_no_points.get('points', 'No point value assigned.')
print(points)

print("\n--- 6.4 Bucle a través de un diccionario ---")
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}
# Iterando sobre pares clave-valor con `.items()`.
print("\nIterando sobre pares clave-valor:")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
# Iterando solo sobre las claves con `.keys()`.
print("\nIterando solo sobre las claves:")
for name in favorite_languages.keys():
    print(name.title())
# Iterando solo sobre los valores con `.values()`.
print("\nIterando solo sobre los valores:")
for language in favorite_languages.values():
    print(language.title())
# Valores únicos usando `set()`.
print("\nValores únicos con set():")
for language in set(favorite_languages.values()):
    print(language.title())


print("\n--- 6.5 Anidamiento (Nesting) ---")
# Una lista de diccionarios.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
aliens = [alien_0, alien_1]
print("Lista de aliens:")
for alien in aliens:
    print(alien)

# Una lista en un diccionario.
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
print(f"\nOrdenaste una pizza con masa {pizza['crust']} y los siguientes ingredientes:")
for topping in pizza['toppings']:
    print(f"\t- {topping}")

# Un diccionario en un diccionario.
users = {'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'},
         'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris'}}
print("\nInformación de usuarios:")
for username, user_info in users.items():
    print(f"Username: {username}")
    print(f"\tNombre completo: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"\tUbicación: {user_info['location'].title()}")


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 6: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

### Ejercicio 6-1. Person
# Almacena información sobre una persona en un diccionario y imprímela.
person = {'first_name': 'john', 'last_name': 'doe', 'age': 30, 'city': 'new york'}
print("\n6-1: Información de la persona:")
for key, value in person.items():
    print(f"\t{key.title()}: {value}")

### Ejercicio 6-2. Favorite Numbers
# Crea un diccionario con nombres y números favoritos.
favorite_numbers = {'jen': 7, 'sarah': 42, 'edward': 5, 'phil': 7, 'maria': 13}
print("\n6-2: Números favoritos:")
for name, number in favorite_numbers.items():
    print(f"El número favorito de {name.title()} es {number}.")

### Ejercicio 6-3. Glossary
# Crea un glosario de términos de programación en un diccionario.
glossary = {'variable': 'A label connected to a value.',
            'string': 'A series of characters.',
            'list': 'A collection of items in a particular order.',
            'for loop': 'To run through all entries in a list.',
            'integer': 'A whole number.'}
print("\n6-3: Glosario de términos:")
for word, meaning in glossary.items():
    print(f"\n{word.title()}:\n\t{meaning}")

### Ejercicio 6-4. Glossary 2
# Añade más términos al glosario y usa un bucle para imprimirlo.
glossary['float'] = 'A number with a decimal point.'
glossary['dictionary'] = 'A collection of key-value pairs.'
print("\n6-4: Glosario actualizado:")
for word, meaning in glossary.items():
    print(f"\n{word.title()}:\n\t{meaning}")

### Ejercicio 6-5. Rivers
# Diccionario de ríos y países.
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}
print("\n6-5: Oraciones sobre ríos:")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("\n6-5: Ríos:")
for river in rivers.keys():
    print(river.title())
print("\n6-5: Países:")
for country in rivers.values():
    print(country.title())

### Ejercicio 6-6. Polling
# Verifica quién ha participado en una encuesta y quién no.
poll_takers = ['jen', 'sarah', 'maria', 'peter']
print("\n6-6: Sondeo de personas:")
for person in poll_takers:
    if person in favorite_languages.keys():
        print(f"Gracias, {person.title()}, por haber respondido a la encuesta.")
    else:
        print(f"{person.title()}, por favor, ¡participa en la encuesta!")

### Ejercicio 6-7. People
# Crea una lista de diccionarios de personas.
person1 = {'first_name': 'john', 'last_name': 'doe', 'age': 30, 'city': 'new york'}
person2 = {'first_name': 'jane', 'last_name': 'smith', 'age': 25, 'city': 'london'}
person3 = {'first_name': 'peter', 'last_name': 'jones', 'age': 40, 'city': 'paris'}
people_list = [person1, person2, person3]
print("\n6-7: Información de las personas:")
for person_info in people_list:
    print("\n--- Nueva persona ---")
    for key, value in person_info.items():
        print(f"\t{key.title()}: {value}")

### Ejercicio 6-8. Pets
# Crea una lista de diccionarios de mascotas.
pet1 = {'animal': 'dog', 'owner': 'john'}
pet2 = {'animal': 'cat', 'owner': 'maria'}
pets_list = [pet1, pet2]
print("\n6-8: Información de las mascotas:")
for pet_info in pets_list:
    print(f"\n- Animal: {pet_info['animal'].title()}, Propietario: {pet_info['owner'].title()}")

### Ejercicio 6-9. Favorite Places
# Crea un diccionario con listas anidadas para lugares favoritos.
favorite_places = {'john': ['paris', 'tokyo'], 'sara': ['london'], 'peter': ['new york', 'rome']}
print("\n6-9: Lugares favoritos:")
for name, places in favorite_places.items():
    print(f"\nLos lugares favoritos de {name.title()} son:")
    for place in places:
        print(f"\t- {place.title()}")

### Ejercicio 6-10. Favorite Numbers (multiple)
# Modifica el ejercicio 6-2 para almacenar múltiples números favoritos por persona.
favorite_numbers_multi = {'jen': [7, 12], 'sarah': [42], 'edward': [5, 10], 'phil': [7], 'maria': [13, 26]}
print("\n6-10: Números favoritos (múltiples):")
for name, numbers in favorite_numbers_multi.items():
    print(f"\nLos números favoritos de {name.title()} son:")
    for number in numbers:
        print(f"\t{number}")

### Ejercicio 6-11. Cities
# Crea un diccionario de diccionarios para almacenar información de ciudades.
cities = {'new york': {'country': 'usa', 'population': 8_400_000, 'fact': 'It is called the Big Apple.'},
          'paris': {'country': 'france', 'population': 2_100_000, 'fact': 'It is known as the City of Love.'}}
print("\n6-11: Información de las ciudades:")
for city, city_info in cities.items():
    print(f"\nCiudad: {city.title()}")
    for key, value in city_info.items():
        print(f"\t- {key.title()}: {value}")

### Ejercicio 6-12. Extensions
# Extiende uno de los programas anteriores con nuevas características.
print("\n6-12: Este ejercicio requiere extender uno de los programas anteriores. ¡Sé creativo y añade nuevas claves o lógicas!")

# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 6 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 6 ===")
print("="*80)

# 1. Registro de Inventario Simple:
#    Crea un diccionario `inventario` donde las claves son nombres de productos (strings)
#    y los valores son listas que contienen [cantidad, precio_unitario].
#    a) Agrega al menos 3 productos.
#    b) Modifica la cantidad de un producto existente.
#    c) Elimina un producto del inventario.
#    d) Itera y muestra cada producto, su cantidad y precio unitario.
inventario = {
    "manzanas": [50, 0.75],
    "bananas": [30, 0.50],
    "naranjas": [40, 1.20]
}
print(f"1a. Inventario inicial: {inventario}")
inventario["manzanas"][0] = 60 # Modificar cantidad.
print(f"1b. Manzanas modificadas: {inventario}")
del inventario["naranjas"]
print(f"1c. Naranjas eliminadas: {inventario}")
print("1d. Inventario actual:")
for producto, datos in inventario.items():
    print(f"   - {producto.title()}: Cantidad={datos[0]}, Precio=${datos[1]:.2f}")

# 2. Libro de Calificaciones Estudiantil:
#    Crea un diccionario `calificaciones_estudiantes` donde las claves son nombres de estudiantes (strings)
#    y los valores son diccionarios con asignaturas y sus calificaciones (ej. {"Matematicas": 95, "Ciencias": 88}).
#    a) Agrega al menos 2 estudiantes con 2-3 asignaturas cada uno.
#    b) Agrega una nueva asignatura y calificación para un estudiante existente.
#    c) Imprime las calificaciones de cada estudiante, asignatura por asignatura.
calificaciones_estudiantes = {
    "Ana": {"Matematicas": 90, "Historia": 85},
    "Pedro": {"Matematicas": 78, "Ciencias": 92, "Literatura": 80}
}
print(f"\n2a. Calificaciones iniciales: {calificaciones_estudiantes}")
calificaciones_estudiantes["Ana"]["Arte"] = 95
print(f"2b. Calificaciones de Ana actualizadas: {calificaciones_estudiantes['Ana']}")
print("2c. Calificaciones por estudiante:")
for estudiante, asignaturas in calificaciones_estudiantes.items():
    print(f"   {estudiante.title()}:")
    for asignatura, calificacion in asignaturas.items():
        print(f"     - {asignatura}: {calificacion}")

# 3. Contador de Palabras en una Frase:
#    Dada una frase (string), crea un diccionario donde las claves son las palabras
#    (en minúsculas) y los valores son la cantidad de veces que aparecen.
#    a) Ignora mayúsculas/minúsculas.
#    b) Imprime el diccionario resultante.
frase_larga = "Python es un lenguaje muy versátil. Python es fácil de aprender."
palabras_frase = frase_larga.lower().replace('.', '').split()
contador_palabras = {}
for palabra in palabras_frase:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print(f"\n3. Conteo de palabras: {contador_palabras}")

# 4. Libro de Contactos Básico:
#    Crea un diccionario `contactos` donde las claves son nombres de personas (strings)
#    y los valores son diccionarios con "telefono" y "email".
#    a) Agrega 2-3 contactos.
#    b) Accede e imprime el email de un contacto específico.
#    c) Añade un nuevo campo (ej. "direccion") a un contacto existente.
#    d) Itera y muestra el nombre y teléfono de todos los contactos.
contactos = {
    "Juan Perez": {"telefono": "555-1234", "email": "juan@ejemplo.com"},
    "Maria Lopez": {"telefono": "555-5678", "email": "maria@ejemplo.com"}
}
print(f"\n4a. Contactos: {contactos}")
print(f"4b. Email de Juan: {contactos['Juan Perez']['email']}")
contactos["Juan Perez"]["direccion"] = "Calle Falsa 123"
print(f"4c. Juan con dirección: {contactos['Juan Perez']}")
print("4d. Nombres y teléfonos:")
for nombre, info in contactos.items():
    print(f"   - {nombre}: {info['telefono']}")

# 5. Menú de Restaurante por Categoría:
#    Crea un diccionario `menu_restaurante` donde las claves son categorías (ej. "Entradas", "Platos Fuertes")
#    y los valores son listas de ítems de menú (strings).
#    a) Agrega al menos 2 categorías con varios ítems.
#    b) Imprime el menú completo, categoría por categoría.
#    c) Agrega un nuevo ítem a una categoría existente.
menu_restaurante = {
    "Entradas": ["Sopa de tomate", "Ensalada César", "Nachos"],
    "Platos Fuertes": ["Filete con papas", "Pasta Alfredo", "Salmón al horno"]
}
print(f"\n5a. Menú del restaurante: {menu_restaurante}")
print("5b. Imprimiendo menú:")
for categoria, items in menu_restaurante.items():
    print(f"   --- {categoria.upper()} ---")
    for item in items:
        print(f"     - {item}")
menu_restaurante["Entradas"].append("Aros de cebolla")
print(f"5c. Entradas actualizadas: {menu_restaurante['Entradas']}")

# 6. Registro de Votos:
#    Crea un diccionario `votos` donde las claves son candidatos (strings) y los valores son el conteo de votos (números).
#    a) Inicializa con 3 candidatos y 0 votos.
#    b) Simula 5 votos aleatorios (incrementa el conteo de votos para un candidato elegido aleatoriamente).
#    c) Imprime el resultado de la votación, ordenado por el nombre del candidato.
#    (No usar `random` todavía, simula eligiendo con `if/elif/else` o simplemente modificando).
votos = {"Candidato A": 0, "Candidato B": 0, "Candidato C": 0}
print(f"\n6a. Votos iniciales: {votos}")
# Simulación de 5 votos.
votos["Candidato A"] += 1
votos["Candidato B"] += 1
votos["Candidato A"] += 1
votos["Candidato C"] += 1
votos["Candidato B"] += 1
print(f"6b. Votos después de simulación: {votos}")
print("6c. Resultado de la votación (ordenado por candidato):")
for candidato in sorted(votos.keys()):
    print(f"   - {candidato}: {votos[candidato]} votos")

# 7. Información de Usuario Anidada:
#    Crea una lista `usuarios_web` donde cada elemento es un diccionario que representa a un usuario,
#    con campos como "username", "email" y "roles" (lista de strings).
#    a) Agrega 2 usuarios, uno con 1 rol y otro con 2 roles.
#    b) Itera sobre la lista y para cada usuario, imprime su username y sus roles.
usuarios_web = [
    {"username": "admin1", "email": "admin@web.com", "roles": ["administrador"]},
    {"username": "user1", "email": "user@web.com", "roles": ["editor", "revisor"]}
]
print(f"\n7a. Usuarios web: {usuarios_web}")
print("7b. Roles de usuario:")
for user in usuarios_web:
    print(f"   - {user['username']}: Roles -> {', '.join(user['roles'])}")

# 8. Diccionario de Capitales:
#    Crea un diccionario `capitales_del_mundo` con al menos 3 países y sus capitales.
#    a) Imprime la capital de un país específico usando `get()` para manejar países no presentes.
#    b) Agrega un nuevo país y su capital.
#    c) Elimina un país.
#    d) Itera y muestra todos los países (ordenados) y sus capitales.
capitales_del_mundo = {
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín"
}
print(f"\n8a. Capital de España: {capitales_del_mundo.get('España')}")
print(f"   Capital de Italia (no existe): {capitales_del_mundo.get('Italia', 'No encontrada')}")
capitales_del_mundo["Italia"] = "Roma"
print(f"8b. Italia añadida: {capitales_del_mundo}")
del capitales_del_mundo["Alemania"]
print(f"8c. Alemania eliminada: {capitales_del_mundo}")
print("8d. Todas las capitales (ordenadas por país):")
for pais in sorted(capitales_del_mundo.keys()):
    print(f"   - {pais}: {capitales_del_mundo[pais]}")

# 9. Conteo de Géneros Musicales (Lista de Strings):
#    Dada una lista de géneros musicales, cuenta cuántas veces aparece cada género
#    y almacena el conteo en un diccionario.
#    Ejemplo: ["rock", "pop", "rock", "jazz"] -> {"rock": 2, "pop": 1, "jazz": 1}
generos_musicales = ["rock", "pop", "rock", "jazz", "metal", "pop", "rock"]
conteo_generos = {}
for genero in generos_musicales:
    conteo_generos[genero] = conteo_generos.get(genero, 0) + 1
print(f"\n9. Conteo de géneros musicales: {conteo_generos}")

# 10. Gestión de Configuración (Simulada):
#     Crea un diccionario `configuracion_app` con claves como "tema" (string),
#     "notificaciones_activas" (booleano) y "idioma" (string).
#     a) Imprime el valor de "notificaciones_activas".
#     b) Cambia el "tema".
#     c) Agrega una nueva configuración (ej. "autoguardado": True).
#     d) Imprime todas las configuraciones con sus tipos de valor.
configuracion_app = {
    "tema": "oscuro",
    "notificaciones_activas": True,
    "idioma": "es"
}
print(f"\n10a. Notificaciones activas: {configuracion_app['notificaciones_activas']}")
configuracion_app["tema"] = "claro"
print(f"10b. Tema modificado: {configuracion_app['tema']}")
configuracion_app["autoguardado"] = True
print(f"10c. Configuración añadida: {configuracion_app}")
print("10d. Todas las configuraciones y sus tipos:")
for key, value in configuracion_app.items():
    print(f"   - {key}: {value} (Tipo: {type(value)})")

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 6 ===")
print("="*80 + "\n")

#endregion

#region CAPÍTULO 7: ENTRADA DEL USUARIO Y BUCLES WHILE

# ======================================================================================================================
# CAPÍTULO 7: ENTRADA DEL USUARIO Y BUCLES WHILE
# ======================================================================================================================
#
# Este capítulo enseña a obtener información del usuario y a controlar la ejecución del programa con bucles `while`.
#
# Conceptos clave:
# - `input()`: Pausa el programa y espera a que el usuario ingrese texto. Siempre devuelve un `string`.
# - `int()`: Convierte un `string` a un `int` para realizar cálculos numéricos.
# - Bucle `while`: Se ejecuta mientras una condición sea `True`.
# - Controlando un bucle:
#   - `active` (flag): Una variable booleana para controlar si el bucle debe continuar.
#   - `break`: Salida inmediata del bucle.
#   - `continue`: Omite el resto del bucle y vuelve al principio de la siguiente iteración.
# - Bucle infinito: Un bucle que nunca se detiene. Siempre debe tener una condición de salida.
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 7: CONCEPTOS Y EJEMPLOS ===")
print("="*80)

print("--- 7.1 La función input() ---")
# Nota: Los prompts de `input()` pueden no funcionar en algunos editores.
# Ejecuta este script desde una terminal para interactuar.
#
# message_input = input("Dime algo, y lo repetiré: ")
# print(message_input)

# Usando `int()` para entrada numérica.
# age_input = input("¿Cuántos años tienes? ")
# age_input = int(age_input)
# if age_input >= 18:
#     print("Eres mayor de edad.")


print("\n--- 7.2 Bucle while ---")
# Un bucle simple que cuenta hasta 5.
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 # Condición de salida.

print("\n--- 7.3 Controlando el bucle con `break`, `continue` y flags ---")
# Bucle que se ejecuta hasta que el usuario ingresa 'quit'.
# prompt_quit = "\nDime algo, o escribe 'quit' para terminar: "
# while True: # Bucle infinito con salida controlada por `break`.
#     city_input = input(prompt_quit)
#     if city_input == 'quit':
#         break
#     else:
#         print(f"Me encantaría ir a {city_input.title()}!")

# Uso de `continue`.
print("Números impares del 1 al 10:")
current_number_cont = 0
while current_number_cont < 10:
    current_number_cont += 1
    if current_number_cont % 2 == 0:
        continue # Si el número es par, se salta la impresión y vuelve al inicio.
    print(current_number_cont)

# Uso de `while` con listas para mover elementos.
print("\n--- 7.4 Movimiento de elementos entre listas ---")
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop() # Saca el último elemento de la lista.
    print(f"Verificando usuario: {current_user.title()}")
    confirmed_users.append(current_user) # Añade a la nueva lista.
print(f"\nUsuarios confirmados: {confirmed_users}")


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 7: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

# Nota: Los ejercicios con `input()` requieren interacción del usuario.
# Ejecuta cada uno por separado para probarlos.

### Ejercicio 7-1. Rental Car
# Pregunta al usuario por un coche de alquiler.
# car_choice = input("\n7-1: ¿Qué tipo de coche de alquiler te gustaría? ")
# print(f"7-1: Déjame ver si puedo encontrar un {car_choice.title()}.")

### Ejercicio 7-2. Restaurant Seating
# Pregunta el tamaño de un grupo para cenar.
# num_people = input("\n7-2: ¿Cuántas personas hay en tu grupo para cenar? ")
# num_people = int(num_people)
# if num_people > 8:
#     print("7-2: Tendrán que esperar por una mesa.")
# else:
#     print("7-2: Tu mesa está lista.")

### Ejercicio 7-3. Multiples of Ten
# Verifica si un número es múltiplo de 10.
# number_multiple = input("\n7-3: Ingresa un número: ")
# number_multiple = int(number_multiple)
# if number_multiple % 10 == 0:
#     print(f"7-3: El número {number_multiple} es un múltiplo de 10.")
# else:
#     print(f"7-3: El número {number_multiple} no es un múltiplo de 10.")

### Ejercicio 7-4. Pizza Toppings
# Pide al usuario ingredientes de pizza hasta que escriba 'quit'.
# prompt_pizza = "\n7-4: Ingresa un ingrediente para tu pizza (escribe 'quit' para terminar): "
# while True:
#     topping_pizza = input(prompt_pizza)
#     if topping_pizza.lower() == 'quit':
#         break
#     print(f"7-4: ¡Añadiré {topping_pizza} a tu pizza!")

### Ejercicio 7-5. Movie Tickets
# Calcula el precio de un boleto de cine según la edad.
# prompt_age = "\n7-5: ¿Cuál es tu edad? (escribe 'quit' para terminar): "
# while True:
#     age_ticket = input(prompt_age)
#     if age_ticket.lower() == 'quit':
#         break
#     age_ticket = int(age_ticket)
#     if age_ticket < 3:
#         price_ticket = "gratis"
#     elif age_ticket <= 12:
#         price_ticket = "$10"
#     else:
#         price_ticket = "$15"
#     print(f"7-5: El costo de tu boleto es de {price_ticket}.")

### Ejercicio 7-6. Three Exits
# Revisa el ejercicio anterior y aplica diferentes formas de salir del bucle.
print("\n7-6: Este ejercicio requiere que apliques flags, `break` o condiciones de bucle. Revisa los ejemplos del capítulo para practicar.")

### Ejercicio 7-7. Infinity
# Crea un bucle que nunca termine (comentado para evitar que se ejecute).
print("\n7-7: El siguiente código es un bucle infinito, comentado para que no se ejecute.")
# x = 1
# while x <= 5:
#    print(x) # Faltaría `x += 1` para que el bucle termine.

### Ejercicio 7-8. Deli
# Mueve elementos de una lista de pedidos a una lista de sándwiches terminados.
sandwich_orders = ['atún', 'pavo', 'jamón y queso']
finished_sandwiches = []
print("\n7-8: Procesando órdenes de sándwiches:")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) # pop(0) elimina desde el principio.
    print(f"7-8: Preparando tu sándwich de {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
print("\n7-8: Sándwiches preparados:")
for sandwich in finished_sandwiches:
    print(f" - {sandwich.title()}")

### Ejercicio 7-9. No Pastrami
# Elimina todas las ocurrencias de un valor de una lista.
sandwich_orders_2 = ['pastrami', 'atún', 'pastrami', 'pavo', 'pastrami']
print("\n7-9: ¡La charcutería se ha quedado sin pastrami!")
while 'pastrami' in sandwich_orders_2:
    sandwich_orders_2.remove('pastrami')
print("7-9: Todas las órdenes de pastrami han sido eliminadas.")
print(f"7-9: Órdenes restantes: {sandwich_orders_2}")

### Ejercicio 7-10. Dream Vacation
# Realiza una encuesta a los usuarios sobre su lugar de vacaciones soñado.
# dream_vacation_poll = {}
# active_poll = True
# while active_poll:
#     name_poll = input("\n7-10: ¿Cuál es tu nombre? ")
#     place_poll = input("7-10: Si pudieras visitar un lugar en el mundo, ¿a dónde irías? ")
#     dream_vacation_poll[name_poll] = place_poll
#     repeat = input("7-10: ¿Le gustaría a otra persona responder? (si/no) ")
#     if repeat.lower() == 'no':
#         active_poll = False
# print("\n--- 7-10: Resultados de la encuesta ---")
# for name, place in dream_vacation_poll.items():
#     print(f"7-10: {name.title()} le gustaría visitar {place.title()}.")

# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 7 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 7 ===")
print("="*80)

# 1. Simulación de Chatbot Simple:
#    Crea un chatbot que salude al usuario y luego repita lo que el usuario escribe,
#    hasta que el usuario escriba "salir" o "bye" (sin distinguir mayúsculas/minúsculas).
#    Usa un bucle `while` y una variable `flag`.
print("\n1. Chatbot Simple:")
# chatbot_active = True
# while chatbot_active:
#     user_input = input("Chatbot: Hola. ¿Cómo puedo ayudarte? (Escribe 'salir' o 'bye' para terminar) ")
#     if user_input.lower() == 'salir' or user_input.lower() == 'bye':
#         chatbot_active = False
#         print("Chatbot: ¡Adiós!")
#     else:
#         print(f"Chatbot: Dijiste: '{user_input}'")

# 2. Constructor de Pizza Interactivo:
#    Pide al usuario que ingrese ingredientes para una pizza, uno por uno.
#    Almacena los ingredientes en una lista.
#    Cuando el usuario ingrese "listo", detén la entrada y muestra un resumen de la pizza.
print("\n2. Constructor de Pizza Interactivo:")
# pizza_toppings_list = []
# print("Ingresa los ingredientes de tu pizza (escribe 'listo' cuando hayas terminado):")
# while True:
#     topping = input("Ingrediente: ")
#     if topping.lower() == 'listo':
#         break
#     else:
#         pizza_toppings_list.append(topping)
# print("\nTu pizza tendrá los siguientes ingredientes:")
# if pizza_toppings_list:
#     for t in pizza_toppings_list:
#         print(f"- {t.title()}")
# else:
#     print("- ¡Una pizza sencilla sin ingredientes!")

# 3. Juego de Adivinar el Número (Mejorado):
#    El programa piensa en un número fijo (ej. 7).
#    Pide al usuario que adivine el número.
#    Da pistas: "Demasiado alto" o "Demasiado bajo".
#    Continúa hasta que el usuario adivine correctamente.
#    Usa `int()` para convertir la entrada.
print("\n3. Juego de Adivinar el Número:")
# secret_number = 7
# print("Estoy pensando en un número entre 1 y 10. ¡Intenta adivinarlo!")
# while True:
#     guess_str = input("Tu suposición: ")
#     try:
#         guess = int(guess_str)
#         if guess == secret_number:
#             print("¡Correcto! ¡Adivinaste el número!")
#             break
#         elif guess < secret_number:
#             print("Demasiado bajo. Intenta de nuevo.")
#         else:
#             print("Demasiado alto. Intenta de nuevo.")
#     except ValueError:
#         print("Entrada inválida. Por favor, ingresa un número.")

# 4. Constructor de Lista de Usuarios:
#    Pide al usuario que ingrese nombres de usuario, uno por uno.
#    Almacena los nombres en una lista.
#    Cuando el usuario ingrese una cadena vacía (solo presione Enter), detén la entrada.
#    Imprime la lista final de usuarios.
print("\n4. Constructor de Lista de Usuarios:")
# user_names_collected = []
# print("Ingresa nombres de usuario (presiona Enter sin escribir para terminar):")
# while True:
#     name_input_chall = input("Nombre de usuario: ")
#     if name_input_chall == '':
#         break
#     else:
#         user_names_collected.append(name_input_chall.strip().title())
# print(f"\nLista final de usuarios: {user_names_collected}")

# 5. Encuesta Continua:
#    Haz una pregunta (ej. "¿Cuál es tu color favorito?") y permite que múltiples personas respondan.
#    Guarda cada respuesta en un diccionario donde la clave es el nombre de la persona
#    y el valor es su respuesta.
#    Pregunta después de cada respuesta si otra persona desea participar.
#    Cuando no haya más participantes, imprime todos los resultados de la encuesta.
print("\n5. Encuesta Continua:")
# poll_results = {}
# polling_active_chall = True
# print("¡Bienvenido a la encuesta!")
# while polling_active_chall:
#     name_chall = input("¿Cuál es tu nombre? ")
#     response_chall = input("¿Cuál es tu color favorito? ")
#     poll_results[name_chall.title()] = response_chall.lower()
#     another_person = input("¿Hay otra persona que quiera participar? (sí/no) ")
#     if another_person.lower() == 'no':
#         polling_active_chall = False
# print("\n--- Resultados de la Encuesta ---")
# for name, response in poll_results.items():
#     print(f"{name} dijo que su color favorito es {response}.")

# 6. Lista de Tareas Interactivas:
#    Permite al usuario gestionar una lista de tareas.
#    Opciones: "añadir", "ver", "eliminar", "salir".
#    Implementa cada opción con bucles `while` y condicionales.
#    No te preocupes por la persistencia de datos aún.
print("\n6. Lista de Tareas Interactivas:")
# tasks = []
# print("Bienvenido a tu Gestor de Tareas.")
# while True:
#     action = input("\n¿Qué quieres hacer? (añadir, ver, eliminar, salir): ").lower()
#     if action == 'añadir':
#         new_task = input("Ingresa la nueva tarea: ")
#         tasks.append(new_task)
#         print(f"Tarea '{new_task}' añadida.")
#     elif action == 'ver':
#         if tasks:
#             print("\n--- Tus Tareas ---")
#             for i, task in enumerate(tasks):
#                 print(f"{i + 1}. {task}")
#         else:
#             print("No tienes tareas pendientes.")
#     elif action == 'eliminar':
#         if tasks:
#             try:
#                 task_num = int(input("Ingresa el número de la tarea a eliminar: "))
#                 if 1 <= task_num <= len(tasks):
#                     removed = tasks.pop(task_num - 1)
#                     print(f"Tarea '{removed}' eliminada.")
#                 else:
#                     print("Número de tarea inválido.")
#             except ValueError:
#                 print("Entrada inválida. Por favor, ingresa un número.")
#         else:
#             print("No hay tareas para eliminar.")
#     elif action == 'salir':
#         print("¡Adiós!")
#         break
#     else:
#         print("Acción no reconocida. Por favor, intenta de nuevo.")

# 7. Contador de Números con Límites:
#    Pide al usuario un número inicial y un número final.
#    Luego, imprime todos los números en ese rango (inclusive).
#    Si el número inicial es mayor que el final, imprime un mensaje de error.
print("\n7. Contador de Números con Límites:")
# while True:
#     start_str = input("Ingresa el número inicial: ")
#     if start_str.lower() == 'q': break
#     end_str = input("Ingresa el número final: ")
#     if end_str.lower() == 'q': break
#     try:
#         start_num = int(start_str)
#         end_num = int(end_str)
#         if start_num > end_num:
#             print("Error: El número inicial no puede ser mayor que el final.")
#         else:
#             current = start_num
#             while current <= end_num:
#                 print(current)
#                 current += 1
#             break # Sale del bucle si el rango es válido y se imprime.
#     except ValueError:
#         print("Entrada inválida. Por favor, ingresa números enteros.")

# 8. Verificador de Contraseña con Intentos Limitados:
#    Define una contraseña fija.
#    Pide al usuario la contraseña. Tiene 3 intentos.
#    Si acierta, imprime "Acceso concedido." y termina.
#    Si agota los intentos, imprime "Acceso denegado. Demasiados intentos."
print("\n8. Verificador de Contraseña con Intentos Limitados:")
# correct_password = "password123"
# attempts_left = 3
# while attempts_left > 0:
#     user_password = input(f"Ingresa la contraseña ({attempts_left} intentos restantes): ")
#     if user_password == correct_password:
#         print("Acceso concedido.")
#         break
#     else:
#         attempts_left -= 1
#         if attempts_left > 0:
#             print("Contraseña incorrecta. Intenta de nuevo.")
#         else:
#             print("Acceso denegado. Demasiados intentos.")

# 9. Simulación de Caja Registradora Simple:
#    Pide al usuario el precio de un artículo. Continúa pidiendo precios hasta que el usuario ingrese "0" (cero).
#    Almacena los precios en una lista.
#    Al final, calcula y muestra el total de la compra.
print("\n9. Simulación de Caja Registradora:")
# item_prices = []
# print("Ingresa los precios de los artículos (ingresa 0 para terminar):")
# while True:
#     price_str = input("Precio del artículo: ")
#     try:
#         price = float(price_str)
#         if price == 0:
#             break
#         elif price < 0:
#             print("El precio no puede ser negativo.")
#         else:
#             item_prices.append(price)
#     except ValueError:
#         print("Entrada inválida. Por favor, ingresa un número.")
# total_purchase = sum(item_prices)
# print(f"\nTotal de la compra: ${total_purchase:.2f}")

# 10. Procesador de Comandos Básico (con `continue`):
#     Pide al usuario un comando (ej. "hola", "info", "error", "salir").
#     Si es "error", usa `continue` para saltar la impresión y decir "Comando no válido".
#     Si es "salir", termina el bucle. Para otros comandos, repite el comando.
print("\n10. Procesador de Comandos Básico:")
# print("Ingresa comandos (hola, info, error, salir):")
# while True:
#     command = input("Comando: ").lower()
#     if command == 'salir':
#         print("Saliendo del procesador de comandos.")
#         break
#     elif command == 'error':
#         print("Comando no válido. Intenta de nuevo.")
#         continue # Salta el resto de la iteración.
#     else:
#         print(f"Ejecutando: {command}")

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 7 ===")
print("="*80 + "\n")

#endregion

#region CAPÍTULO 8: FUNCIONES

# ======================================================================================================================
# CAPÍTULO 8: FUNCIONES
# ======================================================================================================================
#
# Este capítulo enseña a escribir y usar funciones, bloques de código reutilizables para tareas específicas.
#
# Conceptos clave:
# - Definición de función: Usa `def` para crear una función.
# - Parámetros vs. Argumentos: Los parámetros son los nombres de las variables en la definición; los argumentos son los valores pasados al llamar la función.
# - Tipos de argumentos:
#   - Posicionales: Ordenados según la definición.
#   - de Palabra Clave: Pares `nombre=valor`, el orden no importa.
#   - con Valores por Defecto: Parámetros opcionales con un valor preestablecido.
# - Valor de retorno: La palabra clave `return` permite que una función devuelva un valor o una estructura de datos.
# - Argumentos arbitrarios:
#   - `*args`: Recopila un número variable de argumentos posicionales en una tupla.
#   - `**kwargs`: Recopila un número variable de argumentos de palabra clave en un diccionario.
# - Módulos: Almacena funciones en archivos `.py` separados para organizar el código.
# - Importar:
#   - `import module_name`: Importa el módulo completo.
#   - `from module_name import function`: Importa una función específica.
#   - `as`: Crea un alias para módulos o funciones.
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 8: CONCEPTOS Y EJEMPLOS ===")
print("="*80)

# --- INICIO FUNCIÓN: greet_user ---
def greet_user():
    """Muestra un saludo simple."""
    print("¡Hola!")
# --- FIN FUNCIÓN: greet_user ---
print("--- 8.1 Definiendo una función ---")
greet_user()

# --- INICIO FUNCIÓN: greet_user_name ---
def greet_user_name(username): # `username` es un parámetro.
    """Muestra un saludo personalizado."""
    print(f"¡Hola, {username.title()}!")
# --- FIN FUNCIÓN: greet_user_name ---
print("\n--- 8.2 Pasando información a una función ---")
greet_user_name('jesse') # `'jesse'` es un argumento.

# --- INICIO FUNCIÓN: describe_pet ---
def describe_pet(animal_type, pet_name): # Parámetros posicionales.
    print(f"Tengo un {animal_type}.")
    print(f"El nombre de mi {animal_type} es {pet_name.title()}.")
# --- FIN FUNCIÓN: describe_pet ---
print("\n--- 8.3 Pasando argumentos ---")
print("--- Argumentos Posicionales ---")
describe_pet('hamster', 'harry') # El orden importa.
describe_pet('dog', 'willie')

print("\n--- Argumentos de Palabra Clave ---")
describe_pet(animal_type='dog', pet_name='willie') # El orden no importa.
describe_pet(pet_name='harry', animal_type='hamster')

# --- INICIO FUNCIÓN: describe_pet_default ---
def describe_pet_default(pet_name, animal_type='dog'): # 'dog' es el valor por defecto.
    print(f"Tengo un {animal_type}.")
    print(f"El nombre de mi {animal_type} es {pet_name.title()}.")
# --- FIN FUNCIÓN: describe_pet_default ---
print("\n--- 8.4 Valores por defecto ---")
describe_pet_default('willie') # Usa el valor por defecto 'dog'.
describe_pet_default(pet_name='harry', animal_type='hamster') # Anula el valor por defecto.

# --- INICIO FUNCIÓN: get_formatted_name ---
def get_formatted_name(first_name, last_name):
    """Devuelve un nombre completo bien formateado."""
    full_name = f"{first_name} {last_name}"
    return full_name.title() # Devuelve el valor.
# --- FIN FUNCIÓN: get_formatted_name ---
print("\n--- 8.5 Valores de retorno ---")
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# --- INICIO FUNCIÓN: get_formatted_name_optional ---
def get_formatted_name_optional(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
# --- FIN FUNCIÓN: get_formatted_name_optional ---
print("\n--- 8.6 Parámetro opcional ---")
print(get_formatted_name_optional('jimi', 'hendrix'))
print(get_formatted_name_optional('john', 'hooker', 'lee'))


print("\n--- 8.7 Argumentos arbitrarios (`*args` y `**kwargs`) ---")
# --- INICIO FUNCIÓN: make_pizza_args ---
def make_pizza_args(size, *toppings): # `*toppings` recoge los argumentos posicionales en una tupla.
    print(f"\nPreparando una pizza de {size}-inch con los siguientes ingredientes:")
    for topping in toppings:
        print(f"- {topping}")
# --- FIN FUNCIÓN: make_pizza_args ---
make_pizza_args(16, 'pepperoni')
make_pizza_args(12, 'mushrooms', 'green peppers', 'extra cheese')

# --- INICIO FUNCIÓN: build_profile_kwargs ---
def build_profile_kwargs(first, last, **user_info): # `**user_info` recoge los argumentos de palabra clave en un diccionario.
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
# --- FIN FUNCIÓN: build_profile_kwargs ---
user_profile = build_profile_kwargs('albert', 'einstein', location='princeton', field='physics')
print(f"\nPerfil de usuario: {user_profile}")


print("\n--- 8.8 Módulos (Importando funciones) ---")
# Para estos ejemplos, crea un archivo `pizza_module.py` con la función `make_pizza`.
#
# Contenido de `pizza_module.py`:
# def make_pizza(size, *toppings):
#     print(f"\nPreparando una pizza de {size}-inch con los siguientes ingredientes:")
#     for topping in toppings:
#         print(f"- {topping}")
#
# Luego, en tu archivo principal, puedes importar de varias formas:
#
# import pizza_module
# pizza_module.make_pizza(16, 'pepperoni')
#
# from pizza_module import make_pizza
# make_pizza(12, 'mushrooms')
#
# from pizza_module import make_pizza as mp
# mp(10, 'cheese')
#
# import pizza_module as p
# p.make_pizza(8, 'ham')
#
# from pizza_module import *
# make_pizza(14, 'olives')
print("Revisa los comentarios anteriores para entender cómo importar funciones desde otros archivos.")


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 8: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

### Ejercicio 8-1. Message
# Define y llama una función que imprime un mensaje sobre el capítulo.
# --- INICIO FUNCIÓN: display_message ---
def display_message():
    print("8-1: En este capítulo, estoy aprendiendo sobre funciones en Python.")
# --- FIN FUNCIÓN: display_message ---
display_message()

### Ejercicio 8-2. Favorite Book
# Crea una función que acepte un título de libro como parámetro.
# --- INICIO FUNCIÓN: favorite_book ---
def favorite_book(title):
    print(f"8-2: Uno de mis libros favoritos es {title.title()}.")
# --- FIN FUNCIÓN: favorite_book ---
favorite_book('el señor de los anillos')

### Ejercicio 8-3. T-Shirt
# Función para crear camisetas con talla y mensaje.
# --- INICIO FUNCIÓN: make_shirt ---
def make_shirt(size, message):
    print(f"\n8-3: Se creará una camiseta de talla {size.upper()} con el mensaje: '{message}'.")
# --- FIN FUNCIÓN: make_shirt ---
make_shirt('m', 'I love Python') # Posicionales.
make_shirt(size='l', message='Code is poetry') # Palabra Clave.

### Ejercicio 8-4. Large Shirts
# Modifica la función anterior para tener valores por defecto.
# --- INICIO FUNCIÓN: make_shirt_default ---
def make_shirt_default(size='L', message='I love Python'):
    print(f"\n8-4: Se creará una camiseta de talla {size.upper()} con el mensaje: '{message}'.")
# --- FIN FUNCIÓN: make_shirt_default ---
make_shirt_default() # Grande por defecto.
make_shirt_default(size='m') # Talla mediana, mensaje por defecto.
make_shirt_default('xl', 'Hello world!') # Personalizado.

### Ejercicio 8-5. Cities
# Función para describir una ciudad y su país, con un valor por defecto para el país.
# --- INICIO FUNCIÓN: describe_city ---
def describe_city(city, country='Iceland'):
    print(f"\n8-5: {city.title()} is in {country.title()}.")
# --- FIN FUNCIÓN: describe_city ---
describe_city('reykjavik')
describe_city('london', 'united kingdom')
describe_city('tokyo', 'japan')

### Ejercicio 8-6. City Names
# Función que devuelve un string formateado.
# --- INICIO FUNCIÓN: city_country ---
def city_country(city, country):
    return f"{city.title()}, {country.title()}"
# --- FIN FUNCIÓN: city_country ---
print(f"\n8-6: {city_country('santiago', 'chile')}")

### Ejercicio 8-7. Album
# Función que crea un diccionario para un álbum, con un parámetro opcional para el número de canciones.
# --- INICIO FUNCIÓN: make_album ---
def make_album(artist, title, songs=None):
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album
# --- FIN FUNCIÓN: make_album ---
print(f"\n8-7: {make_album('led zeppelin', 'iv')}")
print(f"8-7: {make_album('pink floyd', 'the wall', songs=26)}")

### Ejercicio 8-8. User Albums
# Usa un bucle `while` para obtener entrada del usuario y crear álbumes.
print("\n8-8: Generador de álbumes (bucle while):")
# --- INICIO BUCLE: user_albums_loop ---
# while True:
#     print("\nIngresa los datos del álbum (escribe 'q' para salir):")
#     artist_input = input("Artista: ")
#     if artist_input == 'q': break
#     title_input = input("Título: ")
#     if title_input == 'q': break
#     album_created = make_album(artist_input, title_input)
#     print(album_created)
# --- FIN BUCLE: user_albums_loop ---

### Ejercicio 8-9. Messages
# Función que imprime mensajes de una lista.
# --- INICIO FUNCIÓN: show_messages ---
def show_messages(messages):
    print("\n8-9: Mensajes:")
    for message in messages:
        print(f"- {message}")
# --- FIN FUNCIÓN: show_messages ---
text_messages = ['hola', 'cómo estás?', 'nos vemos luego']
show_messages(text_messages)

### Ejercicio 8-10. Sending Messages
# Mueve mensajes de una lista a otra.
# --- INICIO FUNCIÓN: send_messages ---
def send_messages(messages_to_send, sent_messages):
    print("\n8-10: Enviando mensajes:")
    while messages_to_send:
        current_message = messages_to_send.pop(0) # pop(0) para sacar del inicio y mantener orden.
        print(f"- Enviando: {current_message}")
        sent_messages.append(current_message)
# --- FIN FUNCIÓN: send_messages ---
messages_to_send = ['hola', 'cómo estás?', 'nos vemos luego']
sent_messages = []
send_messages(messages_to_send, sent_messages)
print(f"\n8-10: Lista original (vacía): {messages_to_send}")
print(f"8-10: Lista de mensajes enviados: {sent_messages}")

### Ejercicio 8-11. Archived Messages
# Pasa una copia de una lista para evitar modificar la original.
messages_to_send_copy = ['hola', 'cómo estás?', 'nos vemos luego']
sent_messages_archived = []
send_messages(messages_to_send_copy[:], sent_messages_archived) # Pasa una copia con `[:]`.
print(f"\n8-11: Lista original (se conserva): {messages_to_send_copy}")
print(f"8-11: Mensajes archivados: {sent_messages_archived}")

### Ejercicio 8-12. Sandwiches
# Función con un número arbitrario de argumentos posicionales.
# --- INICIO FUNCIÓN: make_sandwich ---
def make_sandwich(*items):
    print("\n8-12: Preparando un sándwich con:")
    for item in items:
        print(f"- {item}")
# --- FIN FUNCIÓN: make_sandwich ---
make_sandwich('queso', 'tomate', 'lechuga')
make_sandwich('pavo', 'bacon')

### Ejercicio 8-13. User Profile
# Función con argumentos arbitrarios de palabra clave para un perfil de usuario.
# --- INICIO FUNCIÓN: build_profile_ex ---
def build_profile_ex(first, last, **user_info): # Se renombra para no chocar con ejemplo.
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
# --- FIN FUNCIÓN: build_profile_ex ---
user_profile_ex = build_profile_ex('daniel', 'velazquez', location='salina cruz',
                                hobby='programming', age=25)
print(f"\n8-13: Perfil de usuario: {user_profile_ex}")

### Ejercicio 8-14. Cars
# Función para almacenar información de un coche.
# --- INICIO FUNCIÓN: make_car ---
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
# --- FIN FUNCIÓN: make_car ---
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(f"\n8-14: Información del coche: {car}")

### Ejercicio 8-15, 8-16, 8-17. Imports and Styling
print("\n8-15, 8-16, 8-17: Estos ejercicios requieren organizar tu código en múltiples archivos y aplicar estilo. Revisa la sección de Módulos para más detalles.")

# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 8 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 8 ===")
print("="*80)

# 1. Función de Operaciones Aritméticas Básicas:
#    Crea una función `calculadora(operacion, num1, num2)` que realice una operación básica
#    (`"suma"`, `"resta"`, `"multiplicacion"`, `"division"`) con dos números.
#    La función debe devolver el resultado. Si la operación no es válida, debe devolver un mensaje de error.
#    Prueba cada operación.
# --- INICIO FUNCIÓN: calculadora ---
def calculadora(operacion, num1, num2):
    """Realiza una operación aritmética básica."""
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero."
    else:
        return "Error: Operación no válida."
# --- FIN FUNCIÓN: calculadora ---
print(f"1. Suma (5+3): {calculadora('suma', 5, 3)}")
print(f"   División (10/2): {calculadora('division', 10, 2)}")
print(f"   División (10/0): {calculadora('division', 10, 0)}")
print(f"   Operación inválida: {calculadora('potencia', 2, 3)}")

# 2. Generador de Rango de Números:
#    Crea una función `generar_rango(inicio, fin, paso=1)` que devuelva una lista de números
#    en el rango especificado. Si `paso` no se proporciona, debe ser 1.
#    Si `inicio` es mayor que `fin` y `paso` es positivo, o viceversa, debe devolver una lista vacía o un mensaje de error.
# --- INICIO FUNCIÓN: generar_rango ---
def generar_rango(inicio, fin, paso=1):
    """Genera una lista de números en un rango dado."""
    if (paso > 0 and inicio > fin) or (paso < 0 and inicio < fin):
        return [] # Retorna lista vacía para rangos imposibles.
    return list(range(inicio, fin + (1 if paso > 0 else -1), paso)) # Ajusta `fin` para ser inclusivo.
# --- FIN FUNCIÓN: generar_rango ---
print(f"2. Rango (1, 5): {generar_rango(1, 5)}")
print(f"   Rango (1, 10, 2): {generar_rango(1, 10, 2)}")
print(f"   Rango (5, 1, -1): {generar_rango(5, 1, -1)}")
print(f"   Rango imposible (10, 5): {generar_rango(10, 5)}")

# 3. Función para Verificar Número Primo:
#    Crea una función `es_primo(numero)` que devuelva `True` si un número es primo y `False` en caso contrario.
#    (Un número primo es aquel que solo es divisible por 1 y por sí mismo).
#    Prueba la función con varios números.
# --- INICIO FUNCIÓN: es_primo ---
def es_primo(numero):
    """Verifica si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, numero): # Itera desde 2 hasta el número-1.
        if numero % i == 0:
            return False # Si es divisible, no es primo.
    return True # Si no encontró divisores, es primo.
# --- FIN FUNCIÓN: es_primo ---
print(f"3. ¿Es 7 primo?: {es_primo(7)}")
print(f"   ¿Es 10 primo?: {es_primo(10)}")
print(f"   ¿Es 2 primo?: {es_primo(2)}")
print(f"   ¿Es 1 primo?: {es_primo(1)}")

# 4. Formateador de Nombres Versátil:
#    Modifica la función `get_formatted_name_optional` para que también pueda aceptar un `titulo` (Sr., Sra., Dr.)
#    como argumento opcional (keyword-only argument).
#    Debe devolver el nombre formateado (ej. "Dr. John Doe").
#    Sugerencia: Usa `**kwargs` y luego verifica la clave 'titulo'.
# --- INICIO FUNCIÓN: get_formatted_name_versatile ---
def get_formatted_name_versatile(first_name, last_name, middle_name='', **kwargs):
    """Devuelve un nombre completo bien formateado con un título opcional."""
    full_name = f"{first_name} {middle_name} {last_name}".strip() # strip para eliminar doble espacio si no hay middle.
    if 'title' in kwargs:
        return f"{kwargs['title']} {full_name.title()}"
    return full_name.title()
# --- FIN FUNCIÓN: get_formatted_name_versatile ---
print(f"4. Nombre con título: {get_formatted_name_versatile('john', 'doe', title='Dr.')}")
print(f"   Nombre con segundo nombre y título: {get_formatted_name_versatile('mary', 'jane', 'sue', title='Sra.')}")
print(f"   Nombre sin título: {get_formatted_name_versatile('peter', 'pan')}")

# 5. Resumen de Pedido de Café:
#    Crea una función `resumen_pedido_cafe(tamaño, *ingredientes_extra, **detalles_pago)` que reciba:
#    - `tamaño` del café (posicional).
#    - Cualquier número de `ingredientes_extra` (ej. "leche", "azucar").
#    - Detalles de pago como argumentos de palabra clave (ej. `metodo="tarjeta"`, `propina=2.50`).
#    La función debe imprimir un resumen completo del pedido.
# --- INICIO FUNCIÓN: resumen_pedido_cafe ---
def resumen_pedido_cafe(size, *extra_ingredients, **payment_details):
    """Imprime un resumen completo de un pedido de café."""
    print(f"\n5. Resumen del Pedido de Café ({size.title()}):")
    if extra_ingredients:
        print("   Ingredientes extra:")
        for ingredient in extra_ingredients:
            print(f"     - {ingredient.title()}")
    else:
        print("   Sin ingredientes extra.")

    if payment_details:
        print("   Detalles de pago:")
        for key, value in payment_details.items():
            print(f"     - {key.replace('_', ' ').title()}: {value}")
# --- FIN FUNCIÓN: resumen_pedido_cafe ---
resumen_pedido_cafe("grande", "leche de avena", "azúcar", metodo="efectivo", total_pagado=5.00)
resumen_pedido_cafe("pequeño", metodo="tarjeta")

# 6. Sumador de Lista (con Valor Opcional):
#    Crea una función `sumar_lista(lista_numeros, valor_inicial=0)` que sume todos los números
#    en una lista, comenzando desde un `valor_inicial` opcional.
#    La función debe devolver el total.
# --- INICIO FUNCIÓN: sumar_lista ---
def sumar_lista(lista_numeros, valor_inicial=0):
    """Suma todos los números en una lista, opcionalmente con un valor inicial."""
    total = valor_inicial
    for numero in lista_numeros:
        total += numero
    return total
# --- FIN FUNCIÓN: sumar_lista ---
numeros_a_sumar = [1, 2, 3, 4, 5]
print(f"6. Suma de {numeros_a_sumar}: {sumar_lista(numeros_a_sumar)}")
print(f"   Suma de {numeros_a_sumar} con valor inicial 10: {sumar_lista(numeros_a_sumar, 10)}")

# 7. Creador de Listas Personalizadas:
#    Crea una función `crear_lista_personalizada(tipo_elementos, *elementos)` que reciba
#    un string `tipo_elementos` (ej. "frutas", "colores") y luego una cantidad arbitraria de elementos.
#    La función debe imprimir un mensaje indicando el tipo de elementos y luego listar cada uno.
# --- INICIO FUNCIÓN: crear_lista_personalizada ---
def crear_lista_personalizada(tipo_elementos, *elementos):
    """Imprime una lista personalizada de elementos."""
    print(f"\n7. Lista de {tipo_elementos.title()}:")
    if elementos:
        for elemento in elementos:
            print(f"   - {elemento.title()}")
    else:
        print("   (Sin elementos)")
# --- FIN FUNCIÓN: crear_lista_personalizada ---
crear_lista_personalizada("frutas", "manzana", "banana", "uva")
crear_lista_personalizada("colores", "rojo", "azul")
crear_lista_personalizada("animales")

# 8. Verificador de Contraseña con Longitud Mínima:
#    Crea una función `validar_contrasena(contrasena, min_longitud=8)` que devuelva `True`
#    si la contraseña tiene al menos la `min_longitud` especificada, y `False` en caso contrario.
#    Usa un valor por defecto para `min_longitud`.
# --- INICIO FUNCIÓN: validar_contrasena ---
def validar_contrasena(contrasena, min_longitud=8):
    """Valida si una contraseña cumple con una longitud mínima."""
    return len(contrasena) >= min_longitud
# --- FIN FUNCIÓN: validar_contrasena ---
print(f"8. Contraseña 'abc' (min 8): {validar_contrasena('abc')}")
print(f"   Contraseña 'python123' (min 8): {validar_contrasena('python123')}")
print(f"   Contraseña 'short' (min 3): {validar_contrasena('short', min_longitud=3)}")

# 9. Formateador de Fechas (Básico):
#    Crea una función `formatear_fecha(dia, mes, anio, formato="DD/MM/AAAA")` que reciba
#    día, mes y año como números, y un `formato` opcional como string.
#    Debe devolver la fecha formateada. Solo soporta "DD/MM/AAAA" y "MM-DD-AAAA".
# --- INICIO FUNCIÓN: formatear_fecha ---
def formatear_fecha(dia, mes, anio, formato="DD/MM/AAAA"):
    """Formatea una fecha según el formato especificado."""
    s_dia = str(dia).zfill(2) # zfill(2) para añadir 0 a la izquierda si es necesario.
    s_mes = str(mes).zfill(2)
    s_anio = str(anio)
    if formato == "DD/MM/AAAA":
        return f"{s_dia}/{s_mes}/{s_anio}"
    elif formato == "MM-DD-AAAA":
        return f"{s_mes}-{s_dia}-{s_anio}"
    else:
        return "Error: Formato no soportado."
# --- FIN FUNCIÓN: formatear_fecha ---
print(f"9. Fecha (5, 7, 2024): {formatear_fecha(5, 7, 2024)}")
print(f"   Fecha (1, 1, 2023, 'MM-DD-AAAA'): {formatear_fecha(1, 1, 2023, 'MM-DD-AAAA')}")

# 10. Generador de Saludo Completo:
#     Crea una función `generar_saludo(**info_personal)` que acepte información personal
#     arbitraria (ej. nombre, edad, ciudad).
#     La función debe imprimir un saludo que incluya toda la información proporcionada.
#     Si no se proporciona nombre, usar "Desconocido".
# --- INICIO FUNCIÓN: generar_saludo ---
def generar_saludo(**info_personal):
    """Genera un saludo completo con información personal arbitraria."""
    nombre = info_personal.get('nombre', 'Desconocido')
    saludo = f"Hola, {nombre.title()}."
    if 'edad' in info_personal:
        saludo += f" Tienes {info_personal['edad']} años."
    if 'ciudad' in info_personal:
        saludo += f" Vives en {info_personal['ciudad'].title()}."
    print(f"10. {saludo}")
# --- FIN FUNCIÓN: generar_saludo ---
generar_saludo(nombre="ana", edad=30, ciudad="barcelona")
generar_saludo(nombre="juan")
generar_saludo(ciudad="madrid")

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 8 ===")
print("="*80 + "\n")

#endregion

#region CAPÍTULO 9: CLASES

# ======================================================================================================================
# CAPÍTULO 9: CLASES
# ======================================================================================================================
#
# Este capítulo introduce la programación orientada a objetos (POO), modelando objetos del mundo real.
#
# Conceptos clave:
# - Clase: Un plano o modelo para crear objetos.
# - Objeto (Instancia): Una entidad específica creada a partir de una clase.
# - `__init__()`: Un método especial que se ejecuta al crear una instancia para inicializar sus atributos.
# - `self`: Referencia a la instancia actual. Es el primer parámetro en todos los métodos de instancia.
# - Atributos: Variables que pertenecen a un objeto.
# - Métodos: Funciones que operan sobre un objeto.
# - Herencia: Una clase hija hereda los atributos y métodos de una clase padre.
#   - `super()`: Llama a un método de la clase padre.
# - Composición: Usar una instancia de una clase como un atributo en otra clase.
# - Módulos y Clases: Almacena clases en archivos `.py` separados para organizar el código.
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 9: CONCEPTOS Y EJEMPLOS ===")
print("="*80)

print("--- 9.1 Creando una clase ---")
# --- INICIO CLASE: Dog ---
class Dog:
    """Un intento simple de modelar un perro."""
    def __init__(self, name, age):
        """Inicializa los atributos de nombre y edad."""
        self.name = name # Atributo.
        self.age = age
    def sit(self):
        """Simula a un perro sentándose."""
        print(f"{self.name} ahora está sentado.")
    def roll_over(self):
        """Simula a un perro rodando."""
        print(f"{self.name} rolled over!")
# --- FIN CLASE: Dog ---

my_dog = Dog('Willie', 6) # Creando una instancia de la clase `Dog`.
print(f"El nombre de mi perro es {my_dog.name}.")
print(f"Mi perro tiene {my_dog.age} años.")
my_dog.sit() # Llamando a un método.


print("\n--- 9.2 Trabajando con atributos ---")
# --- INICIO CLASE: Car ---
class Car:
    """Un intento simple de representar un coche."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Atributo con valor por defecto.
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"Este coche tiene {self.odometer_reading} millas en el odómetro.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("¡No puedes retroceder el odómetro!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
# --- FIN CLASE: Car ---

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 # Modificando un atributo directamente.
my_new_car.read_odometer()
my_new_car.update_odometer(100) # Modificando con un método.
my_new_car.read_odometer()


print("\n--- 9.3 Herencia ---")
# --- INICIO CLASE: ElectricCar ---
class ElectricCar(Car): # `ElectricCar` hereda de `Car`.
    """Representa aspectos de un coche eléctrico."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # Llama al método __init__ del padre.
        self.battery_size = 40 # Atributo específico de la clase hija.
    def describe_battery(self):
        print(f"Este coche tiene una batería de {self.battery_size}-kWh.")
# --- FIN CLASE: ElectricCar ---

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


print("\n--- 9.4 Composición (Instancias como atributos) ---")
# --- INICIO CLASE: Battery ---
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"Esta batería es de {self.battery_size}-kWh.")
# --- FIN CLASE: Battery ---

# --- INICIO CLASE: ElectricCar_Comp ---
class ElectricCar_Comp(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() # Una instancia de `Battery` como atributo.
# --- FIN CLASE: ElectricCar_Comp ---

my_tesla = ElectricCar_Comp('tesla', 'model 3', 2024)
my_tesla.battery.describe_battery()


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 9: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

### Ejercicio 9-1. Restaurant
# Crea una clase `Restaurant` con atributos y métodos.
# --- INICIO CLASE: Restaurant ---
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"\n9-1: El restaurante se llama {self.restaurant_name} y sirve comida {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"9-1: ¡El restaurante {self.restaurant_name} está abierto!")
# --- FIN CLASE: Restaurant ---
restaurant = Restaurant('La Mamma', 'italiana')
print(f"\n9-1: Nombre: {restaurant.restaurant_name}")
print(f"9-1: Tipo de cocina: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

### Ejercicio 9-2. Three Restaurants
# Crea tres instancias de la clase `Restaurant`.
restaurant1 = Restaurant('Sushi King', 'japonesa')
restaurant2 = Restaurant('El Fuego', 'mexicana')
restaurant3 = Restaurant('The French Bistro', 'francesa')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

### Ejercicio 9-3. Users
# Crea una clase `User` con atributos y métodos.
# --- INICIO CLASE: User ---
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    def describe_user(self):
        print(f"\n9-3: Perfil de usuario:")
        print(f"\t- Nombre: {self.first_name.title()} {self.last_name.title()}")
        print(f"\t- Edad: {self.age}")
        print(f"\t- Ciudad: {self.city.title()}")
    def greet_user(self):
        print(f"9-3: ¡Hola, {self.first_name.title()}! Bienvenido de nuevo.")
# --- FIN CLASE: User ---
user1 = User('alice', 'smith', 28, 'new york')
user2 = User('bob', 'johnson', 35, 'london')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

### Ejercicio 9-4. Number Served
# Añade un atributo y métodos para rastrear el número de clientes servidos.
# --- INICIO CLASE: Restaurant_Served ---
class Restaurant_Served(Restaurant):
    def __init__(self, name, cuisine, number_served=0):
        super().__init__(name, cuisine)
        self.number_served = number_served
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, increment):
        self.number_served += increment
# --- FIN CLASE: Restaurant_Served ---
restaurant_served = Restaurant_Served('The Great Plate', 'fusion')
print(f"\n9-4: Clientes servidos: {restaurant_served.number_served}")
restaurant_served.number_served = 15 # Cambiar directamente.
print(f"9-4: Clientes servidos (directo): {restaurant_served.number_served}")
restaurant_served.set_number_served(30) # Cambiar con método.
print(f"9-4: Clientes servidos (con método): {restaurant_served.number_served}")
restaurant_served.increment_number_served(12) # Incrementar.
print(f"9-4: Clientes servidos (incremento): {restaurant_served.number_served}")

### Ejercicio 9-5. Login Attempts
# Añade un contador de intentos de inicio de sesión a la clase `User`.
# --- INICIO CLASE: User_Login ---
class User_Login(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.login_attempts = 0
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
# --- FIN CLASE: User_Login ---
user_login_test = User_Login('maria', 'lopez', 29, 'madrid')
user_login_test.increment_login_attempts()
user_login_test.increment_login_attempts()
user_login_test.increment_login_attempts()
print(f"\n9-5: Intentos de inicio de sesión: {user_login_test.login_attempts}")
user_login_test.reset_login_attempts()
print(f"9-5: Intentos de inicio de sesión después del reinicio: {user_login_test.login_attempts}")

### Ejercicio 9-6. Ice Cream Stand
# Crea una clase `IceCreamStand` que hereda de `Restaurant`.
# --- INICIO CLASE: IceCreamStand ---
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors):
        super().__init__(name, cuisine)
        self.flavors = flavors
    def display_flavors(self):
        print(f"\n9-6: Los sabores de helado disponibles en {self.restaurant_name} son:")
        for flavor in self.flavors:
            print(f"\t- {flavor.title()}")
# --- FIN CLASE: IceCreamStand ---
ice_cream_stand = IceCreamStand('Sweet Scoop', 'heladería', ['vainilla', 'chocolate', 'fresa'])
ice_cream_stand.display_flavors()

### Ejercicio 9-7. Admin & 9-8. Privileges
# Crea clases para un usuario administrador y sus privilegios.
# El ejercicio 9-8 refactoriza el 9-7 usando composición.
# --- INICIO CLASE: Privileges ---
class Privileges:
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges
    def show_privileges(self):
        print("Privilegios del administrador:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")
# --- FIN CLASE: Privileges ---

# --- INICIO CLASE: Admin ---
class Admin(User): # Admin hereda de User.
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges() # Composición: una instancia de Privileges como atributo.
# --- FIN CLASE: Admin ---
admin_user = Admin('super', 'user', 45, 'cyberspace')
print("\n9-7 & 9-8:")
admin_user.privileges.show_privileges()

### Ejercicio 9-9. Battery Upgrade
# Añade un método para actualizar una batería.
# Para este ejercicio, se asume que la clase `Battery` ya fue definida en los ejemplos (9.4).
# Aquí se añade el método `upgrade_battery` a la clase `Battery` para este ejercicio.
# --- MODIFICACIÓN CLASE: Battery (para 9-9) ---
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"Esta batería es de {self.battery_size}-kWh.")
    def get_range(self): # Método ya existente en el ejemplo.
        if self.battery_size == 40:
            return 150
        elif self.battery_size == 65:
            return 225
        else:
            return "Rango desconocido"
    def upgrade_battery(self): # Nuevo método para el ejercicio 9-9.
        if self.battery_size < 65:
            self.battery_size = 65
            print("¡Batería mejorada a 65-kWh!")
        else:
            print("La batería ya está actualizada.")
# --- FIN MODIFICACIÓN CLASE: Battery ---

# Se asume que ElectricCar_Comp usa esta nueva Battery.
# --- MODIFICACIÓN CLASE: ElectricCar_Comp (para 9-9) ---
class ElectricCar_Comp(Car): # Definición completa para asegurar que usa la Battery actualizada.
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() # Usa la clase Battery modificada.
# --- FIN MODIFICACIÓN CLASE: ElectricCar_Comp ---

my_leaf_upgrade = ElectricCar_Comp('nissan', 'leaf', 2024)
print(f"\n9-9: Rango inicial: {my_leaf_upgrade.battery.get_range()} millas.")
my_leaf_upgrade.battery.upgrade_battery()
print(f"9-9: Rango después de la mejora: {my_leaf_upgrade.battery.get_range()} millas.")

### Ejercicio 9-10, 9-11, 9-12. Importing Classes
# Estos ejercicios requieren la gestión de múltiples archivos y módulos.
print("\n9-10, 9-11, 9-12: Estos ejercicios requieren la gestión de múltiples archivos. Revisa la sección 9.5 para la sintaxis de importación de clases.")

### Ejercicio 9-13. Dice
# Crea una clase `Die` para simular un dado.
from random import randint
# --- INICIO CLASE: Die ---
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
# --- FIN CLASE: Die ---
d6 = Die()
print("\n9-13: Lanzando el dado de 6 caras 10 veces:")
for _ in range(10):
    print(d6.roll_die(), end=" ")
d10 = Die(10)
print("\n\n9-13: Lanzando el dado de 10 caras 10 veces:")
for _ in range(10):
    print(d10.roll_die(), end=" ")
d20 = Die(20)
print("\n\n9-13: Lanzando el dado de 20 caras 10 veces:")
for _ in range(10):
    print(d20.roll_die(), end=" ")
print("\n")

### Ejercicio 9-14. Lottery
# Crea un boleto de lotería y verifica si es ganador.
from random import choice
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_ticket = []
print("9-14: El boleto ganador es:")
for _ in range(4):
    winning_ticket.append(choice(lottery_pool))
print(winning_ticket)
print("¡Cualquier boleto que coincida con estos 4 números o letras gana un premio!")

### Ejercicio 9-15. Lottery Analysis
# Simula intentos de lotería hasta obtener el boleto ganador.
my_ticket = [3, 'A', 7, 'C']
attempts = 0
while True:
    attempts += 1
    drawn_ticket = []
    for _ in range(4):
        drawn_ticket.append(choice(lottery_pool))
    if drawn_ticket == my_ticket:
        print(f"\n9-15: ¡Ganaste! Se necesitaron {attempts} intentos.")
        break

### Ejercicio 9-16. Python Module of the Week
print("\n9-16: Este ejercicio requiere explorar un sitio web de módulos de Python. No hay código ejecutable.")

# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 9 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 9 ===")
print("="*80)

# 1. Clase Libro:
#    Crea una clase `Libro` con atributos para `titulo`, `autor` y `paginas`.
#    Añade un método `leer()` que imprima "Leyendo [titulo] de [autor]".
#    Crea una instancia y llama al método.
# --- INICIO CLASE: Libro ---
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def leer(self):
        print(f"1. Leyendo '{self.titulo}' de {self.autor}.")
# --- FIN CLASE: Libro ---
mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez", 496)
mi_libro.leer()

# 2. Clase Coche con Velocímetro:
#    Extiende la clase `Car` del capítulo. Añade un atributo `velocidad_actual` con valor por defecto 0.
#    Añade métodos `acelerar(incremento)` y `frenar(decremento)` que modifiquen la `velocidad_actual`.
#    Asegúrate de que la velocidad no sea negativa.
#    Crea una instancia, acelera y frena.
# --- INICIO CLASE: CarConVelocimetro ---
class CarConVelocimetro(Car): # Hereda de la clase Car del capítulo.
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.velocidad_actual = 0
    def acelerar(self, incremento):
        self.velocidad_actual += incremento
        print(f"2. Acelerando a {self.velocidad_actual} km/h.")
    def frenar(self, decremento):
        self.velocidad_actual -= decremento
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0
        print(f"2. Frenando a {self.velocidad_actual} km/h.")
# --- FIN CLASE: CarConVelocimetro ---
mi_coche_nuevo = CarConVelocimetro("Toyota", "Corolla", 2023)
mi_coche_nuevo.acelerar(50)
mi_coche_nuevo.frenar(20)
mi_coche_nuevo.frenar(40) # Debe ir a 0.

# 3. Clase Estudiante con Materias:
#    Crea una clase `Estudiante` con `nombre` y una lista de `materias_inscritas` (vacía por defecto).
#    Añade métodos `inscribir_materia(materia)` y `mostrar_materias()`.
#    Crea una instancia, inscribe 2-3 materias y muéstralas.
# --- INICIO CLASE: Estudiante ---
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias_inscritas = []
    def inscribir_materia(self, materia):
        self.materias_inscritas.append(materia.title())
        print(f"3. {self.nombre.title()} se ha inscrito en {materia.title()}.")
    def mostrar_materias(self):
        print(f"3. Materias inscritas de {self.nombre.title()}: {', '.join(self.materias_inscritas)}")
# --- FIN CLASE: Estudiante ---
estudiante1 = Estudiante("luisa")
estudiante1.inscribir_materia("matemáticas")
estudiante1.inscribir_materia("historia")
estudiante1.mostrar_materias()

# 4. Clase Rectángulo (Tuplas para Dimensiones):
#    Crea una clase `Rectangulo` con un atributo `dimensiones` que sea una tupla (ancho, alto).
#    Añade un método `calcular_area()` que devuelva el área del rectángulo.
#    Crea una instancia y calcula su área.
# --- INICIO CLASE: Rectangulo ---
class Rectangulo:
    def __init__(self, ancho, alto):
        self.dimensiones = (ancho, alto)
    def calcular_area(self):
        return self.dimensiones[0] * self.dimensiones[1]
# --- FIN CLASE: Rectangulo ---
mi_rectangulo = Rectangulo(10, 5)
print(f"4. Área del rectángulo: {mi_rectangulo.calcular_area()}")

# 5. Clase Banco con Saldo:
#    Crea una clase `CuentaBancaria` con un atributo `saldo` (por defecto 0).
#    Añade métodos `depositar(cantidad)` y `retirar(cantidad)`.
#    Asegúrate de que no se pueda retirar más de lo que hay en el saldo.
# --- INICIO CLASE: CuentaBancaria ---
class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"5. Depositado: ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}.")
        else:
            print("5. No se puede depositar una cantidad negativa o cero.")
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"5. Retirado: ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}.")
            else:
                print(f"5. Fondos insuficientes. Saldo actual: ${self.saldo:.2f}.")
        else:
            print("5. No se puede retirar una cantidad negativa o cero.")
# --- FIN CLASE: CuentaBancaria ---
mi_cuenta = CuentaBancaria(100)
mi_cuenta.depositar(50)
mi_cuenta.retirar(70)
mi_cuenta.retirar(100) # Debería fallar.

# 6. Clase Producto Simple:
#    Crea una clase `Producto` con `nombre`, `precio` y `stock`.
#    Añade un método `mostrar_info()` que imprima todos los detalles del producto.
#    Añade un método `vender(cantidad)` que reduzca el stock. Si no hay suficiente stock, debe imprimir un error.
# --- INICIO CLASE: Producto ---
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar_info(self):
        print(f"6. Producto: {self.nombre.title()}, Precio: ${self.precio:.2f}, Stock: {self.stock} unidades.")
    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"6. Vendidas {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}.")
        else:
            print(f"6. No hay suficiente stock de {self.nombre}. Stock actual: {self.stock}.")
# --- FIN CLASE: Producto ---
manzana = Producto("Manzana", 0.99, 100)
manzana.mostrar_info()
manzana.vender(30)
manzana.vender(80) # Debería imprimir error.

# 7. Clase Círculo:
#    Crea una clase `Circulo` con un atributo `radio`.
#    Añade métodos `calcular_area()` y `calcular_circunferencia()`.
#    Usa el valor de pi (3.14159) como una constante dentro del método o como variable global.
# --- INICIO CLASE: Circulo ---
PI = 3.14159 # Constante global para pi.
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return PI * (self.radio ** 2)
    def calcular_circunferencia(self):
        return 2 * PI * self.radio
# --- FIN CLASE: Circulo ---
mi_circulo = Circulo(5)
print(f"7. Área del círculo con radio 5: {mi_circulo.calcular_area():.2f}")
print(f"   Circunferencia del círculo con radio 5: {mi_circulo.calcular_circunferencia():.2f}")

# 8. Clase Blog Post:
#    Crea una clase `BlogPost` con `titulo`, `autor` y `contenido`.
#    Añade un atributo `vistas` con valor inicial 0.
#    Añade un método `ver_post()` que incremente las vistas y luego imprima el post.
# --- INICIO CLASE: BlogPost ---
class BlogPost:
    def __init__(self, titulo, autor, contenido):
        self.titulo = titulo
        self.autor = autor
        self.contenido = contenido
        self.vistas = 0
    def ver_post(self):
        self.vistas += 1
        print(f"\n8. Título: {self.titulo.title()}")
        print(f"   Autor: {self.autor.title()}")
        print(f"   Contenido: {self.contenido[:50]}...") # Muestra solo los primeros 50 caracteres.
        print(f"   Vistas: {self.vistas}")
# --- FIN CLASE: BlogPost ---
post_ejemplo = BlogPost("Mi Primer Post", "Juan Bloguero", "Este es el contenido de mi primer post en el blog. Es muy interesante y espero que a todos les guste mucho.")
post_ejemplo.ver_post()
post_ejemplo.ver_post()

# 9. Clase Persona con Edad y Cumpleaños:
#    Crea una clase `Persona` con `nombre` y `edad`.
#    Añade un método `cumplir_anos()` que incremente la edad.
#    Crea una instancia y simula que cumple años varias veces.
# --- INICIO CLASE: Persona ---
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1
        print(f"9. ¡Feliz cumpleaños, {self.nombre.title()}! Ahora tienes {self.edad} años.")
# --- FIN CLASE: Persona ---
mi_persona = Persona("Maria", 25)
mi_persona.cumplir_anos()
mi_persona.cumplir_anos()

# 10. Clase Contacto con Teléfono y Email:
#     Crea una clase `Contacto` con `nombre`, `telefono` y `email`.
#     Añade un método `actualizar_email(nuevo_email)` para cambiar el email.
#     Añade un método `enviar_mensaje()` que solo imprima un mensaje simulado.
# --- INICIO CLASE: Contacto ---
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"10. Email de {self.nombre.title()} actualizado a: {self.email}.")
    def enviar_mensaje(self):
        print(f"10. Enviando mensaje simulado a {self.nombre.title()} ({self.telefono}).")
# --- FIN CLASE: Contacto ---
contacto1 = Contacto("Ana", "555-1111", "ana@email.com")
contacto1.actualizar_email("ana.nueva@email.com")
contacto1.enviar_mensaje()

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 9 ===")
print("="*80 + "\n")

#endregion

#region CAPÍTULO 10: ARCHIVOS Y EXCEPCIONES

# ======================================================================================================================
# CAPÍTULO 10: ARCHIVOS Y EXCEPCIONES
# ======================================================================================================================
#
# Este capítulo enseña a leer y escribir archivos y a manejar errores para crear programas robustos.
#
# Conceptos clave:
# - `pathlib.Path`: Permite manejar rutas de archivos de forma moderna.
# - Leer archivos: `read_text()` lee el contenido como un string.
# - Escribir archivos: `write_text()` escribe strings en un archivo (sobrescribe si existe).
# - Excepciones: Objetos que manejan errores en tiempo de ejecución.
#   - `try-except`: Intenta un código y captura errores.
#   - `else`: Se ejecuta si el bloque `try` no genera errores.
#   - `pass`: Un placeholder que le dice a Python que no haga nada. Útil para fallar silenciosamente.
# - `json`: Módulo para almacenar datos de Python en formato JSON.
#   - `json.dumps()`: Convierte un objeto Python a un string JSON.
#   - `json.loads()`: Convierte un string JSON a un objeto Python.
# - Refactorización: Reorganizar el código en funciones con responsabilidades claras.
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 10: CONCEPTOS Y EJEMPLOS ===")
print("="*80)
from pathlib import Path
import json

print("--- 10.1 Leyendo un archivo ---")
# Para que este código funcione, debes tener el archivo `pi_digits.txt` en el mismo directorio.
# # --- INICIO LECTURA ARCHIVO ---
# path_read = Path('pi_digits.txt')
# try:
#     contents_read = path_read.read_text().rstrip()
#     print(f"Contenido del archivo:\n{contents_read}")
# except FileNotFoundError:
#     print("No se encontró el archivo 'pi_digits.txt'.")
# # --- FIN LECTURA ARCHIVO ---

print("\n--- 10.2 Escribiendo en un archivo ---")
# # --- INICIO ESCRITURA ARCHIVO ---
# path_write = Path('programming.txt')
# path_write.write_text("Me encanta programar.")
# print("Se ha escrito en el archivo 'programming.txt'.")
# # Escribiendo múltiples líneas.
# content_multi = "Línea 1.\n"
# content_multi += "Línea 2.\n"
# path_write.write_text(content_multi)
# print("Se han escrito múltiples líneas en 'programming.txt'.")
# # --- FIN ESCRITURA ARCHIVO ---


print("\n--- 10.3 Manejo de excepciones (try-except) ---")
# Un ejemplo de `ZeroDivisionError`.
try:
    print(5/0)
except ZeroDivisionError:
    print("¡No puedes dividir por cero!")

# Un ejemplo de `FileNotFoundError`.
path_missing = Path('missing_file.txt')
try:
    contents_missing = path_missing.read_text()
except FileNotFoundError:
    print(f"Lo siento, el archivo {path_missing} no existe.")


print("\n--- 10.4 Almacenando datos con JSON ---")
# Usando `json.dumps()` y `json.loads()`.
numbers_json = [2, 3, 5, 7, 11, 13]
path_json = Path('numbers.json')
contents_json = json.dumps(numbers_json)
# # --- INICIO ESCRITURA JSON ---
# path_json.write_text(contents_json) # Escribe el archivo JSON.
# # --- FIN ESCRITURA JSON ---
#
# # Para leerlo de vuelta:
# # --- INICIO LECTURA JSON ---
# contents_read_json = Path('numbers.json').read_text()
# numbers_loaded = json.loads(contents_read_json)
# print(f"Números cargados desde el archivo: {numbers_loaded}")
# # --- FIN LECTURA JSON ---


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 10: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)

# Nota: Algunos ejercicios requieren que crees archivos de texto para que funcionen.

### Ejercicio 10-1. Learning Python
# Escribe un archivo de texto y léelo de dos formas.
# Se asume que tienes un archivo `learning_python.txt` en el mismo directorio.
# path_learning = Path('learning_python.txt')
# try:
#     # Leer el archivo completo.
#     contents_learning = path_learning.read_text()
#     print("\n10-1: Contenido completo:\n", contents_learning)
#     # Leer línea por línea.
#     lines_learning = contents_learning.splitlines()
#     print("\n10-1: Contenido línea por línea:")
#     for line in lines_learning:
#         print(line)
# except FileNotFoundError:
#     print("\n10-1: Archivo 'learning_python.txt' no encontrado.")

### Ejercicio 10-2. Learning C
# Usa `replace()` para cambiar una palabra en el contenido del archivo.
# if 'contents_learning' in locals(): # Verifica si la variable existe.
#     print("\n10-2: Reemplazando la palabra 'Python':")
#     for line in contents_learning.splitlines():
#         print(line.replace('Python', 'C'))
# else:
#     print("\n10-2: No se puede ejecutar. Crea el archivo 'learning_python.txt' primero.")

### Ejercicio 10-4. Guest & 10-5. Guest Book
# Escribe el nombre de un usuario en un archivo, luego varios nombres en otro.
# guest_name = input("\n10-4: Por favor, introduce tu nombre: ")
# Path('guest.txt').write_text(guest_name)
# print(f"10-4: Tu nombre ha sido guardado en 'guest.txt'.")
#
# guest_book_entries = []
# print("\n10-5: Ingresa nombres para el libro de invitados (escribe 'quit' para terminar):")
# while True:
#     name_book = input("Nombre: ")
#     if name_book.lower() == 'quit': break
#     guest_book_entries.append(name_book + '\n')
# Path('guest_book.txt').write_text("".join(guest_book_entries))
# print("10-5: Todos los nombres han sido guardados en 'guest_book.txt'.")

### Ejercicio 10-6. Addition & 10-7. Addition Calculator
# Maneja errores de entrada numérica.
# print("\n10-6 & 10-7: Calculadora de suma (escribe 'q' para salir):")
# while True:
#     num1_str = input("Primer número: ")
#     if num1_str == 'q': break
#     num2_str = input("Segundo número: ")
#     if num2_str == 'q': break
#     try:
#         result = int(num1_str) + int(num2_str)
#         print(f"El resultado es: {result}")
#     except ValueError:
#         print("¡Error! Por favor, ingresa solo números.")

### Ejercicio 10-8. Cats and Dogs
# Lee dos archivos y maneja el error `FileNotFoundError`.
# Se asume que tienes los archivos `cats.txt` y `dogs.txt`.
# # Crea los archivos de prueba para este ejercicio:
# # cats.txt:
# # Felix
# # Garfield
# # Tom
# #
# # dogs.txt:
# # Max
# # Buddy
# # Luna
# print("\n10-8: Leyendo nombres de gatos y perros:")
# filenames_animals = ['cats.txt', 'dogs.txt']
# for filename_animal in filenames_animals:
#     path_animal = Path(filename_animal)
#     try:
#         contents_animal = path_animal.read_text()
#         print(f"\nContenido de {filename_animal}:\n{contents_animal}")
#     except FileNotFoundError:
#         print(f"\nLo siento, el archivo '{filename_animal}' no se encontró.")

### Ejercicio 10-9. Silent Cats and Dogs
# Modifica el ejercicio anterior para que los errores fallen silenciosamente.
# filenames_silent = ['cats.txt', 'missing_dogs.txt'] # Uno que falta.
# print("\n10-9: Lectura silenciosa de archivos:")
# for filename_silent in filenames_silent:
#     path_silent = Path(filename_silent)
#     try:
#         contents_silent = path_silent.read_text()
#         print(f"\nContenido de {filename_silent}:\n{contents_silent}")
#     except FileNotFoundError:
#         pass # Falla silenciosamente.

### Ejercicio 10-10. Common Words
# Cuenta la ocurrencia de palabras en un texto.
# Se asume que tienes un archivo de texto de un libro (ej. `alice.txt`).
# path_book = Path('alice.txt')
# if path_book.exists():
#     contents_book = path_book.read_text(encoding='utf-8').lower()
#     count_the = contents_book.count('the')
#     count_the_space = contents_book.count('the ')
#     print(f"\n10-10: La palabra 'the' aparece {count_the} veces. Con espacio 'the ' aparece {count_the_space} veces.")

### Ejercicio 10-11. Favorite Number & 10-12. Favorite Number Remembered
# Usa `json` para guardar y cargar un número favorito.
# path_fav_num = Path('favorite_number.json')
# if path_fav_num.exists():
#     loaded_number = json.loads(path_fav_num.read_text())
#     print(f"\n10-12: ¡Conozco tu número favorito! Es {loaded_number}.")
# else:
#     number_fav = input("\n10-12: ¿Cuál es tu número favorito? ")
#     Path('favorite_number.json').write_text(json.dumps(int(number_fav)))
#     print("10-12: Tu número ha sido guardado.")

### Ejercicio 10-13. User Dictionary
# Guarda un diccionario de información de usuario en un archivo JSON.
# path_user_dict = Path('user_data.json')
# if path_user_dict.exists():
#     user_data = json.loads(path_user_dict.read_text())
#     print(f"\n10-13: ¡Bienvenido de nuevo, {user_data.get('username', 'usuario')}! Tu perfil: {user_data}.")
# else:
#     username_dict = input("\n10-13: ¿Cuál es tu nombre de usuario? ")
#     full_name_dict = input("10-13: ¿Cuál es tu nombre completo? ")
#     age_dict = int(input("10-13: ¿Cuántos años tienes? "))
#     user_data = {'username': username_dict, 'full_name': full_name_dict, 'age': age_dict}
#     Path('user_data.json').write_text(json.dumps(user_data))
#     print("10-13: Tu información ha sido guardada.")


# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 10 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 10 ===")
print("="*80)

# Importaciones necesarias para los ejercicios de desafío.
from pathlib import Path
import json

# 1. Registro de Actividad Simple:
#    Crea un programa que pida al usuario una actividad y la fecha actual (como string).
#    Guarda esta actividad y fecha en un archivo `log_actividades.txt`, añadiéndola al final.
#    Cada actividad debe estar en una nueva línea.
print("\n1. Registro de Actividad Simple:")
# current_activity = input("¿Qué actividad realizaste hoy? ")
# current_date = "2025-07-01" # Simula la fecha actual.
# log_entry = f"[{current_date}] {current_activity}\n"
# log_path = Path("log_actividades.txt")
# if log_path.exists():
#     existing_content = log_path.read_text()
#     log_path.write_text(existing_content + log_entry)
# else:
#     log_path.write_text(log_entry)
# print(f"Actividad guardada en {log_path}.")


# 2. Visor de Archivo con Control de Errores:
#    Pide al usuario el nombre de un archivo.
#    Intenta leer y mostrar el contenido de ese archivo.
#    Si el archivo no existe, imprime un mensaje amigable.
#    Si el archivo existe pero no se puede leer por alguna razón (ej. permisos, aunque no lo simulemos),
#    imprime un mensaje de error general.
print("\n2. Visor de Archivo con Control de Errores:")
# file_to_view = input("Ingresa el nombre del archivo a ver: ")
# view_path = Path(file_to_view)
# try:
#     content = view_path.read_text(encoding='utf-8')
#     print(f"\n--- Contenido de '{file_to_view}' ---")
#     print(content)
# except FileNotFoundError:
#     print(f"Error: El archivo '{file_to_view}' no se encontró.")
# except Exception as e: # Captura cualquier otro error.
#     print(f"Ocurrió un error al leer el archivo: {e}")


# 3. Conversor de Datos Básicos (Lista a JSON):
#    Crea una lista de strings (ej. nombres de ciudades).
#    Guarda esta lista en un archivo `ciudades.json` en formato JSON.
#    Luego, lee el archivo `ciudades.json` de nuevo y carga la lista en una nueva variable.
#    Imprime la lista cargada.
print("\n3. Conversor de Datos Básicos (Lista a JSON):")
ciudades_original = ["Madrid", "Barcelona", "Valencia", "Sevilla"]
ciudades_json_path = Path("ciudades.json")
# Guarda la lista en JSON.
ciudades_json_path.write_text(json.dumps(ciudades_original))
print("Lista de ciudades guardada en 'ciudades.json'.")
# Lee la lista desde JSON.
ciudades_cargadas = json.loads(ciudades_json_path.read_text())
print(f"Lista de ciudades cargadas: {ciudades_cargadas}")


# 4. Sumador de Números de Archivo:
#    Crea un archivo `numeros_para_sumar.txt` con varios números, uno por línea.
#    Lee este archivo, convierte cada línea a un número entero y suma todos los números.
#    Imprime la suma total. Maneja `FileNotFoundError` y `ValueError` (si una línea no es un número).
print("\n4. Sumador de Números de Archivo:")
# Crea el archivo de prueba (asegúrate de que existe o créalo).
# Path("numeros_para_sumar.txt").write_text("10\n20\n30\ncuarenta\n50")
sum_numbers_path = Path("numeros_para_sumar.txt")
total_sum = 0
try:
    lines = sum_numbers_path.read_text().splitlines()
    for line in lines:
        try:
            total_sum += int(line)
        except ValueError:
            print(f"Advertencia: '{line}' no es un número válido y fue omitido.")
    print(f"La suma total de los números en el archivo es: {total_sum}")
except FileNotFoundError:
    print(f"Error: El archivo '{sum_numbers_path}' no se encontró.")


# 5. Censor de Palabras en Archivo:
#    Crea un archivo `articulo.txt` con un texto.
#    Define una lista de `palabras_prohibidas`.
#    Lee el archivo, reemplaza cada ocurrencia de las palabras prohibidas por "***" (tres asteriscos).
#    Escribe el texto censurado en un nuevo archivo `articulo_censurado.txt`.
print("\n5. Censor de Palabras en Archivo:")
# Crea el archivo de prueba.
# Path("articulo.txt").write_text("Este es un articulo sobre un tema delicado. Evitemos las palabras malas y ofensivas.")
articulo_path = Path("articulo.txt")
palabras_prohibidas = ["malo", "ofensivo", "delicado"]
try:
    content_articulo = articulo_path.read_text().lower() # Leer y convertir a minúsculas.
    for palabra in palabras_prohibidas:
        content_articulo = content_articulo.replace(palabra, "***")
    Path("articulo_censurado.txt").write_text(content_articulo)
    print("Artículo censurado guardado en 'articulo_censurado.txt'.")
except FileNotFoundError:
    print(f"Error: El archivo '{articulo_path}' no se encontró para censurar.")


# 6. Almacenamiento y Carga de Perfil de Usuario (JSON):
#    Crea un programa que pida al usuario su `nombre`, `edad` y `ciudad`.
#    Guarda esta información como un diccionario en un archivo `perfil_usuario.json`.
#    La próxima vez que el programa se ejecute, debe intentar cargar el perfil. Si existe, lo muestra.
#    Si no existe, pide la información y la guarda.
print("\n6. Almacenamiento y Carga de Perfil de Usuario (JSON):")
profile_path = Path("perfil_usuario.json")
user_profile_data = {}
# --- INICIO BLOQUE: Perfil de usuario JSON ---
# if profile_path.exists():
#     try:
#         user_profile_data = json.loads(profile_path.read_text())
#         print(f"\n¡Bienvenido de nuevo, {user_profile_data.get('nombre', 'usuario')}!")
#         print(f"Tu perfil: Nombre: {user_profile_data.get('nombre')}, Edad: {user_profile_data.get('edad')}, Ciudad: {user_profile_data.get('ciudad')}")
#     except json.JSONDecodeError:
#         print("Error: El archivo de perfil está corrupto.")
# else:
#     print("\nCreando nuevo perfil de usuario:")
#     name = input("¿Cuál es tu nombre? ")
#     age = input("¿Cuál es tu edad? ")
#     city = input("¿En qué ciudad vives? ")
#     user_profile_data = {"nombre": name, "edad": age, "ciudad": city}
#     profile_path.write_text(json.dumps(user_profile_data))
#     print("¡Perfil guardado!")
# --- FIN BLOQUE: Perfil de usuario JSON ---


# 7. Contador de Líneas y Palabras en Múltiples Archivos:
#    Dada una lista de nombres de archivos (ej. `["file1.txt", "file2.txt"]`),
#    Para cada archivo, imprime la cantidad de líneas y la cantidad total de palabras.
#    Maneja `FileNotFoundError` para los archivos que no existan.
print("\n7. Contador de Líneas y Palabras en Múltiples Archivos:")
# Crea archivos de prueba:
# file1.txt: "Hola mundo\nEsto es una prueba."
# file2.txt: "Python es genial\nProgramar es divertido."
# missing_file.txt: (no existe)
file_list = ["file1.txt", "file2.txt", "missing_file.txt"]
for f_name in file_list:
    f_path = Path(f_name)
    try:
        content = f_path.read_text(encoding='utf-8')
        lines = content.splitlines()
        words = content.split()
        print(f"\nArchivo '{f_name}':")
        print(f"  - Líneas: {len(lines)}")
        print(f"  - Palabras: {len(words)}")
    except FileNotFoundError:
        print(f"\nArchivo '{f_name}': ¡No encontrado!")


# 8. Registro de Errores Silencioso:
#    Modifica el ejercicio 7.4 (sumador de números de archivo).
#    En lugar de imprimir advertencias en la consola para líneas inválidas,
#    escribe esas líneas inválidas en un archivo `errores_sumador.log` silenciosamente.
#    El programa principal solo debe mostrar la suma final o el error `FileNotFoundError`.
print("\n8. Registro de Errores Silencioso:")
# Sumador de números del ejercicio 4.
# Path("numeros_para_sumar_log.txt").write_text("10\n20\nerror_line\n30\notro error\n50")
sum_log_path = Path("numeros_para_sumar_log.txt")
error_log_path = Path("errores_sumador.log")
total_sum_log = 0
try:
    lines = sum_log_path.read_text().splitlines()
    for line in lines:
        try:
            total_sum_log += int(line)
        except ValueError:
            # Escribe la línea inválida en el log de errores.
            if error_log_path.exists():
                error_log_path.write_text(error_log_path.read_text() + f"Línea inválida: {line}\n")
            else:
                error_log_path.write_text(f"Línea inválida: {line}\n")
            pass # Falla silenciosamente en la consola.
    print(f"La suma total de los números (con log de errores) es: {total_sum_log}")
except FileNotFoundError:
    print(f"Error: El archivo '{sum_log_path}' no se encontró.")
print(f"Revisa '{error_log_path}' para ver los errores registrados.")


# 9. Lector de Última Línea:
#    Dado un archivo de texto, lee y muestra solo la última línea del archivo.
#    Maneja `FileNotFoundError`. Si el archivo está vacío, imprima un mensaje.
print("\n9. Lector de Última Línea:")
# Path("empty_file.txt").write_text("")
# Path("multi_line_file.txt").write_text("Linea 1\nLinea 2\nUltima Linea")
file_to_read_last = "multi_line_file.txt"
try:
    lines = Path(file_to_read_last).read_text().splitlines()
    if lines:
        print(f"La última línea de '{file_to_read_last}' es: '{lines[-1]}'")
    else:
        print(f"El archivo '{file_to_read_last}' está vacío.")
except FileNotFoundError:
    print(f"Error: El archivo '{file_to_read_last}' no se encontró.")


# 10. Agenda de Contactos Básica (JSON):
#     Crea una agenda de contactos donde cada contacto es un diccionario con "nombre", "telefono", "email".
#     La agenda debe ser una lista de estos diccionarios.
#     Guarda y carga la agenda de un archivo `agenda.json`.
#     Permite al usuario añadir un nuevo contacto y luego muestra toda la agenda.
#     (Al inicio del programa, carga la agenda. Si no existe, inicia una vacía).
print("\n10. Agenda de Contactos Básica (JSON):")
agenda_path = Path("agenda.json")
agenda = []
# --- INICIO BLOQUE: Agenda JSON ---
# if agenda_path.exists():
#     try:
#         agenda = json.loads(agenda_path.read_text())
#         print("Agenda cargada exitosamente.")
#     except json.JSONDecodeError:
#         print("Error: El archivo de agenda está corrupto. Iniciando una nueva.")
#     except FileNotFoundError: # Aunque ya se verifica exists(), un doble check.
#         print("Archivo de agenda no encontrado. Iniciando una nueva.")
# else:
#     print("Archivo de agenda no encontrado. Iniciando una nueva.")
#
# print("\nContactos actuales:")
# if agenda:
#     for contact in agenda:
#         print(f"  - {contact.get('nombre')}: Teléfono={contact.get('telefono')}, Email={contact.get('email')}")
# else:
#     print("La agenda está vacía.")
#
# # Añadir un nuevo contacto (simulado).
# add_new = input("¿Deseas añadir un nuevo contacto? (si/no): ")
# if add_new.lower() == 'si':
#     nombre = input("Nombre del contacto: ")
#     telefono = input("Teléfono: ")
#     email = input("Email: ")
#     new_contact = {"nombre": nombre, "telefono": telefono, "email": email}
#     agenda.append(new_contact)
#     agenda_path.write_text(json.dumps(agenda))
#     print("Contacto añadido y agenda guardada.")
#
# print("\nAgenda final:")
# for contact in agenda:
#     print(f"  - {contact.get('nombre')}: Teléfono={contact.get('telefono')}, Email={contact.get('email')}")
# --- FIN BLOQUE: Agenda JSON ---

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 10 ===")
print("="*80 + "\n")

#endregion

#region CAPÍTULO 11: PROBANDO TU CÓDIGO

# ======================================================================================================================
# CAPÍTULO 11: PROBANDO TU CÓDIGO
# ======================================================================================================================
#
# Este capítulo introduce las pruebas unitarias para asegurar que el código funciona como se espera.
#
# Conceptos clave:
# - `pytest`: Una librería externa de Python para escribir y ejecutar tests.
# - `assert`: Una afirmación para verificar si una condición es verdadera.
# - Archivos de prueba: Deben comenzar con `test_`.
# - Funciones de prueba: Deben comenzar con `test_`.
# - Fallo de prueba: Indica un error en el código que se está probando.
# - Fixtures: Funciones que preparan datos para múltiples tests, evitando la repetición de código.
#   - Se definen con `@pytest.fixture`.
#

### Ejemplos de código y conceptos
print("="*80)
print("=== CAPÍTULO 11: CONCEPTOS Y EJEMPLOS ===")
print("="*80)

print("--- 11.1 Instalación de pytest ---")
print("Para instalar `pytest`, usa `pip` en tu terminal: `python -m pip install --user pytest`")

print("\n--- 11.2 Probando una función ---")
# El código de la función y los tests deben estar en archivos separados.
#
# --- INICIO FUNCIÓN: get_formatted_name_test ---
def get_formatted_name_test(first, last, middle=''):
    """Genera un nombre completo bien formateado."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
# --- FIN FUNCIÓN: get_formatted_name_test ---
#
# `test_name_function.py` (Archivo separado para tests):
# # import pytest (necesario si usas fixtures, pero no para asserts simples)
# from name_function import get_formatted_name_test # Asume que la función está en `name_function.py`.
#
# def test_first_last_name():
#     formatted_name = get_formatted_name_test('janis', 'joplin')
#     assert formatted_name == 'Janis Joplin'
# def test_first_last_middle_name():
#     formatted_name = get_formatted_name_test('wolfgang', 'mozart', 'amadeus')
#     assert formatted_name == 'Wolfgang Amadeus Mozart'
#
# Para ejecutar los tests, ve a la terminal en el directorio del proyecto y ejecuta `pytest`.
# (No se ejecuta aquí, solo se muestra el ejemplo de test).
print("Tests de ejemplo de funciones (no ejecutables directamente en este script):")
try:
    test_first_last_name()
    test_first_last_middle_name()
except NameError:
    print("Las funciones de test no están definidas en este alcance. Por favor, crea archivos separados y ejecuta `pytest`.")


print("\n--- 11.3 Probando una clase y fixtures ---")
# El código de la clase `AnonymousSurvey` y sus tests deben estar en archivos separados.
#
# --- INICIO CLASE: AnonymousSurvey ---
class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []
    def store_response(self, new_response):
        self.responses.append(new_response)
# --- FIN CLASE: AnonymousSurvey ---
#
# `test_survey.py` (Archivo separado para tests):
# import pytest
# # from survey import AnonymousSurvey # Asume que la clase está en `survey.py`.
#
# @pytest.fixture
# def language_survey():
#     question = "What language did you first learn to speak?"
#     return AnonymousSurvey(question)
#
# def test_store_single_response(language_survey):
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses
#
# def test_store_three_responses(language_survey):
#     responses = ['English', 'Spanish', 'Mandarin']
#     for response in responses:
#         language_survey.store_response(response)
#     for response in responses:
#         assert response in language_survey.responses
#
# Para ejecutar los tests, ve a la terminal en el directorio del proyecto y ejecuta `pytest test_survey.py`.
print("Tests de ejemplo de clases con fixtures (no ejecutables directamente en este script).")


### Ejercicios de Práctica (TRY IT YOURSELF)
# A continuación se presentan las soluciones a los ejercicios del libro.
print("\n" + "="*80)
print("=== CAPÍTULO 11: EJERCICIOS DE PRÁCTICA (DEL LIBRO) ===")
print("="*80)
print("Para estos ejercicios, debes crear archivos `.py` separados y ejecutar los tests con el comando `pytest` en la terminal.")

### Ejercicio 11-1. City, Country & 11-2. Population
# Crea una función y sus tests. Luego, modifícala para añadir un parámetro opcional.
#
# `city_functions.py`:
# def city_country(city, country, population=None):
#     if population:
#         return f"{city.title()}, {country.title()} - population {population}"
#     else:
#         return f"{city.title()}, {country.title()}"
#
# `test_cities.py`:
# import pytest
# from city_functions import city_country
#
# def test_city_country():
#     santiago_chile = city_country('santiago', 'chile')
#     assert santiago_chile == 'Santiago, Chile'
#
# def test_city_country_population(): # Para 11-2
#     santiago_chile_pop = city_country('santiago', 'chile', population=5000000)
#     assert santiago_chile_pop == 'Santiago, Chile - population 5000000'
print("\n11-1 & 11-2: Revisa las descripciones para crear los archivos `city_functions.py` y `test_cities.py`.")

### Ejercicio 11-3. Employee (con fixture)
# Crea una clase `Employee` y tests para su método `give_raise()`, utilizando fixtures.
#
# `employee.py`:
# class Employee:
#     def __init__(self, first_name, last_name, annual_salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.annual_salary = annual_salary
#     def give_raise(self, amount=5000):
#         self.annual_salary += amount
#
# `test_employee.py`:
# import pytest
# from employee import Employee
#
# @pytest.fixture
# def employee_instance():
#     return Employee("John", "Doe", 50000)
#
# def test_give_default_raise(employee_instance):
#     employee_instance.give_raise()
#     assert employee_instance.annual_salary == 55000
#
# def test_give_custom_raise(employee_instance):
#     employee_instance.give_raise(10000)
#     assert employee_instance.annual_salary == 60000
print("\n11-3: Revisa las descripciones para crear los archivos `employee.py` y `test_employee.py`.")

# === INICIO EJERCICIOS DESAFÍO CAPÍTULO 11 ===
print("\n" + "="*80)
print("=== INICIO EJERCICIOS DESAFÍO CAPÍTULO 11 ===")
print("="*80)

# Nota: Para ejecutar estos ejercicios, necesitarás `pytest` instalado (`pip install pytest`)
# y guardar las funciones y clases a probar en archivos `.py` separados, y los tests
# en archivos `test_*.py` en el mismo directorio. Luego, ejecuta `pytest` desde la terminal.

# 1. Función de Suma con Múltiples Asserts:
#    Crea una función `sumar_numeros(a, b)` que devuelva la suma de dos números.
#    Crea un archivo de test `test_suma.py`.
#    Dentro de `test_suma.py`, escribe una función de test `test_sumar_numeros()`
#    que contenga al menos 3 `assert` diferentes para probar la función con:
#    - Números positivos.
#    - Números negativos.
#    - Cero.
# --- INICIO FUNCIÓN: sumar_numeros (en un archivo: `matematicas.py`) ---
# def sumar_numeros(a, b):
#     return a + b
# --- FIN FUNCIÓN: sumar_numeros ---
#
# --- INICIO TEST: test_suma (en un archivo: `test_suma.py`) ---
# from matematicas import sumar_numeros
# def test_sumar_numeros():
#     assert sumar_numeros(2, 3) == 5
#     assert sumar_numeros(-1, 1) == 0
#     assert sumar_numeros(0, 0) == 0
#     assert sumar_numeros(10, -5) == 5
# --- FIN TEST: test_suma ---
print("\n1. Se describe la estructura para probar la función `sumar_numeros`.")

# 2. Clase Producto con Método de Descuento:
#    Modifica la clase `Producto` del Capítulo 9 para incluir un método `aplicar_descuento(porcentaje)`.
#    Este método debe aplicar un `porcentaje` de descuento al `precio` y actualizarlo.
#    Crea un archivo de test `test_producto.py`.
#    Escribe una función de test `test_aplicar_descuento()` que:
#    - Cree una instancia de `Producto`.
#    - Aplique un descuento.
#    - Use `assert` para verificar si el precio se actualizó correctamente.
# --- INICIO CLASE: Producto (modificada, en un archivo: `tienda.py`) ---
# class Producto:
#     def __init__(self, nombre, precio, stock):
#         self.nombre = nombre
#         self.precio = precio
#         self.stock = stock
#     def aplicar_descuento(self, porcentaje):
#         if 0 <= porcentaje <= 100:
#             self.precio -= self.precio * (porcentaje / 100)
#         else:
#             print("Porcentaje de descuento inválido.")
# --- FIN CLASE: Producto ---
#
# --- INICIO TEST: test_producto (en un archivo: `test_producto.py`) ---
# from tienda import Producto
# def test_aplicar_descuento():
#     camiseta = Producto("Camiseta", 20.00, 50)
#     camiseta.aplicar_descuento(10) # 10% de descuento.
#     assert camiseta.precio == 18.00
#     camiseta_neg = Producto("Pantalon", 30.00, 20)
#     camiseta_neg.aplicar_descuento(-5) # Descuento inválido.
#     assert camiseta_neg.precio == 30.00 # Precio no debería cambiar.
# --- FIN TEST: test_producto ---
print("\n2. Se describe la estructura para probar el método `aplicar_descuento` de la clase `Producto`.")

# 3. Test de Bucle `for` con Lista Vacía:
#    Crea una función `procesar_lista(elementos)` que itere sobre una lista e imprima cada elemento.
#    Crea un archivo de test `test_vacio.py`.
#    Escribe una función de test `test_procesar_lista_vacia()` que pruebe qué ocurre cuando
#    `procesar_lista` recibe una lista vacía. (No debe haber errores, y la salida debe ser nula).
#    Usa `assert` para verificar que no se produzca una excepción.
# --- INICIO FUNCIÓN: procesar_lista (en un archivo: `procesador.py`) ---
# def procesar_lista(elementos):
#     # Esta función no devuelve nada, solo imprime.
#     # El test debe asegurar que no se genere un error si la lista está vacía.
#     for elemento in elementos:
#         print(f"Procesando: {elemento}")
# --- FIN FUNCIÓN: procesar_lista ---
#
# --- INICIO TEST: test_vacio (en un archivo: `test_vacio.py`) ---
# import pytest
# from procesador import procesar_lista
# def test_procesar_lista_vacia():
#     # Se espera que no haya excepciones.
#     procesar_lista([])
#     assert True # Si llegamos aquí sin excepción, el test pasa.
# --- FIN TEST: test_vacio ---
print("\n3. Se describe cómo probar una función que maneja una lista vacía.")

# 4. Prueba de Múltiples Tipos de Datos en Lista (Contador):
#    Crea una función `contar_tipos(lista)` que devuelva un diccionario con el conteo de tipos de datos.
#    Ej: `[1, "hola", 2.5, "mundo"]` -> `{"int": 1, "str": 2, "float": 1}`.
#    Crea un test para esta función usando `assert` en el diccionario retornado.
# --- INICIO FUNCIÓN: contar_tipos (en un archivo: `analizador.py`) ---
# def contar_tipos(lista):
#     conteo = {}
#     for elemento in lista:
#         tipo = type(elemento).__name__ # Obtiene el nombre del tipo como string.
#         conteo[tipo] = conteo.get(tipo, 0) + 1
#     return conteo
# --- FIN FUNCIÓN: contar_tipos ---
#
# --- INICIO TEST: test_tipos (en un archivo: `test_tipos.py`) ---
# from analizador import contar_tipos
# def test_contar_tipos_mixta():
#     mixed_list = [1, "hello", 2.0, True, "world", 5]
#     expected_counts = {"int": 2, "str": 2, "float": 1, "bool": 1} # True es un bool
#     assert contar_tipos(mixed_list) == expected_counts
# --- FIN TEST: test_tipos ---
print("\n4. Se describe cómo probar una función que cuenta tipos de datos en una lista.")

# 5. Prueba de Formateo de String con Caracteres Especiales:
#    Crea una función `limpiar_texto(texto)` que:
#    - Elimine espacios extra al inicio y final.
#    - Convierta el texto a minúsculas.
#    - Reemplace "badword" con "***".
#    Crea un test con varios `assert` para diferentes casos.
# --- INICIO FUNCIÓN: limpiar_texto (en un archivo: `utilidades.py`) ---
# def limpiar_texto(texto):
#     texto_limpio = texto.strip().lower()
#     texto_limpio = texto_limpio.replace("badword", "***")
#     return texto_limpio
# --- FIN FUNCIÓN: limpiar_texto ---
#
# --- INICIO TEST: test_limpieza_texto (en un archivo: `test_utilidades.py`) ---
# from utilidades import limpiar_texto
# def test_limpiar_texto():
#     assert limpiar_texto("  HOLA MUNDO  ") == "hola mundo"
#     assert limpiar_texto("Texto con BADWORD ") == "texto con ***"
#     assert limpiar_texto("  Otro caso  ") == "otro caso"
# --- FIN TEST: test_limpieza_texto ---
print("\n5. Se describe cómo probar una función de limpieza de texto.")

# 6. Clase Usuario con Prueba de Saludo:
#    Usa la clase `User` del Capítulo 9.
#    Crea un archivo de test `test_user_greeting.py`.
#    Escribe una función de test que:
#    - Cree una instancia de `User`.
#    - Capture la salida del método `greet_user()` (Tendrás que buscar cómo hacerlo para tests. Pista: `capsys`).
#    - Use `assert` para verificar que el saludo es el esperado.
# --- INICIO CLASE: User (asumida desde Capítulo 9, en un archivo: `usuario.py`) ---
# class User:
#     def __init__(self, first_name, last_name, age, city):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.city = city
#     def greet_user(self):
#         print(f"Hello, {self.first_name.title()}! Welcome back.")
# --- FIN CLASE: User ---
#
# --- INICIO TEST: test_user_greeting (en un archivo: `test_user_greeting.py`) ---
# import pytest
# from usuario import User
# def test_greet_user_output(capsys):
#     user = User("alice", "smith", 28, "nyc")
#     user.greet_user()
#     captured = capsys.readouterr()
#     assert "Hello, Alice! Welcome back.\n" == captured.out
# --- FIN TEST: test_user_greeting ---
print("\n6. Se describe cómo probar la salida de una función de usuario.")

# 7. Prueba de Ordenamiento de Lista Numérica:
#    Crea una función `ordenar_numeros(lista)` que devuelva la lista ordenada de forma ascendente.
#    Crea un test para verificar que la función ordena correctamente, incluyendo listas con números repetidos.
# --- INICIO FUNCIÓN: ordenar_numeros (en un archivo: `ordenador.py`) ---
# def ordenar_numeros(lista):
#     return sorted(lista)
# --- FIN FUNCIÓN: ordenar_numeros ---
#
# --- INICIO TEST: test_ordenamiento (en un archivo: `test_ordenamiento.py`) ---
# from ordenador import ordenar_numeros
# def test_ordenar_numeros_ascendente():
#     assert ordenar_numeros([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]
#     assert ordenar_numeros([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
#     assert ordenar_numeros([]) == []
# --- FIN TEST: test_ordenamiento ---
print("\n7. Se describe cómo probar una función de ordenamiento numérico.")

# 8. Prueba de Tupla de Dimensiones (Inmutabilidad):
#    Crea una función `crear_dimensiones(ancho, alto)` que devuelva una tupla (ancho, alto).
#    Crea un test que:
#    - Cree una tupla usando la función.
#    - Intente modificar un elemento de la tupla (debería fallar, pero el test no debe romperse).
#    - Use `assert` para verificar que la tupla original no cambió.
# --- INICIO FUNCIÓN: crear_dimensiones (en un archivo: `formas.py`) ---
# def crear_dimensiones(ancho, alto):
#     return (ancho, alto)
# --- FIN FUNCIÓN: crear_dimensiones ---
#
# --- INICIO TEST: test_tupla_inmutable (en un archivo: `test_formas.py`) ---
# from formas import crear_dimensiones
# def test_tupla_inmutabilidad():
#     dims = crear_dimensiones(100, 200)
#     # Intento de modificación que causaría un TypeError si se descomenta:
#     # try:
#     #     dims[0] = 150
#     # except TypeError:
#     #     pass # Esperado
#     assert dims == (100, 200) # La tupla no debería haber cambiado.
# --- FIN TEST: test_tupla_inmutable ---
print("\n8. Se describe cómo probar la inmutabilidad de las tuplas.")

# 9. Verificación de Límite Numérico:
#    Crea una función `esta_en_rango(numero, limite_inferior, limite_superior)` que
#    devuelva `True` si el número está dentro del rango (inclusive), `False` de lo contrario.
#    Escribe tests para casos en el límite, dentro y fuera del rango.
# --- INICIO FUNCIÓN: esta_en_rango (en un archivo: `validaciones.py`) ---
# def esta_en_rango(numero, limite_inferior, limite_superior):
#     return limite_inferior <= numero <= limite_superior
# --- FIN FUNCIÓN: esta_en_rango ---
#
# --- INICIO TEST: test_rango (en un archivo: `test_validaciones.py`) ---
# from validaciones import esta_en_rango
# def test_esta_en_rango():
#     assert esta_en_rango(5, 1, 10) == True
#     assert esta_en_rango(1, 1, 10) == True
#     assert esta_en_rango(10, 1, 10) == True
#     assert esta_en_rango(0, 1, 10) == False
#     assert esta_en_rango(11, 1, 10) == False
# --- FIN TEST: test_rango ---
print("\n9. Se describe cómo probar si un número está dentro de un rango.")

# 10. Prueba de la Clase `Restaurant` (Método `open_restaurant`):
#     Usa la clase `Restaurant` del Capítulo 9.
#     Crea un archivo de test `test_restaurant_status.py`.
#     Escribe una función de test que:
#     - Cree una instancia de `Restaurant`.
#     - Capture la salida del método `open_restaurant()`.
#     - Use `assert` para verificar que el mensaje de "abierto" es correcto.
# --- INICIO CLASE: Restaurant (asumida desde Capítulo 9, en un archivo: `restaurante.py`) ---
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def open_restaurant(self):
#         print(f"¡El restaurante {self.restaurant_name} está abierto!")
# --- FIN CLASE: Restaurant ---
#
# --- INICIO TEST: test_restaurant_status (en un archivo: `test_restaurant_status.py`) ---
# import pytest
# from restaurante import Restaurant
# def test_open_restaurant_message(capsys):
#     mi_restaurante = Restaurant("Mi Rincón", "Mexicana")
#     mi_restaurante.open_restaurant()
#     captured = capsys.readouterr()
#     assert "¡El restaurante Mi Rincón está abierto!\n" == captured.out
# --- FIN TEST: test_restaurant_status ---
print("\n10. Se describe cómo probar el mensaje de apertura de un restaurante.")

print("\n" + "="*80)
print("=== FIN EJERCICIOS DESAFÍO CAPÍTULO 11 ===")
print("="*80 + "\n")

#endregion

#region GUÍA DEL CURSO DE PYTHON: CONCLUSIÓN

# ======================================================================================================================
# FIN DE LA GUÍA
# ======================================================================================================================
#
# Esta guía es un punto de partida para tu aprendizaje. ¡Sigue practicando y construyendo proyectos!
# ¡Feliz programación!
#
# NOTA: Los capítulos siguientes (12-20) del libro se enfocan en proyectos prácticos más avanzados
# como juegos, visualización de datos y aplicaciones web. Te animo a seguir explorándolos.
#
#endregion


