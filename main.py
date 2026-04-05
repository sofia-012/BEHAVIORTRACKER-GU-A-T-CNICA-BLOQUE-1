from src.carga_datos import cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app
from src.validacion_datos import validar_registro

datos = cargar_datos("datos/datos.csv")
datos_validos = []

for d in datos:
    if validar_registro(d):
        datos_validos.append(d)

tiempo_total = calcular_tiempo_total(datos_validos)
promedio = calcular_promedio_uso(datos_validos)
uso_por_app = calcular_uso_por_app(datos_validos)

print("Tiempo total:", tiempo_total)
print("Promedio de uso:", promedio)
print("Uso por app:", uso_por_app)
