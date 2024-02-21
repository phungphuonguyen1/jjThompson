import streamlit as st
import utils as utl
from views import home,about_me,calculator,options,configuration
# Add CSS styles for the navigation bar
st.markdown(
    """
    <style>
        .navbar {
            font-family: 'Your Desired Font', sans-serif;
            background-color: #3498db;  /* Change the background color as needed */
            padding: 10px;
            color: #ffffff;  /* Change the text color as needed */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create the navigation bar
selected_option = st.sidebar.radio("Navigation", list(NAVBAR_PATHS.keys()))

# Display content based on the selected option
if selected_option in NAVBAR_PATHS:
    st.write(f"Selected option: {selected_option}")
    # Add logic to display content based on the selected option

elif selected_option in SETTINGS:
    st.write(f"Selected settings: {selected_option}")
    # Add logic to display content based on the selected setting

st.set_page_config(layout="wide", page_title='JJ Thomson',page_icon='🤓')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

# hide main menu and footer
hide_menu_style= """
    <style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)


def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "calculator":
        calculator.load_view()
    elif route == "about_me":
        about_me.load_view()
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()
        
navigation()
