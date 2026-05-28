# BehaviorTracker - Análisis de Patrones de Uso de Aplicaciones Móviles

## Descripción del Repositorio
Este repositorio contiene el sistema desarrollado para el proyecto **BehaviorTracker** (Bloque 1).  
El objetivo es procesar y analizar datos reales de uso de aplicaciones móviles para estudiar patrones de comportamiento digital.

El sistema permite:
- Leer y estructurar datos desde un archivo CSV
- Filtrar información por participante
- Calcular métricas básicas de uso (tiempo total y promedio)
- Agrupar el uso por aplicación

## Objetivo del Proyecto
Desarrollar un sistema modular en Python que:
- Lea datos de uso de aplicaciones móviles
- Organice la información por participante
- Calcule métricas básicas de comportamiento digital
- Facilite el análisis de cómo el entorno (notificaciones, etc.) influye en el uso de apps


## Integrantes del Grupo
- Sofia Jalil Bestard
- Guadalupe Merke
- Miranda Berazategui

## Cómo ejecutar el programa
1. Colocar el archivo de datos en la carpeta `datos/`
2. Ejecutar `main.py`
3. El programa cargará los datos, los procesará y mostrará las métricas calculadas

## Funciones implementadas
- `cargar_datos()` y `parsear_linea()` → Lectura y estructuración de datos
- `filtrar_por_participante()` → Filtrado por participante
- `calcular_tiempo_total()` → Tiempo total de uso
- `calcular_promedio_uso()` → Promedio de uso
- `calcular_uso_por_app()` → Uso por aplicación (opcional)

## Posible implementacion con pandas
Esto se lograría modificando principalmente la función cargar_datos() (y eliminando o simplificando la función pasear_linea()) del archivo carga_datos.py. En lugar de abrir manualmente el archivo con open(), leer línea por línea y parsear manualmente cada registro (con split, validaciones manuales y construcción de diccionarios agrupados por participante), se utilizaría pandas.read_csv() para cargar los datos directamente en un DataFrame.
Se podría agrupar el DataFrame por la columna id_participante para mantener una estructura compatible con el resto del sistema (lista de diccionarios con listas internas)

Funciones que se deberían modificar:

- cargar_datos() (principalmente) y pasear_linea() en carga_datos.py.
- Posibles ajustes en filtrar_por_participante(), validar_registro() y las funciones de métricas (calcular_tiempo_total(), calcular_promedio_uso(), calcular_uso_por_app()) para aprovechar las opciones de Pandas (groupby, sum, mean, etc.) y mejorar el rendimiento y la validación de datos.

## Objetos

**Clase Registro:**
- Representa una fila del CSV
- Atributos: `id_participante`, `fecha`, `app`, `cantidad_uso`, `tiempo_uso`
- Métodos: mostrar registro, validar registro, obtener tiempo de uso

**Clase Participante:**
- Representa un participante y sus registros
- Atributos: `id_participante`, `registros`
- Métodos: agregar registro, calcular tiempo total, calcular promedio, calcular uso por app

**Sistema general:**
- Representa al sistema
- Atributos: `datos`, `participantes`
- Métodos: cargar datos, filtrar por participante, validar, métricas
Métodos: cargar datos, filtrar por participante, validar, métricas
  

