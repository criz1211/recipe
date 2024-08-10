import openai 
import streamlit as st
import json
import requests

# Set up your OpenAI API key
#openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = st.secrets['api_key']
#openai.api_key = "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"

def get_openai_response(prompt):
    try:
        # Make a request to OpenAI's completions endpoint
        response = openai.Completion.create(
            model="text-davinci-003",  # Use the appropriate model, e.g., "text-davinci-003"
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
