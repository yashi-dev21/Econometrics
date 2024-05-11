import streamlit as st
import pickle
import numpy as np

import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Streamlit App", page_icon="im", layout="wide")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Inject custom CSS
st.markdown(
    """
    <style>
    /* Custom CSS styles */
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f2f6;
    }
    h1 {
        color: #333;
        text-align: center;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)
with st.container():

    # Load the trained model
    model = pickle.load(open('model.pkl', 'rb'))

    # Define the function to predict GDP
    def predict_gdp(land_agriculture, urban_buildup, gdp_agriculture, gdp_industry, gdp_services):
        features = np.array([land_agriculture, urban_buildup, gdp_agriculture, gdp_industry, gdp_services]).reshape(1, -1)
        prediction = model.predict(features)
        return prediction[0]

    # Define the Streamlit app
    def main():
        st.title('GDP Prediction App')
        st.write('Enter the following details to predict GDP:')

        # Add input fields for user input
        land_agriculture = st.number_input('Land due to Agriculture')
        urban_buildup = st.number_input('Buildup (Urban)')
        gdp_agriculture = st.number_input('GDP due to Agriculture')
        gdp_industry = st.number_input('GDP due to Industry')
        gdp_services = st.number_input('GDP due to Services')

        # Add a button to trigger prediction
        if st.button('Predict Total GDP'):
            total_gdp = predict_gdp(land_agriculture, urban_buildup, gdp_agriculture, gdp_industry, gdp_services)
            st.success(f'The predicted Total GDP value is {total_gdp:e}')

    if __name__ == '__main__':
        main()
