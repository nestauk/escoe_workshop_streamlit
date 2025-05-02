"""
Let's now learn how to structure our app using complex layouts/containers:
    - expanders
    - sidebar
    - multiple pages

We also learn how to password protect our app.
"""

## Package imports
import streamlit as st # For building the web app
import pandas as pd   # For simple data manipulation
from PIL import Image # For loading images
import altair as alt
from streamlit_option_menu import option_menu
import os

# Import the utility functions
from utils.getters import generate_random_data
from utils.fonts_setup import nestafont, NESTA_COLOURS

# We setup the fonts and colours for the app in the utils/fonts_setup.py file
alt.themes.register("nestafont", nestafont)
alt.themes.enable("nestafont")
colours = NESTA_COLOURS

# Configure your browser tab by adding a title, changing the layout, and adding an icon to appear on your browser tab
st.set_page_config(page_title='Structuring a streamlit dashboard', layout = "wide", page_icon=':construction:')

def create_app_with_structure():
    """
    This function will setup a very a Streamlit app with expanders, sidebar and multiple pages.
    """

    # Add a title to the app
    st.title("Let's learn how to structure our app :bulb:")

    st.write("You can use the side bar to navigate between the different pages of the app.")

    with st.sidebar:
        side_bar_options = option_menu (
            menu_title = "Side menu title",
            options = ["About this app", "Analysis", "Metadata"], # The options to be displayed in the sidebar
            icons = ["house", "gear", "info-circle"],   # The icons to be displayed next to the options. You can select from:
            default_index = 0, # Defaults to the "About this app" page
            orientation="vertical",
            styles={
                "container": {
                    "padding": "5!important",
                    "background-color": NESTA_COLOURS[12],
                },
                "icon": {"color": NESTA_COLOURS[10], "font-size": "25px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": NESTA_COLOURS[0]},
            },
        )

    if side_bar_options == "About this app":
        st.markdown("## Welcome to the app!")
        st.write("""
        This is a simple app that shows how to structure a Streamlit app using:
                 
        - expanders
                
        - sidebars
                
        - multiple pages
                 
        You can typically use this first page to explain what the app is about and how to use it.

        """)

    elif side_bar_options == "Analysis":

        st.markdown("## This can be our analysis page")
        with st.expander("Click here to know more!"):
            st.write("""
            This is an example of an expander. You can add any content you want inside it, including text, images, charts, etc.
            
            You can add multiple expanders to your app.
            """)

            # Loading the data
            data = generate_random_data()
    
            # Let's now add a slider and a multiselect
            genders = data["gender"].unique()
            st.markdown("## Let's learn about sliders and multiselects")
            min_year, max_year = st.slider(
                    "Select the range of dates",
                    min_value=data["year"].min(),
                    max_value=data["year"].max(),
                    value=(2017, 2020),  # default selected range
                    step=1 # shows values in increments of 1 year
                )
            
            gender_selection_multiselect = st.multiselect("Choose one or more genders", options = genders, default = genders)

            filtered_data_by_year_and_gender = data[
                (data['year'] >= min_year) &
                (data['year'] <= max_year) &
                (data['gender'].isin(gender_selection_multiselect))
            ]

            # Group by category (e.g., gender) and calculate mean income, or use any metric
            avg_income_by_gender_in_selection = filtered_data_by_year_and_gender.groupby('gender')['yearly_income'].mean().reset_index()

            # Altair horizontal bar chart
            bar_chart = alt.Chart(avg_income_by_gender_in_selection).mark_bar(size=50, color=NESTA_COLOURS[0]).encode(
                x=alt.X('yearly_income:Q', title='Average Income'),
                y=alt.Y('gender:N', title='Gender'),
            ).properties(
                title='Average income by gender in selected years',
                width=600,
                height=400,
            )
            st.altair_chart(bar_chart, use_container_width=True)
        
    else:
        st.markdown("## This can be our metadata page")

        st.write("""
        When putting together a dashboard, it is really important to share some information about your data so users can correctly interpret it.
        
        You can:
        - describe the data and its caveats
        - describe the methodology used to process the data
        - provide information about the variables and values in your data
        """
        )

# Let's setup password protection on the sidebar
pwd = st.sidebar.text_input("Password:", type="password")
# st.secrets reads it in from the toml folder, and then runs the streamlit_iod function if the password matches.
if pwd == st.secrets["PASSWORD"]:
  create_app_with_structure()
elif pwd == "": # avoids error when app is first opened
  pass
else:
  st.sidebar.error("Password incorrect. Please try again.")
