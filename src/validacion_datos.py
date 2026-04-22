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
    
    if len(dato["fecha"]) == 0:
        print("Error: Registro sin fechas | Ubicación: validar_registro")
        return False
    
    if len(dato["app"]) == 0:
        print("Error: Registro sin apps | Ubicación: validar_registro")
        return False
    
    if len(dato["cantidad_uso"]) == 0:
        print("Error: Registro sin datos de cantidad de uso | Ubicación: validar_registro")
        return False
    
    if len(dato["tiempo_uso"]) == 0:
        print("Error: Registro sin datos de tiempo | Ubicación: validar_registro")
        return False

    
    for tiempo in dato["tiempo_uso"]:
        if tiempo < 0:
            print("Error: Tiempo de uso negativo | Ubicación: validar_registro")
            return False
    
    if dato["tiempo_uso"] != sorted(dato["tiempo_uso"]):
        print("Error: Tiempo de uso no está ordenado de forma creciente | Ubicación: validar_registro")
        return False

    
    for cantidad_uso in dato["cantidad_uso"]:
        if cantidad_uso < 0:
            print("Error: Cantidad de uso negativa | Ubicación: validar_registro")
            return False

   
    apps_validas = ["Instagram", "TikTok", "WhatsApp", "YouTube"]
    for app in dato["app"]:
        if app not in apps_validas:
            print(f"Error: Valor inválido en campo app ('{app}') | Ubicación: validar_registro")
            return False

    return True