# Import necessary libraries:
import streamlit as st
import requests
import openai

# Set page config:
st.set_page_config(
    page_title="Car Deals Finder",
    page_icon=":car:",
    layout="wide",
)

# Add a title and some text:
st.title("Car Deals Finder App 🚗")
st.text("Enter your API key and location to find car deals near you")

# Input for API key:
API_key = st.text_input("OpenAI API Key: ", type="password")

# Setup OpenAI API:
openai.api_key = API_key

# Declaration of the two messages for AI model:
system_message = {
    'role': 'system',
    'content': 'You are a helpful assistant.'
}
user_message = {
    'role': 'user',
    'content': 'find car deals near'
}

# Input for location:
location = st.text_input("Enter your location:")
if location:
    user_message['content'] += " " + location

# Generate the AI message if both the key and location are entered:
if API_key and location:
    response = openai.ChatCompletion.create(
      model="text-davinci-003",
      messages=[system_message, user_message]
    )
    message_content = response.choices[0].message.content.strip()
    st.write(message_content)