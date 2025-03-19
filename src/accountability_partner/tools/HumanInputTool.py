from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class CrewInput(BaseModel):
    """Input schema for MyCustomTool."""
    initial_message: str = Field(..., description="Initial message fromt the person.")

def ask_human(question: str) -> str:
    human_response = input(question + "\nUser: ")
    if human_response:
        return human_response

class HumanInputTool(BaseTool):
    name: str = "Ask Human follow up questions to get additional context."
    description: str = (
        "Use this tool to ask follow-up questions to the human in case additional context is needed."
    )

    def _run(self, question: str) -> str:
        return ask_human(question)
