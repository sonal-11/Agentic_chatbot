import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_control_inputs):
        self.user_control_input = user_control_inputs

    def get_llm_models(self):
        try:
            groq_api_key = self.user_control_input["GROQ_API_KEY"]
            selected_groq_model = self.user_control_input['selected_groq_model']
            if groq_api_key=='' or os.environ["GROQ_API_KEY"] == '':
                st.error("enter groq api key")

            llm= ChatGroq(api_key=groq_api_key, model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Ocuured with Exception as {e} ")
        return llm
