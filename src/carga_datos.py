
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
        apps_validas = ["instagram", "tiktok", "whatsapp", "youtube"]
        if diccionario['app'] not in apps_validas:
            print(f"Error: Valor inválido para categoría 'app' ({diccionario['app']}) | Ubicación: pasear_linea")
            raise ValueError("Valor inválido para app.")
        
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

import pandas as pd
import os


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
        if not os.path.exists(ruta_archivo):
            print("Error: La ruta no existe o el archivo no se puede abrir | Ubicación: cargar_datos")
            raise FileNotFoundError(f"No se encontró el archivo en la ruta: {ruta_archivo}")

        df = pd.read_csv(ruta_archivo, header=None)      
        df.columns = ['id_participante', 'fecha', 'app', 'cantidad_uso', 'tiempo_uso']

        if df.isna().any().any():
            print("Error crítico: El archivo contiene campos vacíos | Ubicación: cargar_datos")
            raise ValueError("Error crítico: El archivo contiene campos vacíos.")

        if (df['id_participante'] <= 0).any():
            print("Error crítico: Existen id_participante <= 0 | Ubicación: cargar_datos")
            raise ValueError("Error crítico: Existen id_participante <= 0")

        if (df['cantidad_uso'] < 0).any():
            print("Error: Cantidad de uso negativa | Ubicación: cargar_datos")
            raise ValueError("Error: Cantidad de uso negativa")

        if (df['tiempo_uso'] < 0).any():
            print("Error: Tiempo de uso negativo | Ubicación: cargar_datos")
            raise ValueError("Error: Tiempo de uso negativo")

        apps_validas = ["instagram", "tiktok", "whatsapp", "youtube"]
        if not df['app'].isin(apps_validas).all():
            print("Error: Valor inválido en campo app | Ubicación: cargar_datos")
            raise ValueError(f"Error: Apps inválidas. Solo se permiten: {apps_validas}")


        grupos = df.groupby('id_participante')
        lista_diccionarios = []
        for id_p, grupo in grupos:
            participante = {
                'id_participante': int(id_p),
                'fecha': grupo['fecha'].tolist(),
                'app': grupo['app'].tolist(),
                'cantidad_uso': grupo['cantidad_uso'].tolist(),
                'tiempo_uso': grupo['tiempo_uso'].tolist()
            }
            lista_diccionarios.append(participante)

        if not lista_diccionarios:
            print("Error: La base de datos está vacía| Ubicación: cargar_datos")
            raise ValueError("Base de datos vacía")

        print(f"Datos cargados correctamente con Pandas. {len(lista_diccionarios)} participantes encontrados.")
        return lista_diccionarios

    except FileNotFoundError: 
        print("Error: La ruta no existe o el archivo no se puede abrir | Ubicación: cargar_datos")
        raise
    
    except Exception: 
        print("Error: Error al leer el archivo | Ubicación: cargar_datos")
        raise
        
