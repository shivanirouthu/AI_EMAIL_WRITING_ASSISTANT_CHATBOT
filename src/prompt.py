from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are an AI Email Writing Assistant.

Write a professional email based on the user request.

User request:
{email_topic}

Return the response in this format:
{format_instructions}
""")