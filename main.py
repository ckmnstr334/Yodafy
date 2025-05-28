import streamlit as st
import open_ai as ai

output = ""

st.header("Yodafy", divider="green")
st.subheader("The English - Yoda Translator")

api_key = st.text_input("Your Open AI API Key, unleash it, you must.")
input = st.text_area("The text you wish to translate, into the box you must input:")
button = st.button("Yodafy")
lightsaber = st.image("images/lightsaber.png")

if button:
    if input == "":
        output = "Empty, the field must not be"
    else:
        output = ai.ask_assistant(input, api_key)

st.write(output)