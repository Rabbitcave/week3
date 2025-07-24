import streamlit as st
import math

st.title("📐 Area Calculator with Units")

# Unit options
units = ["meters", "centimeters", "feet", "inches"]
selected_unit = st.selectbox("Select measurement unit", units)

# Function Definitions
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# Shape selection
shape = st.selectbox("Select a shape", ["Circle", "Rectangle", "Triangle"])

# Input and calculation based on shape
if shape == "Circle":
    radius = st.number_input(f"Enter radius ({selected_unit})", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_circle(radius)
        st.success(f"Area of Circle: {area:.2f} square {selected_unit}")

elif shape == "Rectangle":
    length = st.number_input(f"Enter length ({selected_unit})", min_value=0.0, format="%.2f")
    width = st.number_input(f"Enter width ({selected_unit})", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_rectangle(length, width)
        st.success(f"Area of Rectangle: {area:.2f} square {selected_unit}")

elif shape == "Triangle":
    base = st.number_input(f"Enter base ({selected_unit})", min_value=0.0, format="%.2f")
    height = st.number_input(f"Enter height ({selected_unit})", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_triangle(base, height)
        st.success(f"Area of Triangle: {area:.2f} square {selected_unit}")
