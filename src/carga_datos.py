def pasear_linea(linea):
    '''
    Transforma una línea de texto del archivo CSV en un diccionario.

    Parameters
    ----------
    linea : str
        Una línea del archivo CSV

    Returns
    -------
    diccionario1: dict
       Diccionario con los datos estructurados

    '''
    partes = linea.strip().split(',') 
    
    if len(partes) != 5:
        print("Error:La línea no tiene la cantidad correcta de columnas| Ubicación: pasear_linea")
        raise ValueError("Cantidad de columnas incorrecta")

   
    for p in partes:
        if p.strip() == "":
            print("Error: Campo vacío| Ubicación: pasear_linea")
            raise ValueError("Campo vacío")
            
            
    diccionario= {}
    try:
        diccionario['id_participante']= int(partes[0])
        if diccionario['id_participante'] <=0:
            print("Error: id_participante debe ser un entero | Ubicación: pasear_linea")
            raise ValueError('es valor ingresado no es positivo')
    
    except ValueError:
        print("Error: id_participante debe ser un entero | Ubicación: pasear_linea")
        raise ValueError
    
    
    diccionario['fecha']= partes[1]
        
    diccionario['app']= partes[2].strip()
    apps_validas = ["instagram", "tikTok", "whatsApp", "youTube"]
    if diccionario['app'] not in apps_validas:
        print(f"Error: Valor inválido para categoría 'app' ({diccionario['app']}) | Ubicación: pasear_linea")
        raise ValueError("Valor inválido para app")
    
    try:
        diccionario['cantidad_uso']= int(partes[3])
        if diccionario['cantidad_uso']<0:
            print("Error: cantidad de uso debe ser un entero | Ubicación: pasear_linea")
            raise ValueError('es valor ingresado no es positivo')
    except ValueError:
        print("Error: la cantidad de uso debe ser un entero | Ubicación: pasear_linea")
        raise ValueError
    try:
        diccionario['tiempo_uso']= float(partes[4])
        if diccionario['tiempo_uso']<0:
            print("Error: tiempo de uso debe ser positivo | Ubicación: pasear_linea")
            raise ValueError('es valor ingresado no es positivo')
    except ValueError:
        print("Error: el tiempo de uso debe ser un numero| Ubicación: pasear_linea")
        raise ValueError
        
    return diccionario
   

def cargar_datos(ruta_archivo):
    '''
    Lee el archivo CSV y devuelve una lista donde cada elemento es un participante agrupado y cada clave tiene listas adentro. 

    Parameters
    ----------
    ruta_archivo : str
        Ruta completa al archivo CSV 

    Returns
    -------
    lista : list
        Lista de diccionarios con todos los registros del archivo

    '''
    try:
        archivo = open(ruta_archivo, 'r')
        lineas = archivo.readlines()
        
        
        if len(lineas) == 0:
            print("Error: El archivo está vacío | Ubicación: cargar_datos")
            archivo.close()
            raise ValueError("Archivo vacío")
        
    except FileNotFoundError: 
        print("Error: La ruta no existe o el archivo no se puede abrir | Ubicación: cargar_datos")
        raise
    
    except Exception: 
        print("Error: Error al leer el archivo | Ubicación: cargar_datos")
        raise
        
    diccionario= {}
    for linea in lineas:
        if linea.strip():
            registro= pasear_linea(linea)
            id_p= registro['id_participante']
            
            if id_p not in diccionario:
                diccionario[id_p]= {
                    'id_participante': id_p,
                    'fecha': [],
                    'app': [],
                    'cantidad_uso': [],
                    'tiempo_uso': []
                }
            
            
            diccionario[id_p]['fecha'].append(registro['fecha'])
            diccionario[id_p]['app'].append(registro['app'])
            diccionario[id_p]['cantidad_uso'].append(registro['cantidad_uso'])
            diccionario[id_p]['tiempo_uso'].append(registro['tiempo_uso'])
            
    lista_diccionarios = []
    for id_p in diccionario:
        lista_diccionarios.append(diccionario[id_p])
    
    if not lista_diccionarios:
        print("Error: La base de datos está vacía| Ubicación: cargar_datos")
        archivo.close()
        raise ValueError("Base de datos vacía")

    
    for participante in lista_diccionarios:
        tiempos = participante['tiempo_uso']
        if len(tiempos) > 1:
            ordenado = True
            for i in range(len(tiempos) - 1):
                if tiempos[i] > tiempos[i + 1]:
                    ordenado = False
                    break
            
            if not ordenado:
                print("Error: La variable tiempo no está ordenada de forma creciente | Ubicación: cargar_datos")
                archivo.close()
                raise ValueError("Tiempo no ordenado creciente")
                
    archivo.close()
    return lista_diccionarios
    




