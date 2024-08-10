import openai
import streamlit as st
import json
import requests

# Initialize API key
openai.api_key = st.secrets['api_key']

# Set up the Streamlit app
st.title("Recipes")
st.header("Getting you deliciously fed")

# Input text area for recipe prompt
prompt = st.text_area(
    "Tell me what you would like to eat, and I'll help you decide! Specify Breakfast, lunch, or dinner."
)

# Check the length of the prompt
if len(prompt) > 1000:
    st.warning("Input too large. Please write less than 1000 characters and try again.")
else:
    if st.button("Show options"):
        # Define the API endpoint and payload
        url = "https://api.openai.com/v1/chat/completions"
        payload = json.dumps({
            "model": "gpt-4",
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

        # Make the API request
        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            response_data = response.json()
            generated_text = response_data["choices"][0]["message"]["content"].strip()
            st.info(generated_text)
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")

# Initialize or update the session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Input text box for chat
user_input = st.text_input("What is up?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Display user message
    st.write(f"**User:** {user_input}")

    # Make an API request to get the assistant's reply
    if 'openai_model' in st.session_state:
        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=st.session_state.messages
        )
        response_data = response.choices[0].message['content']
        st.session_state.messages.append({"role": "assistant", "content": response_data})
        # Display assistant message
        st.write(f"**Assistant:** {response_data}")

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


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})