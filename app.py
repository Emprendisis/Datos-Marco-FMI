import streamlit as st
import pandas as pd
from imfdatapy import ImfData

st.set_page_config(page_title="Explorador FMI", layout="centered")
st.title("🌍 Explorador de Indicadores del FMI")

# Inicializa la clase del FMI
imf = ImfData()

# Interfaz
st.markdown("📥 Ingresa el código del país (por ejemplo: CO, MX, US):")
pais_codigo = st.text_input("Código del país (ISO-2)")

indicadores_fmi = {
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

if st.button("Consultar"):
    if pais_codigo:
        try:
            st.success("Conexión con el FMI establecida.")
            st.info("🔍 Consultando datos disponibles...")

            df_resultados = pd.DataFrame()

            for nombre, codigo in indicadores_fmi.items():
                df = imf.get_data(indicator=codigo, country=pais_codigo, freq='A')
                if not df.empty:
                    df["Indicador"] = nombre
                    df_resultados = pd.concat([df_resultados, df])

            if df_resultados.empty:
                st.warning("No se encontraron datos para los indicadores seleccionados.")
            else:
                st.dataframe(df_resultados)
                file_name = f"{pais_codigo}_indicadores_fmi.xlsx"
                df_resultados.to_excel(file_name, index=False)
                with open(file_name, "rb") as f:
                    st.download_button("📩 Descargar resultados en Excel", f, file_name=file_name)

        except Exception as e:
            st.error(f"❌ Error al consultar datos: {e}")
    else:
        st.warning("⚠️ Ingresa un código de país válido.")