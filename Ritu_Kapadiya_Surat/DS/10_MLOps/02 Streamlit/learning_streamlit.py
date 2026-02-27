import streamlit as st
import datetime

st.title("Frontend using Streamlit")
st.text("We will try to create a basic front-end that takes some input & submit them to the server.")

st.text_input(label="", placeholder="First Name")
st.text_input(label="Last Name")

age = st.slider("How old are you?", 0, 130, 25)

if age < 18:
    category = "Child"
elif age >= 18 and age <40:
    category = "Adult"
elif age >= 40 and age <60:
    category = "Middle Aged"
else:
    category = "Senior"

st.write("You are a", category, "person")

# Slider with "min" & "max"
values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)


d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)

hello = st.button("Greet")
if hello:
    st.write("Hello Ritu!")
else:
    st.write("")

left, center, right = st.columns(3)
left.text_input("Primary Phone")
center.text_input("Secondary Phone")
right.text_input("Mobile")