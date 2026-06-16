from pydantic import BaseModel


class EmailResponse(BaseModel):
    subject: str
    email: str
    tone: str