import logging
import os

import aiofiles
from fastapi import HTTPException, UploadFile

log = logging.getLogger("uvicorn")


async def save_file(file: UploadFile, filestore: str) -> str:
    """
    Saves the file to the filestore location.
    :param file: The temporary spooled file-like object.
    :param filestore: The location to where the file will be saved.
    :return: filename
    """
    try:
        async with aiofiles.open(os.path.join(filestore, file.filename), "wb") as f:

            # Read the data in chunks and save it, as we go.
            for i in iter(lambda: file.file.read(1024 * 1024 * 64), b""):

                # We can improve this by keeping track of the chunks saved,
                # report that number with an API endpoint and have the client
                # start the upload from the last saved chunk if the upload was
                # interrupted intentionally or due to a network failure.
                await f.write(i)
        log.info(f"File saved as {file.filename}")
    except Exception as e:

        # Not trying to cover all possible errors here, just bubble up the details.
        # Response format based on https://datatracker.ietf.org/doc/html/rfc7807
        problem_response = {"type": str(type(e).__name__), "details": str(e)}
        headers = {"Content-Type": "application/problem+json"}
        log.error(problem_response)
        raise HTTPException(status_code=500, detail=problem_response, headers=headers)
    return file.filename
