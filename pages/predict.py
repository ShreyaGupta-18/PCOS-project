import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import helper
from helper import parser, unix as platform
import grp

st.set_page_config(page_title='Data_Analysis', page_icon='📈', layout="wide", initial_sidebar_state="collapsed", menu_items=None)
st.title("Analysis of Polycystic Ovary Syndrome")



st.markdown("- Analyzing the data which has around `7k` data points. The goal is to get some insights about the data for model Building. ")

df = helper.get_Data('Data\without_fertility.csv')
    #dropping duplicates
df=df.drop_duplicates()

st.header("A small portion of the data")
st.dataframe(df.head())

st.markdown("___")

st.write(''' ### Feature Details:  
        ※  
        1. make ⇨ car brand under study.     
        2. model ⇨ the specific model of the car. 
        3. vehicle_class ⇨ car body type of the car.
        4. engine_size ⇨ size of the car engine, in Liters.    
        5. cylinders ⇨ number of cylinders.
        6. transmission ⇨ "A" for`Automatic', "AM" for ``Automated manual', "AS" for 'Automatic with select shift', "AV" for 'Continuously variable', "M" for 'Manual'.
        7. fuel_type ⇨ "X" for 'Regular gasoline', "Z" for 'Premium gasoline', "D" for 'Diesel', "E" for 'Ethanol (E85)', "N" for 'Natural gas'.
        8. fuel_consumption_city ⇨ City fuel consumption ratings, in liters per 100 kilometers.
        9. fuel_consumption_hwy ⇨ Highway fuel consumption ratings, in liters per 100 kilometers.
        10. fuel_consumption_comb(l/100km) ⇨ the combined fuel consumption rating (55% city, 45% highway), in L/100 km.
        11. fuel_consumption_comb(mpg) ⇨ the combined fuel consumption rating (55% city, 45% highway), in miles per gallon (mpg).
        12. co2_emissions ⇨ the tailpipe emissions of carbon dioxide for combined city and highway driving, in grams per kilometer.
    ''')
