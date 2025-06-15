
# 🌐 Explorador de Indicadores del FMI

Aplicación web construida con [Streamlit](https://streamlit.io/) para consultar indicadores económicos disponibles del FMI (Fondo Monetario Internacional), utilizando la nueva versión de la librería `sdmx`.

---

## 📌 ¿Qué hace?

Permite ingresar el código ISO de un país (ej. `MEX`, `COL`, `USA`) y consultar qué indicadores económicos están disponibles para ese país desde los servidores del FMI.

---

## 🧱 Requisitos del proyecto

- Python 3.10 o superior
- `streamlit==1.45.1`
- `sdmx==2.5.0`
- `pydantic==1.10.13`

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## 🚀 ¿Cómo ejecutarlo localmente?

```bash
streamlit run app.py
```

---

## 🛠️ Cambios recientes

- Se eliminó el uso de `pandasdmx`, que ya no es compatible con el nuevo endpoint del FMI.
- Se actualizó a la librería `sdmx`, versión 2.5.0, que soporta correctamente el nuevo servicio `dataservices.imf.org`.

---

## 🔗 Créditos

- Fondo Monetario Internacional (FMI): [SDMX Data Services](https://dataservices.imf.org/)
- Librería `sdmx`: [https://pypi.org/project/sdmx/](https://pypi.org/project/sdmx/)

