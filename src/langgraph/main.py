import streamlit as st
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUi

def load_langgraph_agenti_ai_app():
    """loads ui"""

    ui=LoadStreamlitUi()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("failed to load user input from ui")
        return
    
    user_message = st.chat_input("Enter Your Message")

    
