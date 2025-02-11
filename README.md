# Script-Python-Planetas

Este repositorio contiene un script en Python diseñado para generar dinámicamente datos de planetas ficticios y almacenarlos en un archivo CSV. Este script forma parte de la solución al desafío "Explorador de Planetas", donde la información generada es utilizada por una aplicación full-stack para visualizar, analizar y almacenar los datos de los planetas en una base de datos SQL.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Integración con la Aplicación Full-Stack](#integración-con-la-aplicación-full-stack)

- [Licencia](#licencia)

## Descripción

El script en Python genera datos planetarios de forma aleatoria, incluyendo las características básicas solicitadas en la consigna:
- **Temperatura**
- **Gravedad**
- **Composición**
- **Habitabilidad**

Además, se pueden agregar atributos adicionales de forma creativa para enriquecer la información. Los datos se guardan en un archivo CSV, el cual es posteriormente utilizado por la aplicación full-stack para cargar los planetas en una base de datos (por ejemplo, mediante un endpoint POST que parsea el CSV y utiliza Prisma para insertar los registros).

## Características

- **Generación Aleatoria de Datos:** Cada ejecución del script produce un conjunto único de planetas con datos variados.
- **Formato CSV:** Los datos generados se exportan a un archivo CSV, facilitando su posterior ingestión en otros sistemas.
- **Configurabilidad:** Posibilidad de ajustar el número de planetas y otros parámetros (según implementaciones futuras o personalizaciones).
- **Fácil Integración:** El archivo CSV generado se utiliza como fuente de datos para la aplicación full-stack en el repositorio [Explorador-de-Planetas-App](https://github.com/SebasBarrientos/Explorador-de-Planetas-App).

## Requisitos

- Python 3.7 o superior
- Las dependencias se pueden instalar mediante `pip` (se recomienda utilizar un entorno virtual).

## Instalación y uso

1. **Clona el repositorio y ejecuta la funcion con Python**

   ```bash
   git clone https://github.com/SebasBarrientos/Script-Python-Planetas.git
   cd Script-Python-Planetas
   pip install psycopg2-binary python-dotenv faker                                                                          
   py .\planetListCSV.py
