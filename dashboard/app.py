# app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
import streamlit as st
from PIL import Image


# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model.pkl')
scaler_path = os.path.join(BASE_DIR, 'scaler.pkl')
data_path = os.path.join(BASE_DIR, '..', 'data', 'cleaned_spacex_launches.csv')

# Load assets
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
df = pd.read_csv(data_path)

# Load and display the launch site image
st.subheader("🛰️ SpaceX Launch Site Overview")
image = Image.open(r"C:\Users\varav\Documents\Projects\Data_Science_Capstone\spacey_capstone\dashboard\launch_site.jpg")
st.image(image, caption="Primary Launch Location - SpaceX", use_container_width=True)

# Sidebar Inputs
st.sidebar.title("🚀 Launch Prediction Input")
mass = st.sidebar.slider("Payload Mass (kg)", 0, 10000, 5000)
site = st.sidebar.selectbox("Launch Site", df['Launch site'].unique())
orbit = st.sidebar.selectbox("Orbit", df['Orbit'].unique())
booster = st.sidebar.selectbox("Booster Version", df['Version, booster[h]'].unique())

# User input → DataFrame
input_df = pd.DataFrame({
    'Payload mass': [mass],
    'Launch site': [site],
    'Orbit': [orbit],
    'Version, booster[h]': [booster]
})
input_encoded = pd.get_dummies(input_df)

# Align columns with training features
X_columns = model.feature_names_in_
for col in X_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0
input_encoded = input_encoded[X_columns]

# Scale and Predict
input_scaled = scaler.transform(input_encoded)
prediction = model.predict(input_scaled)[0]
confidence = model.predict_proba(input_scaled)[0][int(prediction)]

# Display Results
st.title("🛰️ SpaceY Launch Dashboard")
st.subheader("Launch Prediction Result")
st.success("✅ Booster Landing Successful!" if prediction == 1 else "❌ Booster Failed to Land.")
st.write(f"📈 Prediction Confidence: **{confidence*100:.2f}%**")

# Show Map
import folium
from streamlit_folium import st_folium

m = folium.Map(location=[28.5, -80.6], zoom_start=3)
for site in df['Launch site'].unique():
    folium.Marker(location=[28.5, -80.6], popup=site).add_to(m)
st.subheader("🗺️ Launch Site Map")
st_folium(m, width=700)

# Orbit Plot
import plotly.express as px
orbit_plot = df.groupby('Orbit')['Landing_Success'].mean().reset_index()
fig = px.bar(orbit_plot, x='Orbit', y='Landing_Success', title='🚀 Orbit vs Success Rate')
st.plotly_chart(fig)