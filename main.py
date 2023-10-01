import streamlit as st
import utils as utl
from views import home,about_me,calculator,options,configuration

st.set_page_config(layout="wide", page_title='JJ Thomson')
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
    elif route == "about":
        calculator.load_view()
    elif route == "analysis":
        about_me.load_view()
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()
        
navigation()
