from pydantic import BaseModel
from typing import Optional

class EmailResponse(BaseModel):
    subject: Optional[str] = "No Subject Generated"
    email: Optional[str] = "No Email Generated"
    tone: Optional[str] = "Professional"