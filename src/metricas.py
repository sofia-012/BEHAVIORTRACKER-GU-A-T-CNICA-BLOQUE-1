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
    total= 0
    for dato in datos:
        total+= dato['tiempo_uso']
    return total
    
    
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
    try: 
        cantidad_registros= 0
        tiempo_total= 0
        
        for dato in datos:
            tiempo_total+= dato['tiempo_uso']
            cantidad_registros += 1
            
      
        promedio= tiempo_total / cantidad_registros
        return promedio
    except ZeroDivisionError as e:
        print("No se puede dividir por cero", e)
    return 0

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
    diccionario= {}
    for dato in datos:
        app = dato['app']
        if app not in diccionario:
            diccionario[app] = 0
        diccionario[app] += dato['tiempo_uso']
            
    return diccionario
        
    
    
    
    
    
    
    
    
    
    