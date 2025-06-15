
import streamlit as st
import pandas as pd
from imfdatapy import ImfData
from datetime import datetime
import io

# Configuración inicial de la app
st.set_page_config(page_title="Explorador FMI", layout="centered")
st.title("🌐 Explorador de Indicadores del FMI")

# Inicializar la conexión con IMF
imf = ImfData()

# Cargar lista de países disponibles desde IMF
st.markdown("### 🌍 Selecciona país e indicador")
try:
    countries_df = imf.get_countries()
    country_list = countries_df['iso'].tolist()
    country_names = countries_df['name'].tolist()
    country_map = dict(zip(country_names, country_list))
    country_name = st.selectbox("Selecciona el país:", country_names)
    country_code = country_map[country_name]
except Exception as e:
    st.error(f"No se pudo cargar países: {e}")
    st.stop()

# Indicadores disponibles (definidos en la imagen)
indicators = {
    "Deuda externa total (USD)": "DT.DOD.DECT.CD",
    "Deuda externa total (% del PIB)": "DT.DOD.DECT.GN.ZS",
    "PIB (USD)": "NY.GDP.MKTP.CD",
    "Balanza comercial (USD)": "NE.EXP.GNFS.CD",
    "Balanza comercial (% PIB)": "NE.EXP.GNFS.ZS",
    "Tasa de desempleo": "SL.UEM.TOTL.ZS",
    "Inflación (IPC anual %)": "FP.CPI.TOTL.ZG",
    "PIB (PPA, USD internacionales)": "NY.GDP.MKTP.PP.CD",
    "Crecimiento del PIB (%)": "NY.GDP.MKTP.KD.ZG",
    "Prima de riesgo (bonos soberanos, %)": "CM.MKT.LDOM.NO"
}
indicator_name = st.selectbox("📊 Indicador:", list(indicators.keys()))
indicator_code = indicators[indicator_name]

# Años disponibles
anio_inicio = st.slider("Año de inicio", 2000, 2023, 2010)
anio_fin = st.slider("Año de fin", anio_inicio, 2024, 2023)

# Consultar al hacer clic
if st.button("Consultar datos"):
    try:
        df = imf.get_indicator(country=country_code, indicator=indicator_code, start=anio_inicio, end=anio_fin)
        df = df.dropna().sort_index()
        st.line_chart(df)
        st.dataframe(df)

        # Exportar a Excel
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=True)
        st.download_button(
            label="📥 Descargar Excel",
            data=excel_buffer.getvalue(),
            file_name=f"{country_code}_{indicator_code}_fmi.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"❌ Error consultando datos del FMI: {e}")
