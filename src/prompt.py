import os
from dotenv import load_dotenv
from langfuse import Langfuse
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

print("AUTH CHECK:")
print(langfuse.auth_check())

lf_prompt = langfuse.get_prompt(
    "AI Email Writing Assistance Chatbot"
)

prompt = ChatPromptTemplate.from_template(
    lf_prompt.prompt
)