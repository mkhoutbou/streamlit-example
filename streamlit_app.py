import streamlit as st
import pandas as pd

# Load the CSV file
csv_file = 'Cooperative Assessment For Streamlit.csv'
df = pd.read_csv(csv_file)

# Display all columns
st.write('## All Columns')
st.write(df.columns)

# Provide basic analysis
st.write('## Basic Analysis')
st.write(f'Number of Rows: {df.shape[0]}')
st.write(f'Number of Columns: {df.shape[1]}')
st.write(df.describe())

# Allow user to select a column for further analysis
selected_column = st.selectbox('Select a Column for Further Analysis', df.columns)

# Display unique values in the selected column
st.write(f'Unique Values in {selected_column}:')
st.write(df[selected_column].unique())
