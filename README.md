# 📘 Gestión de Datos de Países en Python

**Trabajo Práctico Integrador - Programación 1**

## 🏛 Datos de la Universidad y la Cátedra

- **Universidad:** Universidad Tecnológica Nacional
- **Carrera:** Tecnicatura Universitaria en Programación (A distancia)
- **Cátedra:** Programación 1
- **Año:** 2025

## 👨‍💻 Integrantes

- **Nombre y Apellido:** Mauricio Gabriel Guzmán
- **Nombre y Apellido:** Gabriel Sebastián González
- **Comisión:** Ag25-1C-06

## 👩‍🏫 Datos de profesores

- **Coordinador:** Alberto Cortéz
- **Docente Titular:** Sebastián Bruselario
- **Docente Tutor/a:** Flor Camila Gubiotti

## 📄 Descripción del proyecto

El proyecto consiste en desarrollar una **aplicación en Python** para gestionar información sobre **países** a partir de un archivo CSV.
Permite realizar operaciones de **agregar, actualizar, búsqueda, filtrado, ordenamiento y cálculo de estadísticas**, aplicando los conceptos de la cursada: listas, diccionarios, funciones, condicionales, bucles y manejo de archivos CSV.
El objetivo principal es afianzar el uso de estructuras de datos y la modularización del código con funciones de una sola responsabilidad.

## 🧱Estructura del proyecto

```
📂 UTN-TUPaDProgramacion1_TPI/
├── TPI.py → Programa principal con el menú y las opciones
├── paises.csv → Archivo CSV con los datos base de los países
├── image.png → Archivo de imágenes
└── README.md → Documento descriptivo del proyecto (este archivo)
```

## ⚙ Instrucciones de ejecución

1. Clonar o descargar el repositorio
   bash
   git clone https://github.com/gabrielsebagonzalez/UTN-TUPaDProgramacion1_TPI.git
   cd UTN-TUPaDProgramacion1_TPI

2. Ejecutar el programa
   python TPI.py

3. Seguir el menú en consola para realizar operaciones: agregar país, actualizar, buscar filtrar, ordenar y ver estadísticas.

El código está desarrollado usando solo librerías estándar de Python (csv, os, math, etc.)

## 🔗Links

- **Enlace al video:**

## 🔁 Ejemplos de entradas y salidas

En este ejemplo, el usuario selecciona la opción 6 (Mostrar estadísticas) desde el menú principal, y luego elige la subopción 5 (Cantidad de países por continente) dentro del menú de estadísticas.
El sistema procesa los datos cargados desde el archivo CSV y muestra cuántos países hay en cada continente.

```
╔═════════════════════════════════════════════╗
║ TRABAJO PRACTICO INTEGRADOR PROGRAMACIÓN 1  ║
╚═════════════════════════════════════════════╝

┌─────────────────────────────────────────────┐
│             GESTIÓN DE PAISES               │
└─────────────────────────────────────────────┘

---------------MENÚ DE OPCIONES----------------

1). Agregar país.
2). Actualizar país.
3). Buscar país.
4). Filtrar país.
5). Ordenar pais.
6). Mostrar estadísticas.
7). Salir.

Ingrese una opción: 6

***** Menú de estadísticas *****
Seleccione una opción
1) País con mayor población
2) País con menor población
3) Promedio de población
4) Promedio de superficie
5) Cantidad de países por continente
6) Volver al menú principal
Ingrese una opción: 5

Cantidad de países por continente.
Asia: 38 países
Europa: 39 países
África: 47 países
América: 29 países
Oceanía: 11 países
```

## 👥 Participación de los integrantes

- **Mauricio Gabriel Guzmán**:
  Se encargó del **diseño inicial del programa** e implementó el **desarrollo de los tres primeros puntos del trabajo práctico**, que incluyen:

  - Agregar un país con todos los datos necesarios para almacenarse (sin campos vacíos).
  - Actualizar los datos de población y superficie de un país.
  - Buscar un país por nombre (coincidencia parcial o exacta).  
    Además, realizó pruebas de validación de entrada y colaboró en la estructura general del código y **marco teórico (PDF)**.

- **Gabriel Sebastián González**:  
  Implementó los **tres últimos puntos del trabajo práctico**, desarrollando las funciones de:
  - Filtrar países por continente, rango de población o superficie.
  - Ordenar países por nombre, población o superficie (ascendente o descendente).
  - Mostrar estadísticas generales (mayor y menor población, promedios y cantidad de países por continente).  
    También se ocupó de la **documentación del proyecto (README.md)**.
