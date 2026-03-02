import streamlit as st
import os

from src.langgraph.ui.uiconfig import Config

class LoadStreamlitUi:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        print(self.config.get_page_title(), "page_tile")
        st.set_page_config(page_title='my app' + self.config.get_page_title(), layout='wide')
        st.header("🃏" + self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            ## llm selection

            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] ==  'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("select model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API KEY", type = "password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️⚠️ please enter your groq api key to proceed. dont have ? refer https://console.groq.com/keys")

            ## use case selection

            self.user_controls["selected_usecases"] = st.selectbox("Select Usecase", usecase_options)

            if self.user_controls["selected_usecases"] == 'Chatbot with Tool':
                self.user_controls['TAVILY_API_KEY'] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY", type="password")

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️⚠️ please enter your tavily api key to proceed. dont have ? refer https://app.tavily.com/home")
        return self.user_controls

