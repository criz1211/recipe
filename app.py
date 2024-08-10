import openai 
import streamlit as st
import json
import requests

# Set your OpenAI API key (for security, consider using st.secrets or environment variables)
openai.api_key = "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"

st.title("Recipes")
st.header("Getting you deliciously fed")

prompt = st.text_area(
    "Tell me what you would like to eat, and I'll help you decide! Specify Breakfast, lunch, or dinner."
)

if len(prompt) > 1000:
    st.warning("Input too large. Please write less than 1000 characters and try again.")
else:
    if st.button("Show options"):
        url = "https://api.openai.com/v1/chat/completions"
        payload = json.dumps({
            "model": "gpt-4",  # Correct model identifier for GPT-4
            "messages": [
                {
                    "role": "system",
                    "content": "Act like my personal chef and give me delicious food suggestions based on the following prompt:"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.5,
            "max_tokens": 3500,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai.api_key}'
        }

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()  # Raises an error for bad status codes
            response_data = response.json()
            generated_text = response_data["choices"][0]["message"]["content"].strip()
            st.info(generated_text)
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
