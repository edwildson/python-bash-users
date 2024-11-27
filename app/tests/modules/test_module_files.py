import pytest
from fastapi import UploadFile
from io import BytesIO
from unittest.mock import Mock, patch

from app.modules.files import files_module
import app.schemas.files_schemas as schemas
from app.settings.settings import settings
import os


@pytest.mark.asyncio
async def test_get_files(mocked_files_directory):
    files = await files_module.get_files(0, 10)

    assert isinstance(files, schemas.GetFilesResponse)
    assert isinstance(files.files, list)
    assert isinstance(files.files[0], schemas.FileSchema)
    assert files.status == 'success'
    assert len(files.files) == 10


@pytest.mark.asyncio
async def test_get_files_paginated(mocked_files_directory):
    files = await files_module.get_files(5, 10)

    assert isinstance(files, schemas.GetFilesResponse)
    assert isinstance(files.files, list)
    assert isinstance(files.files[0], schemas.FileSchema)
    assert files.status == 'success'
    assert len(files.files) == 5


@pytest.mark.asyncio
async def test_get_files_folder_not_found():
    mocked_path_files = settings.PATH_FILES + "/testfile"

    if os.path.exists(mocked_path_files):
        os.rmdir(mocked_path_files)

    with patch('app.settings.settings.settings.PATH_FILES', mocked_path_files):
        with pytest.raises(Exception) as e:
            _ = await files_module.get_files(0, 10)
            assert str(e) == "404: Files directory not found"
            assert e.value.status == 404


@pytest.mark.asyncio
async def test_create_or_update_file_when_not_exists(mocked_files_directory):
    mock_file = Mock(spec=UploadFile)
    mock_file.filename = "testfile_11"
    mock_file.file = BytesIO(schemas.MOCK_FILE_CONTENT.encode())

    file = await files_module.create_or_update_file(mock_file)

    assert isinstance(file, schemas.PutFileResponse)
    assert file.message == 'File created'
    assert file.status == 'success'
    assert file.status_code == 201


@pytest.mark.asyncio
async def test_create_or_update_file_when_exists(mocked_files_directory):
    mock_file = Mock(spec=UploadFile)
    mock_file.filename = "testfile_1"
    mock_file.file = BytesIO(schemas.MOCK_FILE_CONTENT.encode())

    file = await files_module.create_or_update_file(mock_file)

    assert isinstance(file, schemas.PutFileResponse)
    assert file.message == 'File updated'
    assert file.status == 'success'
    assert file.status_code == 204


@pytest.mark.asyncio
async def test_create_or_update_file_when_filename_is_not_allowed(mocked_files_directory):
    mock_file = Mock(spec=UploadFile)
    mock_file.filename = "testfile;1"
    mock_file.file = BytesIO(schemas.MOCK_FILE_CONTENT.encode())

    with pytest.raises(Exception) as e:
        file = await files_module.create_or_update_file(mock_file)
        assert str(e) == "400: Filename contains invalid characters"
        assert e.value.status == 400
