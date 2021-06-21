from pydantic import BaseModel


class UploadPayloadSchema(BaseModel):
    filename: str
