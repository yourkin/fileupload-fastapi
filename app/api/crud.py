from typing import Optional, List

from app.models.pydantic import UploadPayloadSchema
from app.models.upload import Upload, UploadSchema


async def get(id: int) -> Optional[dict]:
    upload = await Upload.filter(id=id).first().values()
    if upload:
        return upload[0]
    return None


async def get_all() -> List:
    files = await Upload.all().values()
    return files


async def post_upload(payload: UploadPayloadSchema) -> UploadSchema:
    upload = Upload(
        filename=payload.filename,
    )
    await upload.save()
    return upload
