import streamlit as st
import openai 
import json
import requests

openai.api_key = "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"

st.title("recipes")
st.header("getting you deliciously fed")

prompt = st.text_area(
"Tell me what you would like to eat and I'll help you decide! Specify Breakfast, lunch or dinner"
)
if len(prompt) < 1000:
    if st.button("show options"):
        url = "https://api.openai.com/v1/chat/completions"
        payload = json.dumps({
            "model": "gpt-4",  # Correct model identifier for GPT-4
            "messages": [
                {
                    "role": "system",
                    "content": "Act like my personal chef and give me delicious food suggestion based on the following prompt"
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
            'Authorization': f'Bearer {api_key}'
        }
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            response_data = response.json()
            generated_text = response_data["choices"][0]["message"]["content"].strip()
            st.info(generated_text)
            #print(generated_text)
            #return generated_text
        else:
            st.warning(
                "Input too large"

            )
            #print(f"Error from OpenAI: {response.status_code}")
            #print(f"Error from OpenAI: {response.content.decode()}")
            #return "Error in generating text."
