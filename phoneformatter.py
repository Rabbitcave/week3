import streamlit as st
import re

st.title("📞 Phone Number Formatter")

# User input
phone_input = st.text_input("Enter a 10-digit number", max_chars=10)

# Validation and formatting
def format_phone(number: str) -> str:
    if re.fullmatch(r"\d{10}", number):
        return f"({number[:3]}) {number[3:6]}-{number[6:]}"
    return "❌ Please enter exactly 10 digits."

# Show result
if phone_input:
    formatted = format_phone(phone_input)
    st.markdown(f"### Formatted Number:\n{formatted}")
