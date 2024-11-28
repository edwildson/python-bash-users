import pytest
from fastapi import UploadFile
from io import BytesIO
from unittest.mock import Mock


import app.schemas.files_schemas as schemas
import app.services.files_service as services


@pytest.mark.asyncio
async def test_get_files(mocked_files_directory):
    files = await services.get_files(0, 10)

    assert isinstance(files, schemas.GetFilesResponse)
    assert isinstance(files.files, list)
    assert isinstance(files.files[0], schemas.FileSchema)
    assert files.status == 'success'


@pytest.mark.asyncio
async def test_create_or_update_file_when_not_exists(mocked_files_directory):
    mock_file = Mock(spec=UploadFile)
    mock_file.filename = "testfile"
    mock_file.file = BytesIO(schemas.MOCK_FILE_CONTENT.encode())

    file = await services.create_or_update_file(mock_file)

    assert isinstance(file, schemas.PutFileResponse)
    assert file.message == 'File created'
    assert file.status == 'success'
    assert file.status_code == 201


@pytest.mark.asyncio
async def test_create_or_update_file_when_exists(mocked_files_directory):
    mock_file = Mock(spec=UploadFile)
    mock_file.filename = "testfile_1"
    mock_file.file = BytesIO(schemas.MOCK_FILE_CONTENT.encode())

    file = await services.create_or_update_file(mock_file)

    assert isinstance(file, schemas.PutFileResponse)
    assert file.message == 'File updated'
    assert file.status == 'success'
    assert file.status_code == 204


@pytest.mark.asyncio
async def test_create_or_update_file_when_filename_is_not_allowed(mocked_files_directory):
    mock_file = Mock(spec=UploadFile)
    mock_file.filename = "test.file"
    mock_file.file = BytesIO(schemas.MOCK_FILE_CONTENT.encode())

    with pytest.raises(Exception) as e:
        await services.create_or_update_file(mock_file)

    assert str(e.value.detail) == "400: Filename contains invalid characters"
    assert e.value.status_code == 400
