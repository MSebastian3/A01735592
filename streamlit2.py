# -*- coding: utf-8 -*-
"""Streamlit2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Onu7ZGM0GHLIvWXHd71Bp3eK1QOlDBGt
"""

import streamlit as st
import pandas as pd

st.title("Police Incident Reports from 2018 to 2020 in San Francisco")

# Provide the direct link to the CSV file
csv_url = "https://drive.google.com/uc?id=11oLcKiW8SgCOp3tGiQCYuRG7pLL_J-Zf"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_url)

st.markdown("The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.")

# Display the DataFrame
st.write(df)

# Display the map using latitude and longitude columns from the DataFrame
if "Latitude" in df.columns and "Longitude" in df.columns:
    st.map(df[["Latitude", "Longitude"]].dropna())
else:
    st.warning("Latitude and Longitude columns are missing in the DataFrame.")
