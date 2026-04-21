def  filtrar_por_participante(datos, id_participante):
    '''
    Filtra los registros y devuelve solo los que pertenecen a un participante específico.

    Parameters
    ----------
    datos : list/dict
        Lista de diccionarios con todos los registros
    id_participante : int
        DESCRIPTION.

    Returns
    -------
    lista : list
        Lista con solo los registros del participante solicitado

    '''
    if datos == None:
        print("Error critico: error- no hay datos, ubicacion:filtrar_por_participante")
        return []
    if len(datos)== 0:
        print("Error la lista esta vacia, ubicacion:filtrar_por_participante")
        return []
    if id_participante <=0:
        print("error critico, el id debe ser positivo, ubicacion:filtrar_por_participante")
        return[]
    lista= []

    for dato in datos:
        if "id_participante" not in dato:
            print("error, id_participante esta vacio, ubicacion:filtrar_por_participante")
            return[]
        if dato["id_participante"]<=0:
           print("error critico, error: el id  debe ser positivo, ubicacion: filtrar_por_participante")
           return[]
        if dato["id_participante"]== None:
           print("error critico, id_participante esta vacio, ubicacion:filtrar_por_participante")
           return[]
           
        if dato['id_participante']== id_participante:
            lista.append(dato)
    if len(lista)== 0:
        print("Error critico, la lista esta vacia el participante no esta en la lista,ubicacion: filtrar_por_participante")
    return lista
