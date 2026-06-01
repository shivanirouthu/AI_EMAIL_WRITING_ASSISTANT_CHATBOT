from src.model import llm
from src.schema import EmailResponse
from src.prompt import prompt, lf_prompt

from langchain_core.output_parsers import PydanticOutputParser

import json

# Parser
parser = PydanticOutputParser(
    pydantic_object=EmailResponse
)

# Chain
chain = prompt | llm | parser


def generate_email(email_request: str):

    metadata = {
        "project":
        "AI Email Writing Assistance Chatbot"
    }

    if lf_prompt:

        metadata.update({

            "prompt_name":
            lf_prompt.name,

            "prompt_version":
            str(lf_prompt.version)
        })

    result = chain.invoke(

        {
            "email_request": email_request,

            "format_instructions":
            parser.get_format_instructions()
        },

        config={

            "tags": [
                "ai-email-assistant"
            ],

            "metadata": metadata
        }
    )

    return result


if __name__ == "__main__":

    email_request = input(
        "Enter your email request: "
    )

    output = generate_email(
        email_request
    )

    print(
        json.dumps(
            output.model_dump(),
            indent=4
        )
    )