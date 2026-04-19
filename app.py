import streamlit as st

st.set_page_config(page_title="GridBalance", page_icon="⚡")

st.title("⚡ GridBalance")
st.subheader("Einfache Bewertung für netzdienliche Stromnutzung")

st.write("Gib Werte ein und prüfe, ob der Zeitpunkt eher gut oder schlecht ist.")

hour = st.slider("Uhrzeit", 0, 23, 12)
solar = st.slider("Solarproduktion", 0, 100, 50)
wind = st.slider("Windproduktion", 0, 100, 50)

if st.button("Bewertung anzeigen"):
    score = solar + wind

    if score >= 140:
        result = "gut"
        message = "Gute Zeit für flexible Stromnutzung."
    elif score >= 80:
        result = "mittel"
        message = "Mittlere Eignung."
    else:
        result = "schlecht"
        message = "Eher ungünstige Zeit."

    st.write(f"**Uhrzeit:** {hour}:00 Uhr")
    st.write(f"**Solar:** {solar}")
    st.write(f"**Wind:** {wind}")
    st.write(f"**Bewertung:** {result}")

    if result == "gut":
        st.success(message)
    elif result == "mittel":
        st.warning(message)
    else:
        st.error(message)
