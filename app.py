# app.py

import streamlit as st
import subprocess
import sys
import pandas as pd

# Function to install the package
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure the funda-scraper package is installed
install_package("funda-scraper")

# Import the FundaScraper after installation
from funda_scraper import FundaScraper

# Set Streamlit app title
st.title("Funda Real Estate Listings")

# Configure scraper parameters
scraper = FundaScraper(
    area="amsterdam", 
    want_to="rent", 
    find_past=False, 
    page_start=1, 
    n_pages=3, 
    min_price=500, 
    max_price=2000
)

# Run the scraper and save results to a CSV file
df = scraper.run(raw_data=False, save=True, filepath="test.csv")

# Display the DataFrame in Streamlit
st.write("This table shows the real estate listings scraped from Funda for Amsterdam with specified parameters.")
st.dataframe(df)
