import openai 
import streamlit as st
import json
import requests

# Set up your OpenAI API key
#openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = st.secrets['api_key']


def get_openai_response(prompt):
    try:
        # Make a request to OpenAI's completions endpoint
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Or another model if required
            prompt=prompt,
            max_tokens=150  # Adjust the number of tokens as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.title("OpenAI Completion with Streamlit")

# Input from the user
user_prompt = st.text_area("Enter your prompt:", "Hello, how are you?")

# Button to submit the request
if st.button("Get Response"):
    if not openai.api_key:
        st.error("API key is not set. Please set the OPENAI_API_KEY environment variable.")
    else:
        # Get the response from OpenAI
        result = get_openai_response(user_prompt)
        st.write("Response from OpenAI:")
        st.write(result)