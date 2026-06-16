from src.prompt import prompt
from src.model import llm
from src.email_parser import EmailResponse
from langchain_core.output_parsers import PydanticOutputParser
from langfuse import Langfuse

langfuse = Langfuse()

parser = PydanticOutputParser(
    pydantic_object=EmailResponse
)

chain = prompt | llm | parser


def generate_email(email_request):

    trace = langfuse.trace(
        name="email-generation"
    )

    payload = {
        "email_request": email_request,
        "format_instructions": parser.get_format_instructions()
    }

    result = chain.invoke(payload)

    trace.update(
        input=payload,
        output=result.model_dump()
    )

    langfuse.flush()

    print("RESULT TYPE:", type(result))
    print("RESULT:", result)

    return result