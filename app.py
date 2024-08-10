import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

st.title("OpenAI API with Streamlit")

# Input field for the prompt
prompt = st.text_input("Enter a prompt for GPT:")

if st.button("Generate"):
    if prompt:
        # Call the OpenAI API with the provided prompt
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose any available engine
            prompt=prompt,
            max_tokens=150  # Adjust the number of tokens as needed
        )

        # Display the generated text
        st.write(response.choices[0].text)
    else:
        st.warning("Please enter a prompt.")
