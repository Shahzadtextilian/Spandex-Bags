import streamlit as st 

# Function to calculate Spandex percentage
def calculate_spandex_percentage(yarn_count, spandex_denier, draft):
    try:
        spandex_percentage = (yarn_count * spandex_denier * 100) / (5314.5 * draft)
        return spandex_percentage
    except ZeroDivisionError:
        st.error("Draft value cannot be zero!")
        return None

# Function to calculate the number of bags
def calculate_no_of_bags(spandex_quantity, spandex_percentage):
    try:
        spandex_yield = 99  # Fixed Spandex Yield as 99%
        no_of_bags = (spandex_quantity * 100 * 100) / (spandex_percentage * spandex_yield * 45.36)
        return no_of_bags
    except ZeroDivisionError:
        st.error("Spandex Percentage cannot be zero!")
        return None

# Streamlit app layout
st.title("Spandex % and No. of Bags Calculator")
st.write("Enter the values below to calculate Spandex percentage and the number of bags.")

# Input fields
yarn_count = st.number_input("Yarn Count:", min_value=0.0, format="%.2f")
spandex_denier = st.number_input("Spandex Denier:", min_value=0.0, format="%.2f")
draft = st.number_input("Spandex Draft:", min_value=0.0, format="%.2f")
spandex_quantity = st.number_input("Spandex Quantity (Kgs):", min_value=0.0, format="%.2f")

# Calculate Spandex percentage
if st.button("Calculate Spandex %"):
    spandex_percentage = calculate_spandex_percentage(yarn_count, spandex_denier, draft)
    if spandex_percentage is not None:
        st.write(f"Spandex %: {spandex_percentage:.2f}%")

# Calculate Number of Bags
if st.button("Calculate No. of Bags"):
    spandex_percentage = calculate_spandex_percentage(yarn_count, spandex_denier, draft)
    if spandex_percentage is not None:
        no_of_bags = calculate_no_of_bags(spandex_quantity, spandex_percentage)
        if no_of_bags is not None:
            st.write(f"No. of Bags: {no_of_bags:.2f}")

# Footnote
st.write("Developed by Shahzad Mahmood")
