# under construction

import streamlit as st # type: ignore
import pickle
import numpy as np # type: ignore
import pandas as pd # type: ignore
import joblib # type: ignore
# import torch # type: ignore
import xgboost as xgb


macpath = '/Users/Javen/Desktop/Git Repositories/Emissions/PredictionApp/model.pkl'
winpath = 'C:/Users/javen/OneDrive/Desktop/Code/Git Repositories/Emissions/PredictionApp/model.pkl'
# Opens prepackaged model
with open(winpath, 'rb') as f:
    model = pickle.load(f)


def mpg_to_lkm(mpg=1):
    """
    Used to convert mpg to l/100km
    """
    lkm = 235.2 / mpg
    return lkm


def __main__():
    """
    Main program. Utilizes streamlit to start a local web instance for model interaction.
    """
    # Prompts to store user information for the model
    st.title('Vehicle Info')
    st.write("----------------------------------------------------------------------------")
    make = st.text_input('Please enter your vehicle make: ')
    vehicle_class = st.text_input("Please enter your vehicle class: 'COMPACT' 'SUV - SMALL' 'MID-SIZE' 'TWO-SEATER' 'MINICOMPACT' \
                                    'SUBCOMPACT' 'FULL-SIZE' 'STATION WAGON - SMALL' 'SUV - STANDARD' \
                                    'VAN - CARGO' 'VAN - PASSENGER' 'PICKUP TRUCK - STANDARD' 'MINIVAN' \
                                    'SPECIAL PURPOSE VEHICLE' 'STATION WAGON - MID-SIZE' \
                                    'PICKUP TRUCK - SMALL'")
    vehicle_model = st.text_input('Please enter your vehicle model: ')
    st.write("----------------------------------------------------------------------------")
    st.title('MPG')
    st.write("----------------------------------------------------------------------------")

    mpgfuel_cons_cty = st.number_input('Please enter your city fuel consumption: ', value=1)
    mpgfuel_cons_hwy = st.number_input('Please enter your highway fuel consumption: ', value=1)
    mpgfuel_cons_comb = st.number_input('Please enter your combined fuel consumption: ', value=1)
    # Convert the inputs to float if they are not empty

    fuel_cons_cty = mpg_to_lkm(float(mpgfuel_cons_cty))

    fuel_cons_hwy = mpg_to_lkm(float(mpgfuel_cons_hwy))

    fuel_cons_comb = mpg_to_lkm(float(mpgfuel_cons_comb))

    st.write("----------------------------------------------------------------------------")
    st.title('Fuel Type')
    st.write("----------------------------------------------------------------------------")
    fuel_type = st.text_input('Please enter your fuel type: \
                                X = Regular gasoline \
                                Z = Premium gasoline \
                                D = Diesel \
                                E = Ethanol (E85) \
                                N = Natural gas ')
    st.write("----------------------------------------------------------------------------")
    st.title('Transmission')
    st.write("----------------------------------------------------------------------------")
    gears = st.number_input('Please enter your gear count: ')
    transmissison = st.text_input('Please enter your transmission: \
                            A = Automatic \
                            AM = Automated manual \
                            AS = Automatic with select shift \
                            AV = Continuously variable \
                            M = Manual')
    st.write("----------------------------------------------------------------------------")

    if transmissison == 'M':
        Is_Transmission_M = 1
    else:
        Is_Transmission_M = 0

    new_data = pd.DataFrame({
        'Fuel Consumption Comb (L/100 km)': [fuel_cons_comb],
        'Fuel Type': [fuel_type],
        'Fuel Consumption Hwy (L/100 km)': [fuel_cons_hwy],
        'Gears': [gears],
        'Transmission': [transmissison],
        'Make': [make],
        'Vehicle Class': [vehicle_class],
        'Model': [vehicle_model],
        'Fuel Consumption City (L/100 km)': [fuel_cons_cty],
        'Is_Transmission_M': [Is_Transmission_M]
    })

    # Ensure categorical columns are of type 'category'
    new_data['Fuel Type'] = new_data['Fuel Type'].astype('category')
    new_data['Transmission'] = new_data['Transmission'].astype('category')
    new_data['Make'] = new_data['Make'].astype('category')
    new_data['Vehicle Class'] = new_data['Vehicle Class'].astype('category')
    new_data['Model'] = new_data['Model'].astype('category')
    new_data['Gears'] = new_data['Gears'].astype('float')


    dmatrix = xgb.DMatrix(new_data, enable_categorical = True)
    if st.button('Predict'):
        prediction = model.predict(new_data)
        st.write(f'Your car emits {prediction} (g/km) in emissions.')

 
if __name__ == "__main__":
    __main__()

