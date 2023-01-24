import openai
import streamlit as st

openai.api_key = "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"
def openai_create(prompt):
    with st.spinner('We are planning the best possible trip for you ...'):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=1,
        stop=[" Human:", " AI:"]
        )
    print("Response ->"+response.choices[0].text)
    return response.choices[0].text

st.markdown("# Health  GPT3")


st.write(openai_create("treatment for fever"))