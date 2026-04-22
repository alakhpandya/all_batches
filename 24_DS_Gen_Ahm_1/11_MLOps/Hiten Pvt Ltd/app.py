import streamlit as st

st.title("Sample Streamlit Project")
st.text("In this project we will create a basic frontend app using this awesome library!")

st.text_input(label="", placeholder=None)
first_name = st.text_input(label="", placeholder="First Name")
last_name = st.text_input(label="", placeholder="Last Name")
age = st.number_input(label="age", placeholder="Age", min_value=1, max_value=50, value=None)

if st.button("Submit"):
    if age >= 18:
        st.text(f"Hello Mr.{last_name}")
    else:
        st.text(f"Hi dear {first_name}")