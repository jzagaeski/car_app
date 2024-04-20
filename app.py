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
type_list = sorted(cars_df['type'].unique())
type = st.selectbox(label='Select type', options= type_list, index= type_list.index('SUV'))
mask_filter = (cars_df['type'] == type)
car_filtered = cars_df[mask_filter]
car_hist = px.histogram(car_filtered, x='condition', nbins=35, color='type', barmode='overlay')
st.write(car_hist)
