# app.py

import streamlit as st

# Set the title of the app
st.title('My First Streamlit App')

# Display a welcome message
st.write('Welcome to my first Streamlit app!')

# Create a form for user input
name = st.text_input('Enter your name:')

# Display a greeting message
if name:
    st.write(f'Hello, {name}!')
