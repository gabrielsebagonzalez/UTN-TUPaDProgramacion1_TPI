import csv
import os
import unicodedata


def menu():
#Esta función muestra el menú interactivo del sistema y permite al usuario seleccionar distintas operaciones.
#Cada opción llama a una función específica.
    op = "0"
    opciones = [
        "\n╔═════════════════════════════════════════════╗",
        "║ TRABAJO PRACTICO INTEGRADOR PROGRAMACIÓN 1  ║",
        "╚═════════════════════════════════════════════╝\n",
        "┌─────────────────────────────────────────────┐",
        "│             GESTIÓN DE PAISES               │",
        "└─────────────────────────────────────────────┘\n",
        "---------------MENÚ DE OPCIONES----------------\n",
        "1). Agregar país.",
        "2). Actualizar país.",
        "3). Buscar país.",
        "4). Filtrar país.",
        "5). Ordenar pais.",
        "6). Mostrar estadísticas.",
        "7). Salir.",
        ]

    while op != "7":
        for items in opciones:
            print(items)
        op = input("\nIngrese una opción: ")

        match op:
            case "1":
                agregar_pais()
            case "2":
                actualizar_datos()
            case "3":
                buscar_paises()
            case "4":
                filtrar_paises()
            case "5":
                ordenar_paises()
            case "6":
                mostrar_estadisticas()
            case "7":
                print("¡Muchas gracias. Vuelva pronto!")
            case _:
                print("Debes ingresar una opción valida")

def obtener_paises():

#Lee el archivo 'paises.csv' y devuelve una lista de diccionarios,donde cada país se representa con nombre, población, superficie y continente.
# Si el archivo no existe, lo crea con los encabezados correspondientes.

    paises = []
    if not os.path.exists("paises.csv"):
        with open("paises.csv", "w", newline="", encoding="utf-8")as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            escritor.writeheader()
            return paises
        
    with open("paises.csv", "r", newline="", encoding="utf-8")as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            paises.append({"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"]})
        return paises

def agregar_pais():
# Permite registrar un país nuevo en el archivo CSV.
# Valida que el nombre sea correcto, que no esté vacío ni duplicado, y que población y superficie sean números válidos.

    while True:
            nuevo_pais = input(f"Ingrese el nombre del país que desea registrar: ").strip().capitalize()

            if not nuevo_pais:
                print("\n*El nombre no puede estar vacío.*")
                continue

            if not validar_nombre(nuevo_pais):
                print("\n*Debe ingresar un nombre valido*")
                continue

            if existe_pais(nuevo_pais):
                print("*\nEl páis ingresado ya se encuentra registrado.*")
                continue
        
            poblacion = input(f"Ingrese la cantidad de habitantes de {nuevo_pais}: ").strip()

            while not validar_numero(poblacion):
                print("\n*La cantidad ingresada no es válido*")
                poblacion = input(f"Ingrese la cantidad de habitantes de {nuevo_pais}: ").strip()
            
            superficie = input(f"Ingrese la superficie en km² de {nuevo_pais}: ").strip()

            while not validar_numero(superficie):
                print("\n*La superficie ingresada no es válida*")
                superficie = input(f"Ingrese la superficie en km² de {nuevo_pais}: ").strip()

            continente = input(f"Ingrese el continente al que pertenece {nuevo_pais}: ").strip().capitalize()

            if not validar_nombre(continente):
                print("\n*Debe ingresar un nombre valido*")
                continue

            agregar_pais_validado({"nombre": nuevo_pais, "poblacion": int(poblacion), "superficie": (superficie), "continente": continente})
            print("País agregado correctamente")
            break

def existe_pais(pais_agregado):
# Verifica si un país ya está registrado en el CSV.
# Compara nombres normalizados para evitar duplicados con o sin tildes y mayúsculas.
    
    paises = obtener_paises()
    for pais in paises:
        if normalizar_texto(pais_agregado) == normalizar_texto(pais["nombre"]):
            return True
    return False

def validar_numero(numero):
# Comprueba que el texto ingresado contenga únicamente dígitos, enteros positivos, evitando valores vacíos o no numéricos

    if not numero.isdigit():
        return False

    return True 

def agregar_pais_validado(pais):
#Esta función recibe un diccionario con los datos de un país que ya fueron validados previamente y los escribe en el archivo csv

    with open("paises.csv", "a", newline="", encoding="utf-8")as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writerow(pais)

def validar_nombre(nombre):
# Esta función comprueba que el texto ingresado sea un nombre válido.
# Elimina los espacios y verifica que solo contenga caracteres alfabéticos.
    return nombre.replace(" ", "").isalpha()

def actualizar_datos():
    
