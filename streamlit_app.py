import streamlit as st
import pandas as pd
import numpy as np
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static

# Generate random data
np.random.seed(42)
countries = ['United States', 'China', 'India', 'Brazil', 'Pakistan', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan']
num_females = np.random.randint(1000000, 100000000, size=len(countries))
data = pd.DataFrame({'Country': countries, 'Number of Females': num_females})

# Create Streamlit app
st.title('Random Data Generator')
st.write('This app generates random data with country name and number of female, and displays the data on a map.')
st.write('### Random Data')
st.dataframe(data)

# Show data on a map
st.write('### Map')
geolocator = Nominatim(user_agent='my-app')
m = folium.Map(location=[0, 0], zoom_start=2)
for i in range(len(data)):
    country = data.loc[i, 'Country']
    num_females = data.loc[i, 'Number of Females']
    tooltip = f"{country}: {num_females:,} females"
    location = geolocator.geocode(country)
    if location is not None:
        folium.Marker(location=[location.latitude, location.longitude], tooltip=tooltip).add_to(m)
folium_static(m)
