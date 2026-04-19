import streamlit as st
import joblib
import pandas as pd

# Modell laden
model = joblib.load("model.pkl")

st.set_page_config(page_title="GridBalance", page_icon="⚡")

st.title("⚡ GridBalance – ML Version")
st.write("Vorhersage für netzdienliche Stromnutzung")

# Eingaben
hour = st.slider("Uhrzeit", 0, 23, 12)
solar = st.slider("Solarproduktion", 0, 100, 50)
wind = st.slider("Windproduktion", 0, 100, 50)

# Button
if st.button("Vorhersage starten"):

    # Input für Modell
    input_df = pd.DataFrame([{
        "hour": hour,
        "solar": solar,
        "wind": wind
    }])

    # Vorhersage
    prediction = model.predict(input_df)[0]

    st.subheader(f"Vorhersage: {prediction}")

    # Anzeige
    if prediction == "gut":
        st.success("Gute Zeit für Stromnutzung")
    elif prediction == "mittel":
        st.warning("Mittlere Zeit")
    else:
        st.error("Schlechte Zeit")