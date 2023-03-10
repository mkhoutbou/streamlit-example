import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

# Load the CSV file
csv_file = 'Cooperative Assessment For Streamlit.csv'


# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(csv_file)
    return df

df = load_data()

# Show data
if st.checkbox("Show raw data"):
    st.write(df)

# Show summary statistics
if st.checkbox("Show summary statistics"):
    st.write(df.describe())

# Show correlation heatmap
if st.checkbox("Show correlation heatmap"):
    st.write(sns.heatmap(df.corr(), annot=True, cmap="coolwarm"))

# Show scatter plot
x_values = st.selectbox("Select x-axis column for scatter plot", df.columns)
y_values = st.selectbox("Select y-axis column for scatter plot", df.columns)
if st.button("Generate scatter plot"):
    st.write(f"Scatter plot between {x_values} and {y_values}")
    st.write(px.scatter(df, x=x_values, y=y_values))

# Show bar chart
column_to_plot = st.selectbox("Select column to plot", df.columns)
if st.button("Generate bar chart"):
    st.write(f"Bar chart of {column_to_plot}")
    st.write(px.bar(df, x=column_to_plot, y=y_values))