# Permite modificar la población o superficie de un país registrado.
# Usa normalización para que el usuario pueda escribir el nombre con o sin tildes y aún así encontrarlo.

    paises = obtener_paises()

    print("\n----- Actualización de datos de países registrados -----")
    for pais in paises:
        print(f" - País: {pais['nombre']}")

    while True:
        pais_seleccionado = input("\nIngresa el nombre del país que desea actualizar: ").strip()
        if not pais_seleccionado:
            print("*El nombre no puede estar vacío.*")
            continue
        if not existe_pais(pais_seleccionado):
            print("*El país ingresado no se encuentra registrado.*")
            continue
        break

    for pais in paises:
        if normalizar_texto(pais["nombre"]) == normalizar_texto(pais_seleccionado):
            while True:
                opcion = input("Ingrese [P] para actualizar población | [S] para superficie: ").strip().upper()
                if not validar_opcion(opcion):
                    print("*Debes ingresar 'P' o 'S'.*")
                    continue
                break

            if opcion == "P":
                poblacion = input(f"Ingrese la cantidad de habitantes de {pais_seleccionado}: ").strip()
                while not validar_numero(poblacion):
                    print("\n*La cantidad ingresada no es válida*")
                    poblacion = input(f"Ingrese la cantidad de habitantes de {pais_seleccionado}: ").strip()
                pais["poblacion"] = int(poblacion)
                guardar_datos_actualizados(paises)
                print(f"\n- Población de {pais_seleccionado} actualizada exitosamente -")

            elif opcion == "S":
                superficie = input(f"Ingrese la superficie en km² de {pais_seleccionado}: ").strip()
                while not validar_numero(superficie):
                    print("\n*La superficie ingresada no es válida*")
                    superficie = input(f"Ingrese la superficie en km² de {pais_seleccionado}: ").strip()
                pais["superficie"] = int(superficie)
                guardar_datos_actualizados(paises)
                print(f"\n- Superficie de {pais_seleccionado} actualizada exitosamente -")

def mostrar_paises(paises):
# Presenta en pantalla todos los países disponibles con sus atributos
    if not paises:
        print("\n*** No hay información de países disponibles ***")
    else:
        print("\n--- Registro Geográfico ---")
        for pais in paises:
            print(f"País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")

def validar_opcion(opcion):
# Verifica que la opción ingresada por el usuario sea válida para la actualización
# de datos de un país. Acepta únicamente 'P' (población) o 'S' (superficie)

    if not opcion.isalpha():
        return False
    return opcion.upper() in ["P", "S"]

def guardar_datos_actualizados(paises):
#Guarda en 'paises.csv' la lista completa de países (con los cambios realizados).
    with open("paises.csv", "w", newline="", encoding="utf-8")as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion","superficie","continente"])
        escritor.writeheader()
        escritor.writerows(paises)

def buscar_paises():
# Realiza una búsqueda exacta o parcial de países por nombre.
# Devuelve una lista de coincidencias y muestra sus atributos.
    
    paises = obtener_paises()
    nombre_buscado = input("\nIngrese el nombre del país que desea buscar: ").strip()
    
    # Normalizamos el texto ingresado
    nombre_buscado = normalizar_texto(nombre_buscado)

    resultados = []
    for pais in paises:
        # Normalizamos también el nombre del país en el CSV
        if nombre_buscado in normalizar_texto(pais["nombre"]):
            resultados.append(pais)

    if resultados:
        print("\n--- Resultados de la búsqueda ---\n")
        for pais in resultados:
            print(f"País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")
    else:
        print(f"\n*** No se encontraron coincidencias para '{nombre_buscado}' ***")

def normalizar_texto(texto):
#Con esta función normalizamos el texto para filtrar paises, se pasa a minúscula se normaliza y se eliminan las tildes
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto

def obtener_numero(mensaje):
    while True:
        numero = input(mensaje).strip()
        if validar_numero(numero):
            return int(numero)
        else:
            print("Por favor, ingrese un número válido.")


def filtrar_paises():
    paises = obtener_paises()

    op = "0"
    opciones = [
        "\nSeleccione la opción de filtrado",
        "1) Por continente",
        "2) Por rango de población",
        "3) Por rango de superficie",
        "4) Volver al menú principal"
    ]

    while op != "4":
        for item in opciones:
            print(item)
        op = input("\nIngrese una opción: ")

        match op:
            case "1":
                continente = normalizar_texto(input("Ingrese el continente: ").strip()) 
                paises_filtrados = [pais for pais in paises if normalizar_texto(pais["continente"].strip()) == continente]
                mostrar_paises(paises_filtrados)
            case "2":
                min_poblacion = obtener_numero("Ingrese la población mínima: ")
                max_poblacion = obtener_numero("Ingrese la población máxima: ")
                paises_filtrados = [pais for pais in paises if min_poblacion <= pais["poblacion"] <= max_poblacion]
                mostrar_paises(paises_filtrados)
            case "3":
                min_superficie = obtener_numero("Ingrese la superficie mínima: ")
                max_superficie = obtener_numero("Ingrese la superficie máxima: ")
                paises_filtrados = [pais for pais in paises if min_superficie <= pais["superficie"] <= max_superficie]
                mostrar_paises(paises_filtrados)
            case "4":
                print("Volviendo al menú principal...")
                return
            case _:
                print("Opción inválida. Intente nuevamente")


