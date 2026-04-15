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
    try: 
       diccionario= {}
       diccionario['id_participante']= int(partes[0])
       diccionario['fecha']= partes[1]
       diccionario['app']= partes[2]
       diccionario['cantidad_uso']= int(partes[3])
       diccionario['tiempo_uso']= float(partes[4])
       return diccionario
   
    except ValueError as e:
        print('Numero/valor invalido', e)
    except:
        print('error al almacenar datos')

def cargar_datos(ruta_archivo):
    '''
    Lee el archivo CSV y devuelve una lista de diccionarios, donde cada diccionario 
    corresponde a los datos de un participante (con listas internas).
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
        archivo= open(ruta_archivo , 'r')
        lineas= archivo.readlines()
        diccionario= {}
        
    except FileNotFoundError: 
        print('archivo no encontrado')
        return []
    
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
            
    archivo.close()
    return lista_diccionarios
    




