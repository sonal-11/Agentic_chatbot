from src.langgraph.state.state import State


class BasicChatbotNode:
    """basic chatbot login implementation"""

    def __init__(self, model):
        self.llm = model

    def process(self, state:State)->dict:
        """process the input state and generates a chatbot response"""

        return {"messages": self.llm.invoke(state["messages"])}

