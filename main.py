import src.carga_datos as c
import src.metricas as m
import src.validacion_datos as v

datos = c.cargar_datos("datos/datos.csv")
datos_validos = []

for d in datos:
    if v.validar_registro(d):
        datos_validos.append(d)

tiempo_total = m.calcular_tiempo_total(datos_validos)
promedio = m.calcular_promedio_uso(datos_validos)
uso_por_app = m.calcular_uso_por_app(datos_validos)

print("Tiempo total:", tiempo_total)
print("Promedio de uso:", promedio)
print("Uso por app:", uso_por_app)

