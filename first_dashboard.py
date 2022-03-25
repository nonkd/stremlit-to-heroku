import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#TITLE
st.title('First Our Dashboard')

#HEADER
st.header("Ini adalah Data Kepuasan Pelanggan Pesawat")

#WRITE
st.write("Membuat Tabel dari Data")
data = pd.read_csv('https://raw.githubusercontent.com/hanarifdahs/datasets/master/train.csv')

# CHECKBOX
show_data = st.checkbox("Show Dataframe")
if show_data:
    st.write(data)

# BUTTON
info = data.shape
if st.button("Lihat Total Data"):
    st.write(info)

# RADIO BUTTON

Class = st.radio("Select Dataframe of Class", data.Class.unique())

# SELECT
Gender = st.selectbox("Select Dataframe of Gender", data.Gender.unique())

# SLIDER
Age = st.slider('Select The Age', 0, 100)

st.write(data[
    (data.Class == Class) &
    (data.Gender == Gender) & (data.Age == Age) ])

# Membuat PLOT PAKE MATPLOTLIB

arr = np.random.normal(1, 1, 100)
st.write(arr)
fig, ax = plt.subplots()
plt.hist(arr, bins=20)
st.pyplot(fig)

#VISUALISASI DATASET
# df_airplane_col = st.selectbox("Select column", ['Inflight wifi service', 'Departure/Arrival time convenient', 
#     'Ease of Online booking', 'Food and drink'])
# fig = px.line(data,  x='Flight Distance', y=df_airplane_col)
# st.plotly_chart(fig)

df_can = px.data.gapminder().query("country == 'Canada'")
st.write(df_can)
df_can_col = st.selectbox("Select column", ['lifeExp', 'gdpPercap', 'pop'])

fig = px.line(df_can, x='year', y=df_can_col)

st.plotly_chart(fig)
