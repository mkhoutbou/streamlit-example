import streamlit as st
import pandas as pd

# Create a Streamlit app
st.title("CSV Data Analysis")

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('Cooperative Assessment For Streamlit.csv')

# Display the DataFrame using Streamlit's dataframe function
st.write(df)
