# Explorador de Indicadores Macroeconómicos del FMI

Esta aplicación en Streamlit permite consultar indicadores económicos del FMI para cualquier país del mundo utilizando `imfdatapy`.

## Requisitos

- Python 3.8+
- Paquetes listados en `requirements.txt`

## Cómo ejecutar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Indicadores incluidos

- Deuda externa total (USD)
- Deuda externa total (% del PIB)
- PIB (USD)
- Balanza comercial (USD)
- Balanza comercial (% PIB)
- Tasa de desempleo
- Inflación (IPC anual %)
- PIB en PPA (USD internacionales)
- Crecimiento del PIB (%)
- Prima de riesgo (bonos soberanos, %)

Fuente: Fondo Monetario Internacional (FMI)