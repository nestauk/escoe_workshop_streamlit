# 📊 ESCoE workshop Streamlit tutorial

This repository was developed for a [workshop session for ESCoE](https://www.escoe.ac.uk/events/data-visualisation-and-data-labelling-for-machine-learning-applications-workshop-with-nesta/) on the 20th May 2025.


# 📈 About Streamlit

[Streamlit](streamlit.io) is a powerful and user-friendly Python library used for building interactive data applications with minimal code. It enables data visualisation enthusiasts coding in Python to quickly create and deploy data dashboards.

In this session we will cover how to visualise data for decision making and how to communicate insights effectively. We will also cover key functionalities in Streamlit such as graphics interactivity, user selection and theme customisation, enabling participants to build engaging and user-friendly dashboards.

# 📝 Instructions for the workshop

## ✅ Requirements

Your system must have:

- [python](https://www.python.org/downloads/) installed
- [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install#windows-installation) installed
- access to run commands in the terminal

You need to set up:
- A GitHub account

It is helpful to have access to a code editor, such as [VSCode](https://code.visualstudio.com/download) or [Sublime Text](https://www.sublimetext.com/). Any code editor of your choice works well!

## 🛠️ Setup

In your terminal, you will need to run the following commands to set up the environment and install the package requirements.

1. Fork this repository:

Click fork on the upper right corner of the page to create a copy of this repository in your GitHub account.

2. Clone this repository:

`git clone git@github.com:YOUR_GITHUB_HANDLE/escoe_workshop_streamlit.git`

don't forget to change the above by replacing `YOUR_GITHUB_HANDLE` with your GitHub username.

2. Create a conda environment:

`conda create --name streamlit_escoe_workshop python==3.13`

3. Activate your conda environment:

`conda activate streamlit_escoe`

4. Install the package requirements:
`pip install -r requirements.txt`

# 🤓 Workshop activities

1. Explore the `01_learn_basics_about_streamlit.py` file to learn the basics of Streamlit.
This file contains basic features of Streamlit, and you can run it with

`streamlit run 01_learn_basics_about_streamlit.py`.

2. Explore the `02_structuring_app.py` to learn more about how to structure your app using expanders, side bar and multiple pages.
You will also learn how to password protect your app. Run this script with 

`streamlit run 02_structuring_app.py`.

3. Create a dashboard in `03_building_your_own_app.py` to explore job adverts data (or any other dataset you might have in mind). This task is fairly open, so feel free to explore some of the following features or other features you might find interesting (you can check the next section for a summary of Streamlit's features):
    - Creating a sidebar with multiple pages:
        - One about the dashboard
        - A second page about dataset and showcasing the top 10 lines of data
        - One or more pages showing insights through data visualisation
    - Create metrics, such as
        - Number of job adverts
        - Average salary
    - Get creative with plotting, using your favourite plotting library (e.g. `plotly`, `matplotlib`, `altair`, etc.). A few examples include plotting:
        - Number of job adverts over time
        - Average salary over time/ by job title/ by location/ occupation
        - Average salary by occupation for the top 10 occupations with highest salaries
    - Password protect your app (or just the insights page!)
    - Change the theme/colours of your app
    - Deploy your app to [Streamlit Cloud](https://streamlit.io/cloud)

*Have fun getting creative with Streamlit!* 🎉

# 📚 Resources and quick summary of Streamlit's features

The best way to see what Streamlit can do is to explore the [gallery](https://streamlit.io/gallery) as you can explore different web apps in action and access the respective app source code, to understand how each feature was created.

There is a handy [cheat sheet](https://docs.streamlit.io/library/cheatsheet) which summarises a lot of the code you will need, but here are some of the features which are most useful to get you started:
- **Interactive visualisations**: Inserting [interactive and static graphs](https://docs.streamlit.io/library/api-reference/charts). Streamlit allows to easily add:
    - `altair`, `bokeh`, `plotly`, `pydeck` and `matplotlib` plots, in addition to Streamlit's in-built graphing functions.
    - maps using packages such as `folium` and `deck.gl`.
- **Tables**: Inserting both [static and interactive tables either directly from `pandas` or other libraries (e.g. `plotly`) as well as having large metrics printed](https://docs.streamlit.io/library/api-reference/data).
- **User selection**: [User selections](https://docs.streamlit.io/library/api-reference/widgets) such as radio buttons, uploading/downloading data, camera input, text input
- **Password protection**: [Adding passwords (and usernames) to apps to protect them](https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso)
- **Create multi-page apps**: [Multi-page apps](https://blog.streamlit.io/introducing-multipage-apps/)
- **Adding media**: Easily add in [images, videos and audio](https://docs.streamlit.io/library/api-reference/media).
- **Text blocks**: Lots of flexibility with the blocks of text, you can add in [text with variables that can be changed by other user selections, LaTeX, code blocks](https://docs.streamlit.io/library/api-reference/text).
- **Customise the theme**: You can change the font and theme of the Streamlit app with an overall [theme config](https://docs.streamlit.io/library/advanced-features/theming).
- **Containers layout**: [You can be very specific in the layout with containers](https://docs.streamlit.io/library/api-reference/layout).
- **Progress measures**: [You can add in progress measures when loading](https://docs.streamlit.io/library/api-reference/status) - you can even have [celebratory balloons](https://docs.streamlit.io/library/api-reference/status/st.balloons)!

