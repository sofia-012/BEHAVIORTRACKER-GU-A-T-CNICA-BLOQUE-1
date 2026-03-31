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
    
    diccionario= {}
    diccionario['id_participante']= int(partes[0])
    diccionario['fecha']= partes[1]
    diccionario['app']= linea[2]
    diccionario['cantidad_uso']= int(partes[3])
    diccionario['tiempo_uso']= float(partes[4])
    
    return diccionario

def cargar_datos(ruta_archivo):
    '''
    Lee el archivo CSV y devuelve una lista de diccionarios (un registro por línea).
    Parameters
    ----------
    ruta_archivo : str
        Ruta completa al archivo CSV (ej: "datos/datos_proyecto.csv")

    Returns
    -------
    lista : list
        Lista de diccionarios con todos los registros del archivo

    '''
    
    archivo= open( 'ruta_archivo' , 'r')
    lineas= archivo.readlines()
    lista_diccionarios= []
    for linea in lineas:
        datos= pasear_linea(linea)
        lista_diccionarios.append(datos)
        
    return lista_diccionarios
    





