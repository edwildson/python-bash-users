
import os
import pytest
from unittest.mock import patch
from app.settings.settings import settings

from app.schemas.files_schemas import MOCK_FILE_CONTENT


@pytest.fixture
def mocked_files_directory():
    mocked_path_files = settings.PATH_FILES + "/testfile"

    if not os.path.exists(mocked_path_files):
        os.makedirs(mocked_path_files)

    for i in range(10):
        with open(os.path.join(mocked_path_files, f"testfile_{i}"), 'w') as f:
            f.write(f"Content of test file {i}")

    with patch('app.settings.settings.settings.PATH_FILES', mocked_path_files):
        yield mocked_path_files

    if os.path.exists(mocked_path_files):
        for file in os.listdir(mocked_path_files):
            os.remove(os.path.join(mocked_path_files, file))
    os.rmdir(mocked_path_files)


@pytest.fixture
def create_test_file():
    files_dir = settings.PATH_FILES

    filename = "test_file"
    file_path = f"{files_dir}/{filename}"
    file_content = MOCK_FILE_CONTENT
    with open(file_path, "w") as f:
        f.write(file_content)

    yield

    os.remove(file_path)


@pytest.fixture
def create_test_empty_file():
    files_dir = settings.PATH_FILES

    filename = "test_file"
    file_path = f"{files_dir}/{filename}"
    file_content = ''
    with open(file_path, "w") as f:
        f.write(file_content)

    yield

    os.remove(file_path)
