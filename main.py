import os
import matplotlib.pyplot as plt


from src.carga_datos import cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante

ruta_datos = "datos/BehaviorTracker_mock_data.csv"

def generar_graficos(datos_participante, id_participante, uso_por_app):
    if not os.path.exists('graficos'):
        os.makedirs('graficos')
    
    # Gráfico 1: Barras - Uso por aplicación
    plt.figure()
    plt.bar(uso_por_app.keys(), uso_por_app.values())
    plt.title('Uso por Aplicación')
    plt.xlabel('Aplicación')
    plt.ylabel('Tiempo Total (minutos)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('graficos/uso_por_app.png')
    plt.close()

    # Gráfico 2: Líneas - Evolución temporal
    plt.figure()
    tiempos_acum = []
    acum = 0
    fechas = []
    for dato in datos_participante:
        for i in range(len(dato['tiempo_uso'])):
            acum += dato['tiempo_uso'][i]
            tiempos_acum.append(acum)
            fechas.append(dato['fecha'][i])
   
    plt.plot(fechas, tiempos_acum)
    plt.title('Evolución del Uso')
    plt.xlabel('Fecha')
    plt.ylabel('Tiempo Acumulado (minutos)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('graficos/evolucion_temporal.png')
    plt.close()
    
    print("Gráficos guardados en la carpeta graficos/")

#Programa principal
datos = cargar_datos(ruta_datos)

datos_validos = []
if datos is None:
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

            generar_graficos(datos_participante, id_participante, uso_por_app)

            print("Procesamiento completado exitosamente con Pandas y Matplotlib.")
        else:
            print("No se encontraron datos para el participante", id_participante)