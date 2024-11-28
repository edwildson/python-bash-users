import pytest
from fastapi import UploadFile
from io import BytesIO
from unittest.mock import Mock

from app.routers import router_files
import app.schemas.files_schemas as schemas


@pytest.mark.asyncio
async def test_get_files(mocked_files_directory):
    files = await router_files.read_files(1)

    assert isinstance(files, schemas.GetFilesResponse)
    assert isinstance(files.files, list)
    assert isinstance(files.files[0], schemas.FileSchema)
    assert files.status == 'success'
    assert files.status_code == 200


@pytest.mark.asyncio
async def test_create_or_update_file_when_not_exists(mocked_files_directory):
    mock_file = Mock(spec=UploadFile)
    mock_file.filename = "testfile"

    mock_file.file = BytesIO(schemas.MOCK_FILE_CONTENT.encode())

    file = await router_files.create_or_update_file(
        mock_file
    )

    assert isinstance(file, schemas.PutFileResponse)
    assert file.message == 'File created'
    assert file.status == 'success'
    assert file.status_code == 201


@pytest.mark.asyncio
async def test_create_or_update_file_when_exists(mocked_files_directory):
    mock_file = Mock(spec=UploadFile)
    mock_file.filename = "testfile_1"
    mock_file.file = BytesIO(schemas.MOCK_FILE_CONTENT.encode())

    file = await router_files.create_or_update_file(
        mock_file
    )

    assert isinstance(file, schemas.PutFileResponse)
    assert file.message == 'File updated'
    assert file.status == 'success'
    assert file.status_code == 204


@pytest.mark.asyncio
async def test_create_or_update_file_when_filename_is_not_allowed():
    mock_file = Mock(spec=UploadFile)
    mock_file.filename = "test.file"
    mock_file.file = BytesIO(schemas.MOCK_FILE_CONTENT.encode())

    with pytest.raises(Exception) as e:
        await router_files.create_or_update_file(
            mock_file
        )
    assert str(e.value.detail) == '400: Filename contains invalid characters'
    assert e.value.status_code == 400

