import logging
from typing import List

from fastapi import APIRouter, File, UploadFile, Depends

from app.api import crud
from app.config import get_settings, Settings
from app.core.file_utils import save_file
from app.models.pydantic import UploadPayloadSchema
from app.models.upload import UploadSchema

log = logging.getLogger("uvicorn")
router = APIRouter()


@router.post("/file", response_model=UploadSchema, status_code=201)
async def upload_file(
    file: UploadFile = File(...), settings: Settings = Depends(get_settings)
) -> UploadSchema:

    filename = await save_file(file, settings.filestore_dir)

    payload = UploadPayloadSchema(
        filename=filename,
    )
    upload = await crud.post_upload(payload)
    return upload


@router.post("/files", response_model=List[UploadSchema], status_code=201)
async def upload_files(
    file_list: List[UploadFile] = File(...), settings: Settings = Depends(get_settings)
) -> List[UploadSchema]:
    uploads = []
    log.info(file_list)
    for file in file_list:
        filename = await save_file(file, settings.filestore_dir)
        payload = UploadPayloadSchema(
            filename=filename,
        )
        upload = await crud.post_upload(payload)
        uploads.append(upload)
    return uploads
