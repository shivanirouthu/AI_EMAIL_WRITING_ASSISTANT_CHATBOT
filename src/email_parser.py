from pydantic import BaseModel


class EmailResponse(BaseModel):

    subject: str
    email_body: str
    tone: str