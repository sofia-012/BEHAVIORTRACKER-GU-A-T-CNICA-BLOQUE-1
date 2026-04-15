def validar_registro(dato):
    '''
    Verifica que un registro tenga valores válidos.

    Parameters
    ----------
    dato : dict
        Diccionario que representa un registro del datos.

    Returns
    -------
    bool
        True si el registro es válido, False en caso contrario.
    '''
#Verifica que cada valor lista en lista_diccionarios tenga al menos un elemento
#si no tiene nada entonces se rompe. 

    try:
        if len(dato["fecha"])== 0:
            return False
        if len(dato["app"])== 0:
            return False
        if len(dato["cantidad_uso"])== 0:
            return False
        if len(dato["tiempo_uso"])== 0:
            return False
    
        for cantidad_uso in dato["cantidad_uso"]:
            if cantidad_uso < 0:
                return False 
# Si los numeros guardados en tiempo_uso o cantidad_uso es ngativo se rompe.     

        for tiempo_uso in dato["tiempo_uso"]:
            if tiempo_uso < 0:
                return False     
        return True  
    except KeyError:
           return False
    
    except TypeError:
           return False
    
