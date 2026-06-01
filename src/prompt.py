from langchain_core.prompts import ChatPromptTemplate
from langfuse import Langfuse
from dotenv import load_dotenv

load_dotenv()

# Backup prompt
FALLBACK_TEMPLATE = """
You are an AI Email Writing Assistant.

Generate a professional email.

Return ONLY valid JSON in this format:

{{
    "subject": "",
    "email_body": "",
    "tone": ""
}}

User Email Request:
{email_request}

{format_instructions}
"""


def get_prompt():

    try:

        langfuse = Langfuse()

        # Fetch prompt from Langfuse
        lf_prompt = langfuse.get_prompt(

            name="ai-email-writing-assistant",

            label="production",

            cache_ttl_seconds=300
        )

        prompt = ChatPromptTemplate.from_template(
            lf_prompt.prompt
        )

        return prompt, lf_prompt

    except Exception:

        # Fallback if Langfuse fails
        prompt = ChatPromptTemplate.from_template(
            FALLBACK_TEMPLATE
        )

        return prompt, None


prompt, lf_prompt = get_prompt()