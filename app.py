import streamlit as st

# Title of the web app
st.title("Hello, Streamlit!")

# A simple text element
st.write("This is your first Streamlit app.")

# A simple number input and display
number = st.number_input("Pick a number", 0, 100)
st.write(f"You selected the number: {number}")

# Display a button
if st.button("Say Hello"):
    st.write("Hello, world!")

# A slider to select a range of numbers
range_val = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write(f"Selected range: {range_val}")
