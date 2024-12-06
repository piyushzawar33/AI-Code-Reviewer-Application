import streamlit as st
import google.generativeai as genai

f = open(r"Gemini key.txt")
key = f.read()

genai.configure(api_key = key)

st.title("An AI Code Reviewer")

sys_prompt = """You are a helpful AI code reviewer. Students will submit their code for review.
                You are expected to review the code and provide feedback on potential bugs along with suggestions for fixes.
                should also provide bug report and the fixed code snippets.
                In case if a student ask any question outside the coding, polietly decline and ask them to ask the questions regarding the code only."""

model = genai.GenerativeModel(model_name = "gemini-1.5-pro-latest",
                              system_instruction = sys_prompt)

user_prompt = st.text_area("Enter your Python Code here...", height = 100,
              placeholder = "Type your code here")

btn_click = st.button("Review your code")

if btn_click == True:
    response = model.generate_content(user_prompt)
    st.write(response.text)
