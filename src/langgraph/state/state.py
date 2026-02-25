from pydantic import BaseModel, Field
from typing_extensions import TypedDict, list
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """represent the structure of the state used in graph"""
    message: Annotated[list, add_messages]