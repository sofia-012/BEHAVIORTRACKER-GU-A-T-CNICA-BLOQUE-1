def validar_registro(dato):
    '''
    Verifica que un registro tenga valores válidos.

    Parameters
    ----------
    dato : dict
        Diccionario que representa un registro de datos.

    Returns
    -------
    bool
        True si el registro es válido, False en caso contrario.
        Si encuentra un error, imprime el mensaje error antes de retornar False.
    '''
    
    if not dato.get('fecha') or len(dato['fecha']) == 0:
        print("Error: Registro sin fechas | Ubicación: validar_registro")
        return False
    
    if not dato.get('app') or len(dato['app']) == 0:
        print("Error: Registro sin apps | Ubicación: validar_registro")
        return False
    
    if not dato.get('cantidad_uso') or len(dato['cantidad_uso']) == 0:
        print("Error: Registro sin datos de cantidad de uso | Ubicación: validar_registro")
        return False
    
    if not dato.get('tiempo_uso') or len(dato['tiempo_uso']) == 0:
        print("Error: Registro sin datos de tiempo | Ubicación: validar_registro")
        return False

   
    return True