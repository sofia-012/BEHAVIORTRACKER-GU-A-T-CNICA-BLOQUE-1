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
        print("Error: La base de datos no está vacía | Ubicación: calcular_tiempo_total")
        raise ValueError("La base de datos no está vacía")
    
    
    try:
        total = 0
        for dato in datos:
            for tiempo in dato["tiempo_uso"]:
                if tiempo < 0:
                    print("Error: la variable tiempo no debe ser negativa | Ubicación: calcular_tiempo_total")
                    raise ValueError("la variable tiempo no debe ser negativa")
                total += tiempo
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
        print("Error: La base de datos no está vacía | Ubicación: calcular_tiempo_total")
        raise ValueError("La base de datos no está vacía")
    try: 
        cantidad_registros= 0
        tiempo_total= 0
        
        for dato in datos:
            if 'tiempo_uso' not in dato:
                print("Error: Falta la clave 'tiempo_uso' en los datos | Ubicación: calcular_promedio_uso")
                raise KeyError("Falta la clave 'tiempo_uso'")
            
            for tiempo in dato['tiempo_uso']:
                if not isinstance(tiempo, (int, float)):
                    print("Error: Valor no numérico en tiempo_uso | Ubicación: calcular_promedio_uso")
                    raise TypeError("Valor no numérico en tiempo_uso")
                if tiempo < 0:
                    print("Error: Valor negativo en tiempo_uso (no permitido) | Ubicación: calcular_promedio_uso")
                    raise ValueError("Valor negativo en tiempo_uso")
                
                tiempo_total += tiempo
                cantidad_registros += 1
            
        promedio = tiempo_total / cantidad_registros
        return promedio
    
    except ZeroDivisionError:
        print("Error: No hay registros válidos para calcular el promedio | Ubicación: calcular_promedio_uso")
        raise
    except KeyError:
        print("Error: Falta la clave 'tiempo_uso' en los datos | Ubicación: calcular_promedio_uso")
        raise
    except (TypeError, ValueError):
        print("Error: Datos inválidos para calcular el promedio (tipo o valor incorrecto) | Ubicación: calcular_promedio_uso")
        raise
    except Exception as e:
        print(f"Error: {str(e)} | Ubicación: calcular_promedio_uso")
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
        print("Error: la base de datos no está vacía | Ubicación: calcular_uso_por_app")
        return {}
    
    diccionario = {}
    
    try:
        for dato in datos:
            for i in range(len(dato['app'])):
                app = dato['app'][i]
                tiempo = dato['tiempo_uso'][i]
                
                if app not in diccionario:
                    diccionario[app] = 0
                    
                diccionario[app] += tiempo
                
    except (KeyError, TypeError, IndexError) as e:
        print(f"Error: Datos inválidos para calcular uso por app ({type(e).__name__}) | Ubicación: calcular_uso_por_app")
        return {}
    
    return diccionario
        
    
    
    
    
    
    
    
    
    
    
