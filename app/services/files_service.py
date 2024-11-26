"""
This module contains the service layer for the files module.
"""



from fastapi import HTTPException, status, UploadFile, Response
from app.modules.files import files_module


async def get_files(offset: int, limit: int):
    """
    This function returns a list of files.

    :param offset: Offset of the files.
    :param limit: Limit of the files.
    :return: List of files.
    """
    return await files_module.get_files(offset, limit)


async def create_or_update_file(file: UploadFile) -> Response:
    """
    This function creates a file if it does not exist or updates a file \
        if it exists.

    :param file: File to be created or updated.
    :return: File created or updated.
    """
    return await files_module.create_or_update_file(file)
