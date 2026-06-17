from src.chains import chain
from src.chains import parser

def generate_email(email_topic: str):

    result = chain.invoke(
        {
            "email_topic": email_topic,
            "format_instructions": parser.get_format_instructions()
        }
    )

    return result