import streamlit as st
import pandas as pd
import plotly.express as px
cars_df = pd.read_csv('vehicles_us.csv')
cars_df['make'] = cars_df['model'].apply(lambda x: x.split()[0])
st.header('Data Viewer')
st.dataframe(cars_df)
st.header('Vehicle condition relative to price by type')
car_scat = px.scatter(cars_df, x='condition', y='price', color='type')
st.write(car_scat)
st.header('Compare vehicle condition by type')
normalize = st.checkbox(label='normalize histogram', value=True)
if normalize:
    histnorm = 'percent',
else:
    histnorm = None
car_hist = px.histogram(cars_df, x='condition', nbins=35, color='type', histnorm=histnorm, barmode='overlay')
st.write(car_hist)
