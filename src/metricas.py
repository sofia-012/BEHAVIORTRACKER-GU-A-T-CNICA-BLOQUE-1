import pandas as pd
import os

def calcular_tiempo_total(datos):
    '''
    Calcula la suma total del tiempo de uso de todos los registros.

    Parameters
    ----------
    datos : list
        Lista de diccionarios con los registros del archivo CSV

    Returns
    -------
    total : float
        Tiempo total de uso (en minutos)

    '''
    
    if len(datos) == 0:
        print("Error: La base de datos está vacía | Ubicación: calcular_tiempo_total")
        raise ValueError("La base de datos está vacía")
    
    try:

        tiempos = []
        for dato in datos:
            tiempos.extend(dato["tiempo_uso"])
        
        df_tiempos = pd.Series(tiempos)        
        
        
        if (df_tiempos < 0).any():
            print("Error: la variable tiempo no debe ser negativa | Ubicación: calcular_tiempo_total")
            raise ValueError("la variable tiempo no debe ser negativa")
        
        total = df_tiempos.sum()                 
        return total
    
    except (KeyError, TypeError, AttributeError):
        print("Error: Datos inválidos para calcular tiempo total | Ubicación: calcular_tiempo_total")
        raise
    
def calcular_promedio_uso(datos):
    '''
    Calcula el promedio de tiempo de uso de los registros.

    Parameters
    ----------
    datos : list
        Lista de diccionarios con los registros del archivo CSV

    Returns
    -------
    promedio : float
        Promedio de tiempo de uso por registro

    '''
    if len(datos) == 0:
        print("Error: La base de datos está vacía | Ubicación: calcular_promedio_uso")
        raise ValueError("La base de datos está vacía")
    
    try:
        tiempos = []
        for dato in datos:
            tiempos.extend(dato["tiempo_uso"])
        
        if not tiempos:
            raise ZeroDivisionError("No hay registros válidos")
        
        df_tiempos = pd.Series(tiempos)
        
        # Validaciones vectorizadas
        if not pd.api.types.is_numeric_dtype(df_tiempos):
            print("Error: Valor no numérico en tiempo_uso | Ubicación: calcular_promedio_uso")
            raise TypeError("Valor no numérico en tiempo_uso")
        if (df_tiempos < 0).any():
            print("Error: Valor negativo en tiempo_uso (no permitido) | Ubicación: calcular_promedio_uso")
            raise ValueError("Valor negativo en tiempo_uso")
        
        promedio = df_tiempos.mean()   
        return promedio
    
    except ZeroDivisionError:
        print("Error: No hay registros válidos para calcular el promedio | Ubicación: calcular_promedio_uso")
        raise
    except (TypeError, ValueError, KeyError):
        print("Error: Datos inválidos para calcular el promedio (tipo o valor incorrecto) | Ubicación: calcular_promedio_uso")
        raise

def calcular_uso_por_app(datos):
    '''
    Calcula el tiempo total de uso agrupado por cada aplicación.

    Parameters
    ----------
    datos : list
        Lista de diccionarios con los registros del archivo CSV

    Returns
    -------
    diccionario : dict
        Diccionario con el formato {"nombre_app": tiempo_total}

    '''
    if not datos:
        print("Error: la base de datos está vacía | Ubicación: calcular_uso_por_app")
        return {}
    
    try:
        apps = []
        tiempos = []
        for dato in datos:
            apps.extend(dato['app'])
            tiempos.extend(dato['tiempo_uso'])
        
        df = pd.DataFrame({'app': apps, 'tiempo_uso': tiempos})
        
        # Agrupamiento vectorizado (exacto como enseña la clase de Pandas)
        uso_por_app = df.groupby('app')['tiempo_uso'].sum().to_dict()
        
        return uso_por_app
    
    except (KeyError, TypeError, IndexError):
        print("Error: Datos inválidos para calcular uso por app | Ubicación: calcular_uso_por_app")
        return {}
    
    
    
    
    
    
    
    
    
    
