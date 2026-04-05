import src.carga_datos as c
import src.metricas as m

datos = c.cargar_datos("datos/datos.csv")

print("Tiempo total:", m.calcular_tiempo_total(datos))
print("Promedio:", m.calcular_promedio_uso(datos))
print("Uso por app:", m.calcular_uso_por_app(datos))


