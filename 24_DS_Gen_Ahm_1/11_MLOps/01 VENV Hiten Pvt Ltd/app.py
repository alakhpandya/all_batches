import streamlit as st

st.title("Sample Streamlit Project")
st.text("In this project we will create a basic frontend app using this awesome library!")

# st.text_input(label="Test Input", placeholder=None)
# first_name = st.text_input(label="", placeholder="First Name")
# last_name = st.text_input(label="", placeholder="Last Name")
# age = st.number_input(label="age", placeholder="Age", min_value=1, max_value=50, value=None)

# if st.button("Submit"):
#     if age >= 18:
#         st.text(f"Hello Mr.{last_name}")
#     else:
#         st.text(f"Hi dear {first_name}")


col1, col2, col3 = st.columns(3)
# with col1:
#     first_name = st.text_input(label="", placeholder="First Name")
# with col2:
#     last_name = st.text_input(label="", placeholder="Last Name")
# with col3:
#     age = st.number_input(label="age", placeholder="Age", min_value=1, max_value=50, value=None)

first_name = col1.text_input(label="", placeholder="First Name")
last_name = col2.text_input(label="", placeholder="Last Name")
age = col3.number_input(label="age", placeholder="Age", min_value=1, max_value=50, value=None)

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)

# Slider with "min" & "max"
values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)


import datetime

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)

if st.button("Submit"):
    if age >= 18:
        st.text(f"Hello Mr.{last_name}")
    else:
        st.text(f"Hi dear {first_name}")

