from src.chains import chain
from src.chains import parser
from src.chains import langfuse_callback

def generate_email(email_topic: str):

    result = chain.invoke(

        {
            "email_topic": email_topic,

            "format_instructions":
            parser.get_format_instructions()
        },

        config={

            "callbacks": [langfuse_callback],

            "tags": ["ai-email-writer"],

            "metadata": {

                "project":
                "AI Email Writing Assistant"
            }
        }
    )

    return result