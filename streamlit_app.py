import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

# Set page title
st.set_page_config(page_title="Random Data Map", page_icon=":earth_africa:")

# Define function to generate random data
def generate_data(num_rows):
    countries = ['Gambia', 'Guinea-Bissau']
    regions = {
        'Gambia': ['Banjul', 'Central River'],
        'Guinea-Bissau': ['Bafatá', 'Biombo']
    }
    departments = {
        'Banjul': ['Banjul', 'Serrekunda'],
        'Central River': ['Janjanbureh', 'Kuntaur'],
        'Bafatá': ['Bafatá', 'Xitole'],
        'Biombo': ['Biombo', 'Bula']
    }
    min_females = st.slider('Minimum number of females', 1, 1000, 100)
    data = pd.DataFrame({
        'Country': np.random.choice(countries, num_rows),
        'Region': np.nan,
        'Department': np.nan,
        'Female Count': np.random.randint(min_females, 1001, num_rows)
    })
    for country in countries:
        country_mask = data['Country'] == country
        regions_list = regions[country]
        for region in regions_list:
            region_mask = country_mask & (data['Region'].isna())
            data.loc[region_mask, 'Region'] = region
            departments_list = departments[region]
            for department in departments_list:
                department_mask = region_mask & (data['Department'].isna())
                data.loc[department_mask, 'Department'] = department
    return data

# Generate random data
data = generate_data(100)

# Filter data by country
selected_country = st.sidebar.selectbox('Select a country', ['Gambia', 'Guinea-Bissau'])
filtered_data = data[data['Country'] == selected_country]

# Filter data by region
selected_region = st.sidebar.selectbox('Select a region', ['All'] + list(filtered_data['Region'].unique()))
if selected_region != 'All':
    filtered_data = filtered_data[filtered_data['Region'] == selected_region]

# Filter data by department
selected_department = st.sidebar.selectbox('Select a department', ['All'] + list(filtered_data['Department'].unique()))
if selected_department != 'All':
    filtered_data = filtered_data[filtered_data['Department'] == selected_department]

# Create map
geolocator = Nominatim(user_agent="my-app")
location = geolocator.geocode(selected_country)
m = folium.Map(location=[location.latitude, location.longitude], zoom_start=7)

# Add markers to map
for index, row in filtered_data.iterrows():
    address = f"{row['Department']}, {row['Region']}, {row['Country']}"
    location = geolocator.geocode(address)
    if location:
        tooltip = f"Female Count: {row['Female Count']}"
        folium.Marker(
            location=[location.latitude, location.longitude],
            tooltip=tooltip
        ).add_to(m)

# Display map
folium_static(m)