def obtener_nombre(pais):
    return pais["nombre"].lower()

def obtener_poblacion(pais):
    return pais["poblacion"]

def obtener_superficie(pais):
    return pais["superficie"]


def ordenar_paises():
    """Permite al usuario ordenar la lista de paises según diferentes criterios"""
    paises = obtener_paises()

    if not paises:
        print("\n*** No hay información de países disponibles para ordenar ***")
        return
    
    opciones = [
        "\nSeleccione una opción de ordenación: ",
        "1) Por nombre",
        "2) Por población",
        "3) Por superficie",
        "4) Volver al menú principal"
    ]

    op = "0"
    while op != "4":
        for item in opciones:
            print(item)
        op = input("\nIngrese una opción: ")

        match op:
            case "1":
                paises_ordenados = ordenar_burbuja(paises, key=obtener_nombre)
                mostrar_paises(paises_ordenados)
            case "2":
                paises_ordenados = ordenar_burbuja(paises, key=obtener_poblacion)
                mostrar_paises(paises_ordenados)
            case "3":
                orden = input("¿Desea ordenar por superficie en orden (A)scendente o (D)escendente?: ").strip().upper()
                if orden not in ["A", "D"]:
                    print("Opción inválida. Debe ingresar 'A' para ascendente o 'D' para descendente: ")
                    continue

                paises_ordenados = ordenar_burbuja(paises, key=obtener_superficie)

                if orden == "D":
                    paises_ordenados.reverse()
                mostrar_paises(paises_ordenados)

            case "4":
                print("\nVolviendo al menú principal...")
                return
            case _:
                print("Opción inválida. Intente nuevamente")


def ordenar_burbuja(paises, key):
    """Ordena la lista de paises utilizando el algoritmo de ordenamiento burbuja"""
    n = len(paises)
    for i in range(n):
        for j in range(0, n-i-1):
            if key(paises[j]) > key(paises[j + 1]):
                paises[j], paises[j + 1] = paises[j + 1], paises[j]
    return paises


def mostrar_estadisticas():
    """Muestra estadísticas sobre la población y superficie de los paises"""
    paises = obtener_paises()

    if not paises:
        print("\nNo hay información de países disponibles para mostrar estadísticas.")
        return
    
    #Calcula la población y superficie total  
    total_poblacion = sum(obtener_poblacion(pais) for pais in paises)
    total_superficie = sum(obtener_superficie(pais) for pais in paises)

    #Calcula los promedios
    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    #Encuentra el país con mayor y menor población
    pais_mayor_poblacion = max(paises, key=obtener_poblacion)
    pais_menor_poblacion = min(paises, key=obtener_poblacion)

    #Contar paises por continente
    contador_continentes = {}
    for pais in paises:
        continente = pais["continente"]
        #Incrementa el contador para el continente correspondiente
        if continente in contador_continentes:
            contador_continentes[continente] += 1
        else:
            contador_continentes[continente] = 1
    
    while True:
        print("\n***** Menú de estadísticas *****")
        print("Seleccione una opción")
        print("1) País con mayor población")
        print("2) País con menor población")
        print("3) Promedio de población")
        print("4) Promedio de superficie")
        print("5) Cantidad de países por continente")
        print("6) Volver al menú principal")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1":
                print(f"País con mayor población: {pais_mayor_poblacion["nombre"]} ({pais_mayor_poblacion["poblacion"]} habitantes)")
            case "2":
                print(f"País con menor población: {pais_menor_poblacion["nombre"]} ({pais_menor_poblacion["poblacion"]} habitantes)")
            case "3":
                print(f"Promedio de población: {promedio_poblacion:.2f} habitantes")
            case "4":
                print(f"Promedio de superficie: {promedio_superficie:.2f} km²")
            case "5":
                print("\nCantidad de países por continente.")
                for continente, cantidad in contador_continentes.items():
                    print(f"{continente}: {cantidad} países")
            case "6":
                print("Volviendo al menú principal...")
                return
            case _:
                print("Opción inválida. Intente nuevamente")


if __name__ == "__main__":
    menu()