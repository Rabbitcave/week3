import streamlit as st
import re

st.title("📞 Phone Number Formatter")

# Input
phone_input = st.text_input("Enter a 10-digit number", max_chars=10)

# Proceed button
if st.button("Proceed"):
    def format_phone(number: str) -> str:
        if re.fullmatch(r"\d{10}", number):
            return f"({number[:3]}) {number[3:6]}-{number[6:]}"
        return "❌ Please enter exactly 10 digits."

    # Format and show result
    if phone_input:
        formatted = format_phone(phone_input)
        st.markdown(f"### Formatted Number:\n{formatted}")
    else:
        st.warning("Please enter a number before proceeding.")
