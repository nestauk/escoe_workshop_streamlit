"""
Let's now create a Streamlit dashboard to explore job adverts data.
"""

# Package imports
import streamlit as st
import pandas as pd
import datetime
import altair as alt

# Configuring the browser tab
st.set_page_config(
    page_title="Jobs data dashboard", layout="wide", page_icon=":briefcase:"
)


# You can call the function presented below to load the data into the app
# We do @st.cache_data to cache the data so that it is not loaded every time we run the app
# This is particularly useful with larger data
@st.cache_data(show_spinner="Loading Data")
def load_and_preprocess_jobs_data() -> pd.DataFrame:
    """
    Load jobs data and creates two additional columns with the year and year/month of the job posting.

    Returns:
        pd.DataFrame: DataFrame containing the jobs data.
    """
    jobs_data = pd.read_parquet(
        "s3://nesta-open-data/escoe_workshop/data/data_jobs_df.parquet"
    )
    jobs_data["year_month"] = jobs_data["date_posted"].dt.to_period("M")
    jobs_data["year"] = jobs_data["date_posted"].dt.year

    return jobs_data


def create_jobs_data_dashboard():
    """
    This function will setup a Streamlit dashboard to explore job adverts data.
    """
    st.title(":briefcase: Jobs data dashboard :briefcase:")

    # This adds a spinner into the webpage to let the user know it's updating
    with st.spinner("Updating Report..."):
        # Load the data
        jobs_data = load_and_preprocess_jobs_data()
        st.dataframe(jobs_data.head())


create_jobs_data_dashboard()
