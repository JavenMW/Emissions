# repo changes after being cloned
import streamlit as st
import pickle

# ['Fuel Consumption Comb (L/100 km)', 
# 'Fuel Type',
# 'Fuel Consumption Hwy (L/100 km)',
# 'Gears', 'Transmission',
# 'Make', 
# 'Vehicle Class',
# 'Model',
# 'Fuel Consumption City (L/100 km)',
# 'Is_Transmission_M']
macpath = 'PredictionApp/model.pkl'

winpath = 'C:/Users/javen/OneDrive/Desktop/Code/Git Repositories/Emissions/PredictionApp/model.pkl'


with open(ipath, 'rb') as file:
    model = pickle.load(file)


fuel_cons_cty = st.text_input('Please enter your city fuel consumption: ')
fuel_cons_hwy = st.text_input('Please enter your highway fuel consumption: ')
fuel_cons_comb = st.text_input('Please enter your combined fuel consumption: ')

fuel_type = st.text_input('Please enter your fuel type: ')

gears = st.text_input('Please enter your gear count: ')
transmissison = st.text_input('Please enter your transmission: ')

make = st.text_input('Please enter your vehicle make: ')
vehicle_class = st.text_input('Please enter your vehicle class: ')
model = st.text_input('Please enter your vehicle model: ')


Is_Transmission_M = transmissison
