"""
app.py — BehaviorTracker Dashboard
====================================
Interfaz web interactiva construida con Streamlit para el análisis
de patrones de uso de aplicaciones móviles.

Flujo principal:
    1. El usuario sube un archivo CSV mediante st.file_uploader.
    2. El archivo es validado por cargar_datos(); si contiene errores,
       se muestra un mensaje con st.error() y se detiene la ejecución.
    3. El usuario selecciona un participante con st.selectbox.
    4. Se calculan y muestran 4 KPIs con st.metric.
    5. Se renderizan 2 gráficos con st.pyplot.
    6. Se ofrece una tabla de detalle expandible con st.dataframe.

Módulos del backend utilizados:
    - src/carga_datos.py     → cargar_datos()
    - src/metricas.py        → calcular_tiempo_total(),
                               calcular_promedio_uso(),
                               calcular_uso_por_app()
    - src/procesamiento_datos.py → filtrar_por_participante()

Autoras:
    Sofia Jalil Bestard, Guadalupe Merke, Miranda Berazategui

Ejecución:
    streamlit run app.py
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from src.carga_datos import cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app
from src.procesamiento_datos import filtrar_por_participante


# ──────────────────────────────────────────────
# Configuración general de la página
# ──────────────────────────────────────────────

st.set_page_config(
    page_title="BehaviorTracker Dashboard",
    page_icon="📱",
    layout="wide"
)

st.title("📱 BehaviorTracker — Análisis de Patrones de Uso")
st.markdown(
    "Sistema de análisis de comportamiento digital a partir de "
    "datos de uso de aplicaciones móviles."
)


# ──────────────────────────────────────────────
# SECCIÓN 1: Carga dinámica de datos
# ──────────────────────────────────────────────
# Se presenta un componente de carga de archivos (st.file_uploader).
# El usuario arrastra o selecciona su archivo CSV.
# Si no se sube ningún archivo, la ejecución se detiene aquí.

st.header("1. Carga de Datos")

archivo_subido = st.file_uploader(
    "Arrastrá y soltá tu archivo CSV aquí",
    type=["csv"],
    help="El archivo debe tener 5 columnas sin encabezado: "
         "id_participante, fecha, app, cantidad_uso, tiempo_uso"
)

if archivo_subido is None:
    st.info("📂 Esperando archivo CSV para comenzar el análisis.")
    st.stop()


# ──────────────────────────────────────────────
# SECCIÓN 2: Puente de validación defensiva
# ──────────────────────────────────────────────
# cargar_datos() requiere una ruta de archivo en disco, no un objeto
# en memoria. Por eso guardamos el archivo subido temporalmente en /tmp/.
# Si el archivo viola alguna regla de validación, cargar_datos() lanza
# una excepción que capturamos y mostramos con st.error(), bloqueando
# el avance del programa con st.stop().

ruta_temp = f"/tmp/{archivo_subido.name}"

with open(ruta_temp, "wb") as f:
    """Escritura temporal del archivo subido en disco para su procesamiento."""
    f.write(archivo_subido.getbuffer())

try:
    datos = cargar_datos(ruta_temp)
except ValueError as e:
    st.error(f"❌ Error de validación en los datos: {e}")
    st.stop()
except FileNotFoundError as e:
    st.error(f"❌ Archivo no encontrado: {e}")
    st.stop()
except Exception as e:
    st.error(f"❌ Error inesperado al cargar los datos: {e}")
    st.stop()

st.success(
    f"✅ Archivo cargado correctamente. "
    f"Se encontraron **{len(datos)} participantes**."
)


# ──────────────────────────────────────────────
# SECCIÓN 2b: Selector de participante
# ──────────────────────────────────────────────
# Se listan los IDs disponibles en el archivo cargado.
# El usuario elige uno y se filtran sus registros con
# filtrar_por_participante().

ids_disponibles = sorted([d["id_participante"] for d in datos])

id_seleccionado = st.selectbox(
    "Seleccioná un participante para analizar:",
    options=ids_disponibles,
    format_func=lambda x: f"Participante {x}"
)

datos_participante = filtrar_por_participante(datos, id_seleccionado)

if not datos_participante:
    st.warning(
        f"⚠️ No se encontraron datos para el participante {id_seleccionado}."
    )
    st.stop()


# ──────────────────────────────────────────────
# SECCIÓN 3: Indicadores Clave (KPIs)
# ──────────────────────────────────────────────
# Se calculan las métricas del participante seleccionado usando
# las funciones del módulo src/metricas.py y se muestran como
# tarjetas con st.metric.

st.header(f"2. Indicadores Clave — Participante {id_seleccionado}")

tiempo_total   = calcular_tiempo_total(datos_participante)
promedio       = calcular_promedio_uso(datos_participante)
uso_por_app    = calcular_uso_por_app(datos_participante)
total_registros = sum(len(d["tiempo_uso"]) for d in datos_participante)
app_favorita   = max(uso_por_app, key=uso_por_app.get) if uso_por_app else "N/A"

col1, col2, col3, col4 = st.columns(4)
col1.metric("⏱️ Tiempo Total (min)",        f"{tiempo_total:.0f}")
col2.metric("📊 Promedio por Sesión (min)", f"{promedio:.1f}")
col3.metric("📋 Total de Registros",        total_registros)
col4.metric("⭐ App más usada",             app_favorita.capitalize())


# ──────────────────────────────────────────────
# SECCIÓN 4: Visualizaciones interactivas
# ──────────────────────────────────────────────
# Se generan dos gráficos con matplotlib y se renderizan
# en el panel principal usando st.pyplot().
# Se usa plt.close() después de cada gráfico para liberar
# memoria y evitar superposición entre reruns de Streamlit.

st.header("3. Visualizaciones")

col_izq, col_der = st.columns(2)

# --- Gráfico 1: Barras — Tiempo de uso por aplicación ---
# Muestra cuántos minutos totales se usó cada app en el período.
with col_izq:
    st.subheader("Uso por Aplicación")
    fig1, ax1 = plt.subplots()
    ax1.bar(uso_por_app.keys(), uso_por_app.values(), color="#4C72B0")
    ax1.set_title("Tiempo total por app (minutos)")
    ax1.set_xlabel("Aplicación")
    ax1.set_ylabel("Tiempo Total (min)")
    ax1.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

# --- Gráfico 2: Líneas — Evolución temporal acumulada ---
# Muestra cómo crece el tiempo de uso acumulado a lo largo de las fechas
# registradas para el participante seleccionado.
with col_der:
    st.subheader("Evolución Temporal Acumulada")

    tiempos_acum = []
    acum = 0
    fechas = []

    for dato in datos_participante:
        for i in range(len(dato["tiempo_uso"])):
            acum += dato["tiempo_uso"][i]
            tiempos_acum.append(acum)
            fechas.append(dato["fecha"][i])

    fig2, ax2 = plt.subplots()
    ax2.plot(fechas, tiempos_acum, marker="o", color="#55A868")
    ax2.set_title("Tiempo acumulado de uso")
    ax2.set_xlabel("Fecha")
    ax2.set_ylabel("Tiempo Acumulado (min)")
    ax2.tick_params(axis="x", rotation=45)
    ax2.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)


# ──────────────────────────────────────────────
# SECCIÓN 5: Tabla de detalle de registros
# ──────────────────────────────────────────────
# Muestra todos los registros individuales del participante en una
# tabla interactiva dentro de un contenedor expandible (st.expander).
# El usuario puede explorar los datos sin que la tabla ocupe espacio
# permanente en la pantalla.

with st.expander("📄 Ver detalle de registros del participante"):
    filas = []
    for dato in datos_participante:
        for i in range(len(dato["fecha"])):
            filas.append({
                "Fecha":              dato["fecha"][i],
                "App":                dato["app"][i],
                "Cantidad de Uso":    dato["cantidad_uso"][i],
                "Tiempo de Uso (min)": dato["tiempo_uso"][i],
            })
    df_detalle = pd.DataFrame(filas)
    st.dataframe(df_detalle, use_container_width=True)
