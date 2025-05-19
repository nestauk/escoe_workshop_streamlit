"""
Let's now learn how to structure our app using complex layouts/containers:
    - expanders
    - sidebar
    - multiple pages

We also learn how to password protect our app.
"""

## Package imports
import streamlit as st  # For building the web app
import pandas as pd  # For simple data manipulation
from PIL import Image  # For loading images
import altair as alt  # For creating interactive charts with Altair
from streamlit_option_menu import option_menu  # For creating a sidebar menu

# Import the utility functions
from utils.getters import generate_random_data
from utils.fonts_setup import nestafont, NESTA_COLOURS

# We setup the fonts and colours for the altair plots in the utils/fonts_setup.py file
alt.themes.register("nestafont", nestafont)
alt.themes.enable("nestafont")
colours = NESTA_COLOURS

# Configure your browser tab by adding a title, changing the layout, and adding an icon to appear on your browser tab
st.set_page_config(
    page_title="Structuring a streamlit dashboard",
    layout="wide",
    page_icon=":construction:",
)


def create_app_with_structure():
    """
    This function will setup a Streamlit app with expanders, sidebar and multiple pages.
    """

    # Add a title to the app
    st.title("Let's learn how to structure our app :bulb:")

    st.write(
        "You can use the side bar to navigate between the different pages of the app."
    )

    with st.sidebar:
        side_bar_options = option_menu(
            menu_title="Side menu title",
            options=[
                "About this app",
                "Analysis",
                "Metadata",
            ],  # The options to be displayed in the sidebar
            icons=[
                "house",
                "gear",
                "info-circle",
            ],  # The icons to be displayed next to the options. You can select from: https://icons.getbootstrap.com/
            default_index=0,  # Defaults to the "About this app" page
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
        st.write(
            """
        This is a simple app that shows how to structure a Streamlit app using:
                 
        - expanders
                
        - sidebars
                
        - multiple pages
                 
        You can typically use this first page to explain what the app is about and how to use it.

        """
        )

    elif side_bar_options == "Analysis":

        st.markdown("## This can be our analysis page")
        with st.expander("Click here to know more!"):
            st.write(
                """
            This is an example of an expander. You can add any content you want inside it, including text, images, charts, etc.
            
            You can add multiple expanders to your app.
            """
            )

            # Loading the data
            data = generate_random_data()

            # Create a slider to select a range of years
            min_year, max_year = st.slider(
                "Select the range of dates",
                min_value=data["year"].min(),
                max_value=data["year"].max(),
                value=(2017, 2020),  # default selected range
                step=1,  # shows values in increments of 1 year
            )

            # List of unique genders
            genders = list(data["gender"].unique())

            # Initialize session state for gender and set it to "F"
            if "gender" not in st.session_state:
                st.session_state.gender = "F"

            # Creating a select box for gender
            gender_selection = st.selectbox(
                "Choose one gender",
                options=genders,
                index=genders.index(st.session_state.gender),
                key="gender",
            )  # using session state allows for the value of gender selection not to change when the slider is changed

            # Filter data by year range
            filtered_data_by_year = data[
                (data["year"] >= min_year) & (data["year"] <= max_year)
            ].copy()

            # Compute average income for selected gender within selected years
            avg_income_selected_gender = filtered_data_by_year[
                filtered_data_by_year["gender"] == gender_selection
            ]["yearly_income"].mean()

            # Compute overall average income across all genders within selected years
            avg_income_overall = filtered_data_by_year["yearly_income"].mean()

            # Prepare data for chart
            chart_data = pd.DataFrame(
                {
                    "Group": [f"{gender_selection}", "Overall"],
                    "Average Income": [avg_income_selected_gender, avg_income_overall],
                }
            )

            # Creating the altair horizontal bar chart
            bar_chart = (
                alt.Chart(chart_data)
                .mark_bar(size=50)
                .encode(
                    x=alt.X("Average Income:Q", title="Average Income"),
                    y=alt.Y(
                        "Group:N",
                        title="Group",
                        sort=["Overall", gender_selection],
                        scale=alt.Scale(paddingInner=0.3),  # adds space between bars
                    ),
                    color=alt.Color(
                        "Group:N",
                        scale=alt.Scale(
                            domain=["Overall", gender_selection],
                            range=[NESTA_COLOURS[10], NESTA_COLOURS[0]],
                        ),
                        legend=None,
                    ),
                )
                .properties(
                    title="Average Income: Selected Gender vs. Overall",
                    width=600,
                    height=300,
                )
            )

            # Displaying the altair chart
            st.altair_chart(bar_chart, use_container_width=False)

    else:
        st.markdown("## This can be our metadata page")

        st.write(
            """
        When putting together a dashboard, it is really important to share some information about your data so users can correctly interpret it.
        
        You can:
        - describe the data and its caveats
        - describe the methodology used to process the data
        - provide information about the variables and values in your data
        """
        )


# Let's setup password protection on the sidebar
pwd = st.sidebar.text_input("Password:", type="password")
# st.secrets reads it in from the toml folder, and then runs the create_app_with_structure() function if the password matches.
if pwd == st.secrets["PASSWORD"]:
    create_app_with_structure()
elif pwd == "":  # avoids error when app is first opened
    pass
else:
    st.sidebar.error("Password incorrect. Please try again.")
