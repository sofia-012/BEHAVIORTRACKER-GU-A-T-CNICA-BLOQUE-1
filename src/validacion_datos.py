def validar_registro(dato):
    '''
    Verifica que un registro tenga valores válidos.

    Parameters
    ----------
    dato : dict
        Diccionario que representa un registro del datos.

    Returns
    -------
    None
        Lanza ValueError si encuentra un problema
    '''
#Verifica que cada valor lista en lista_diccionarios tenga al menos un elemento
#si no tiene nada entonces se rompe. 

    
    if len(dato["fecha"])== 0:
        raise ValueError("[ERROR CRÍTICO] Registro sin fechas / ubicación: validar_registro")
    if len(dato["app"])== 0:
        raise ValueError("ERROR CRÍTICO] Registro sin apps / ubicación: validar_registro")
    if len(dato["cantidad_uso"])== 0:
        raise ValueError("ERROR CRÍTICO] Registro sin datos de cantidad de uso / ubicación: validar_registro")
    if len(dato["tiempo_uso"])== 0:
        raise ValueError("ERROR CRÍTICO] Registro sin datos de tiempo / ubicación: validar_registro")
    
