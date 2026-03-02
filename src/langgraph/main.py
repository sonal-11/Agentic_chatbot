import streamlit as st
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUi
from src.langgraph.llms.groqllm import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.streamlitui.display_results import DisplayResultStreamlit

def load_langgraph_agenti_ai_app():
    """loads ui"""

    ui=LoadStreamlitUi()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("failed to load user input from ui")
        return
    
    user_message = st.chat_input("Enter Your Message")

    if user_message:
        try:
            ## configure a llm
            obj_llm_config = GroqLLM(user_control_inputs=user_input)
            model = obj_llm_config.get_llm_models()

            if not model:
                st.error("Model could not be initialized")
                return
            
            # initialize and setup the graph bases on usecase

            use_case = user_input.get("selected_usecases")
            if not use_case:
                st.error("usecase could not be initialized")
                return
            
            # initialize the graph builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(use_case)
                DisplayResultStreamlit(use_case, graph, user_message).display_results_on_ui()
            except Exception as e:
                st.error(f" Error: Graph setup failed as {e}")
                return
            
        except Exception as e:
            st.error(f" Error: setup failed as {e}")
            return


    
