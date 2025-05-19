"""
Let's explore some of the commonly used features of Streamlit such as:
- Adding text and markdown
- Adding images
- Loading and printing data
- Creating interactive charts
- Adding sliders and select boxes for more interactivity

"""

## Package imports
import streamlit as st  # For building the web app
import pandas as pd  # For simple data manipulation
from PIL import Image  # For loading images
import altair as alt  # For creating interactive charts with Altair
import os

# Import the utility functions
from utils.getters import generate_random_data
from utils.fonts_setup import nestafont, NESTA_COLOURS

# We setup the fonts and colours for the altair plots in the utils/fonts_setup.py file
alt.themes.register("nestafont", nestafont)
alt.themes.enable("nestafont")


def my_simple_streamlit_app():
    """
    This function will setup a very simple Streamlit app.
    """

    # Configure your browser tab by adding a title, changing the layout, and adding an icon to appear on your browser tab
    st.set_page_config(
        page_title="Exploring Streamlit functionalities",
        layout="wide",
        page_icon=":nerd_face:",
    )

    # Add a title to the app
    st.title("The title of our page/web app/dashboard :nerd_face:")

    # You can add more text by using markdown
    st.markdown("## This is a markdown header")

    # Let's add some text
    st.write(
        "The purpose of this app is to learn the basics of Streamlit and how to use it to build a simple web app."
    )

    # Let's now load an image
    current_dir = os.getcwd()
    escoe_logo = Image.open(f"{current_dir}/images/escoe.jpg")
    st.image(escoe_logo, caption="ESCoE logo", width=300)

    # Let's add load and display some data
    st.markdown("## Let's load and display data")
    data = generate_random_data()
    st.dataframe(data.head())

    # Let's add a line chart
    st.markdown("## Let's add a line chart showing the average income per year")
    avg_income_per_year = data.groupby("year")["yearly_income"].mean().reset_index()

    income_line_chart = (
        alt.Chart(avg_income_per_year)
        .mark_line(point=True)
        .encode(
            x=alt.X("year:O", axis=alt.Axis(title="Year")),
            y=alt.Y(
                "yearly_income:Q",
                axis=alt.Axis(title="Average income"),
                scale=alt.Scale(domain=[0, 60_000]),
            ),
            color=alt.value(NESTA_COLOURS[0]),
            tooltip=["year", "yearly_income"],
        )
        .properties(title="Income grows every year", width=400, height=500)
    )

    st.altair_chart(income_line_chart, use_container_width=False)

    ## Can we center the chart?
    st.markdown("## Let's center the chart by introducing the concept of columns")
    col1, col2, col3 = st.columns(
        [1, 2, 1]
    )  # Adjust the ratio as needed - in this case column 2 is twice as wide as the others

    with col2:
        st.altair_chart(income_line_chart, use_container_width=True)

    # Let's now add a slider and a select box

    st.markdown("## Let's learn about sliders and select boxes")

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
            height=300,  # Increased height
        )
    )

    # Displaying the altair chart
    st.altair_chart(bar_chart, use_container_width=False)


my_simple_streamlit_app()
