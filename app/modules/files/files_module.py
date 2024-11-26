"""
This module contains the functions to manage the files.
"""

from fastapi import HTTPException, status, UploadFile, Response
import os
import json

from app.utils.utils import check_if_filename_is_allowed


async def get_files(offset: int, limit: int):
    """
    This function returns a list of files.

    :param offset: Offset of the files.
    :param limit: Limit of the files.
    :return: List of files.
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files_directory = os.path.abspath(os.path.join(current_directory, "../../tmp/files"))

    files = []
    try:
        for file_name in os.listdir(files_directory):
            file_path = os.path.join(files_directory, file_name)
            if os.path.isfile(file_path):
                files.append(
                    {
                        'name': file_name,
                        'size': os.path.getsize(file_path),
                    }
                )
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Files directory not found")

    start = offset
    end = offset + limit
    return files[start:end]


async def create_or_update_file(file: UploadFile) -> Response:
    """
    This function creates a file if it does not exist or updates a file \
        if it exists.

    :param file: File to be created or updated.
    :return: File created or updated.
    """
    file_already_exists = False

    current_directory = os.path.dirname(os.path.abspath(__file__))
    files_directory = os.path.abspath(
        os.path.join(current_directory, "../../tmp/files")
    )

    try:
        if not check_if_filename_is_allowed(file.filename):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Filename contains invalid characters"
            )

        if not os.path.exists(files_directory):
            os.makedirs(files_directory)

        if os.path.exists(
            os.path.join(files_directory, file.filename)
        ):
            os.remove(os.path.join(files_directory, file.filename))
            file_already_exists = True

        file_path = os.path.join(files_directory, file.filename)
        with open(file_path, "wb") as file_object:
            file_object.write(file.file.read())
            os.chmod(file_path, 0o775)

        return Response(
            content=json.dumps({
                'file': file.filename,
                'status': 'file updated' if (
                    file_already_exists
                ) else 'file created',
            }),
            media_type="application/json",
            status_code=status.HTTP_201_CREATED if (
                not file_already_exists
            ) else status.HTTP_204_NO_CONTENT,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
