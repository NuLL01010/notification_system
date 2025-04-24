from pydantic import BaseModel


class SEmailNotify(BaseModel):
    to: str
    subject: str
    body: str
    error_message: str



class SSmsNotify(BaseModel):
    to: str
    text: str