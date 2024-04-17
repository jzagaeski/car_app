import streamlit as st
import pandas as pd
import altair as at
import plotly.express as px
full_path = 'C:/Users/jzigg/car_app/vehicles_us.csv'
vehicles = pd.read_csv(full_path)
vehicles = pd.read_csv('/vehicles_us.csv')
