from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.runnables import RunnableLambda
import config

class ChatHandler:
    def __init__(self):
        self.model = ChatGroq(model="llama3-8b-8192")
        self.memory = MemorySaver()
        
        # Define prompt template
        self.prompt_template = ChatPromptTemplate([
            ("system", "You are a friendly AI assistant. Be concise."),
            MessagesPlaceholder(variable_name="messages"),
        ])
        
        # Define a new graph
        self.workflow = StateGraph(state_schema=MessagesState)
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self.call_model)
        self.app = self.workflow.compile(checkpointer=self.memory)

    def call_model(self, state: MessagesState):
        """Calls the AI model with a given state."""
        prompt = self.prompt_template.invoke(state)
        response = self.model.invoke(prompt)
        return {"messages": response}

    def get_response(self, user_message):
        """Handles chat messages and gets response from AI."""
        input_messages = [HumanMessage(user_message)]
        config = {"configurable": {"thread_id": "abc123"}}
        output = self.app.invoke({"messages": input_messages}, config)
        ai_message = output["messages"][-1]  # Last response from AI
        return ai_message.content
