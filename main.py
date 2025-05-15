import streamlit as st
import open_ai as ai

output = ""

st.title("Yodafy")
st.subheader("The English - Yoda Translator")

input = st.text_area("The text you wish to translate, into the box you must input:")
button = st.button("Yodafy")

if button:
    if input == "":
        output = "Empty, the field must not be"
    else:
        output = ai.ask_assistant(input)

st.write(output)