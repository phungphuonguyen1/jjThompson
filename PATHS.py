NAVBAR_PATHS = {
    'Trang chủ':'home',
    'Tính toán': 'calculator',
    'Liên hệ': 'about_me'
}

SETTINGS = {
    'OPTIONS':'options',
    'CONFIGURATION':'configuration'
}

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
