from src.carga_datos import cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante

datos = cargar_datos("datos/BehaviorTracker_mock_data.csv")
datos_validos = []
if datos == None:
    print("Error critico: no hay datos, ubicacion: main")

elif len(datos) == 0:
    print("Error critico: la lista esta vacia, ubicacion: main")
else: 
    for d in datos:
            if validar_registro(d):
               datos_validos.append(d)
    if len(datos_validos) == 0:
       print("Error critico: no hay datos validos, ubicacion: main")
    else:
        id_participante = int(input("Ingrese el id del participante: "))
        datos_participante = filtrar_por_participante(datos_validos, id_participante)

        if len(datos_participante) > 0:
            tiempo_total = calcular_tiempo_total(datos_participante)
            promedio = calcular_promedio_uso(datos_participante)
            uso_por_app = calcular_uso_por_app(datos_participante)

            print("Tiempo total:", tiempo_total)
            print("Promedio de uso:", promedio)
            print("Uso por app:", uso_por_app)
