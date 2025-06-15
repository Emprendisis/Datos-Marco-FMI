import streamlit as st
from sdmx import Request

st.set_page_config(page_title="Explorador FMI", page_icon=":bar_chart:", layout="centered")

st.title("📊 Explorador de Indicadores del FMI")

st.write("Ingresa el código del país (ej. MEX, COL, USA) y consulta los indicadores disponibles.")

with st.form("fmi_form"):
    country_code = st.text_input("🌐 Código ISO del país:", "MEX")
    submitted = st.form_submit_button("Consultar indicadores")

if submitted:
    try:
        st.info("Conectando al FMI...")
        req = Request("IMF", endpoint="https://dataservices.imf.org/REST/SDMX_XML.svc")
        resp = req.dataflow()
        flows = resp.dataflow

        # Filtrar flujos que contienen datos del país solicitado
        filtered = {k: v for k, v in flows.items() if country_code.upper() in v.name.en.upper()}

        if not filtered:
            st.warning("No se encontraron indicadores para ese país.")
        else:
            st.success("📈 Indicadores encontrados:")
            data = [(k, v.name.en) for k, v in filtered.items()]
            st.dataframe(data, use_container_width=True)
    except Exception as e:
        st.error(f"❌ Error al consultar los datos: {e}")
