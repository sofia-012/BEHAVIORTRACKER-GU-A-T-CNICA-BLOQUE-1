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
    lista= []
    for dato in datos:
        if dato['id_participante']== id_participante:
            lista.append(dato)
    return lista
