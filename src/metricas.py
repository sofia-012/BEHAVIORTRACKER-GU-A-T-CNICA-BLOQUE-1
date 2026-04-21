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
    total = 0
    for dato in datos:
        for tiempo in dato["tiempo_uso"]:
            total += tiempo
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
            for tiempo in dato['tiempo_uso']:
                tiempo_total += tiempo
                cantidad_registros += 1
            
      
        promedio= tiempo_total / cantidad_registros
        return promedio
    except ZeroDivisionError as e:
        raise ZeroDivisionError("[ERROR CRÍTICO] Sin registros para calcular el promedio / ubicación: calcular_promedio_uso")
     
    

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
    diccionario = {}
    
    for dato in datos:
        for i in range(len(dato['app'])):
            app = dato['app'][i]
            tiempo = dato['tiempo_uso'][i]
            
            if app not in diccionario:
                diccionario[app] = 0
                
            diccionario[app] += tiempo
            
    return diccionario
        
    
    
    
    
    
    
    
    
    
    
