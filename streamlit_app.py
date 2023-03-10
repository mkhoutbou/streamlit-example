import streamlit as st
import folium
from streamlit_folium import folium_static

# Create a map centered on Keur Madiabel
m = folium.Map(location=[14.1325, -16.0535], zoom_start=14)

# Add a marker at Keur Madiabel and highlight it with a color
folium.Marker(location=[14.1325, -16.0535],
              popup="Keur Madiabel",
              icon=folium.Icon(color='red', icon='info-sign')).add_to(m).add_child(folium.Tooltip("Click me!"))

# Highlight the location of Keur Madiabel with a circle
folium.Circle(location=[14.1325, -16.0535], radius=500,
              color='red', fill=True, fill_opacity=0.2).add_to(m)

# Display the map
folium_static(m)
