from dotenv import load_dotenv
from langfuse import get_client
from langfuse.langchain import CallbackHandler
from langchain_core.output_parsers import PydanticOutputParser

from src.prompt import prompt
from src.model import llm
from src.schema import EmailResponse

load_dotenv()

langfuse = get_client()
langfuse_callback = CallbackHandler()

parser = PydanticOutputParser(pydantic_object=EmailResponse)

chain = prompt | llm | parser


def generate_email(email_request):
    payload = {
        "email_topic": email_request,
        "format_instructions": parser.get_format_instructions()
    }

    result = chain.invoke(
        payload,
        config={
            "callbacks": [langfuse_callback],
            "tags": ["ai-email-writer"],
            "metadata": {
                "project": "AI Email Writing Assistant"
            }
        }
    )

    langfuse.flush()
    return result