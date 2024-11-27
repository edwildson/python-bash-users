import pytest
import json
import subprocess
import os

from unittest.mock import patch
from fastapi import status, HTTPException

from app.modules.users import users_module
from app.settings import settings
from app.schemas.files_schemas import MOCK_FILE_CONTENT
from app.schemas.users_schemas import UserSchema, GetUsersResponse


@pytest.mark.asyncio
async def test_get_users_by_name_asc_success(create_test_file):
    filename = 'test_file'
    username = ""
    order = "asc"
    offset = 0
    limit = 10

    expected_result = [UserSchema(**result) for result in [
        {"username": "alice.wonderland@yahoo.com", "folder": "inbox", "numberMessages": 3210, "size": 987654},
        {"username": "blue.ocean@marine.life", "folder": "inbox", "numberMessages": 2222, "size": 987123},
        {"username": "bob.builder@hotmail.com", "folder": "inbox", "numberMessages": 1234, "size": 567890},
        {"username": "charlie.brown@outlook.com", "folder": "inbox", "numberMessages": 2345, "size": 1111222},
        {"username": "cool.guy@random.net", "folder": "inbox", "numberMessages": 678, "size": 345678},
        {"username": "damejoxo@uol.com.br", "folder": "inbox", "numberMessages": 13, "size": 2142222},
        {"username": "galaxy.star@space.org", "folder": "inbox", "numberMessages": 5678, "size": 1111999},
        {"username": "gamer@play.fun", "folder": "inbox", "numberMessages": 6666, "size": 1111333},
        {"username": "green.planet@eco.org", "folder": "inbox", "numberMessages": 1111, "size": 444555},
        {"username": "jane.doe@example.com", "folder": "inbox", "numberMessages": 123, "size": 124567},
    ]]

    # Executa a função
    response = await users_module.get_users_by_name(filename, username, order, offset, limit)

    # Verifica a resposta
    assert response.status_code == status.HTTP_200_OK

    assert response.users == expected_result
    assert response.total == len(expected_result)
    assert response.page == 1


@pytest.mark.asyncio
async def test_get_users_by_name_desc_success(create_test_file):
    # Configura os diretórios temporários para o teste
    filename = 'test_file'
    username = ""
    order = "desc"
    offset = 0
    limit = 10

    expected_result = [UserSchema(**result) for result in [
        {"username": "yyfdinny@uol.com.br", "folder": "inbox", "numberMessages": 5000, "size": 11134606},
        {"username": "vx.qka@uol.com.br", "folder": "inbox", "numberMessages": 1042150, "size": 11113043},
        {"username": "valley.low@earth.net", "folder": "inbox", "numberMessages": 4321, "size": 654321},
        {"username": "user123@domain.com", "folder": "inbox", "numberMessages": 999, "size": 555666},
        {"username": "tiny.human@bigworld.org", "folder": "inbox", "numberMessages": 3333, "size": 111222},
        {"username": "test.email+alex@foo.com", "folder": "inbox", "numberMessages": 111, "size": 123321},
        {"username": "sihdtelu@uol.com.br", "folder": "inbox", "numberMessages": 20, "size": 1033573},
        {"username": "robotic.future@ai.tech", "folder": "inbox", "numberMessages": 4444, "size": 1000001},
        {"username": "random.user2@test.com", "folder": "inbox", "numberMessages": 7890, "size": 1444555},
        {"username": "random.user1@test.com", "folder": "inbox", "numberMessages": 456, "size": 222333},
    ]]  # noqa

    # Executa a função
    response = await users_module.get_users_by_name(filename, username, order, offset, limit)

    # Verifica a resposta
    assert response.status_code == status.HTTP_200_OK

    assert response.users == expected_result
    assert response.total == len(expected_result)
    assert response.page == 1

# @pytest.mark.asyncio
# async def test_get_users_by_name_asc_success():
#     filename = "test_file.txt"
#     username = ""
#     order = "asc"
#     offset = 0
#     limit = 10

#     # Mock settings
#     mock_path_files = "/mock/path/files"
#     mock_path_scripts = "/mock/path/scripts"
#     mock_users_array = [
#         "damejoxo@uol.com.br inbox 000000013 size 002142222",
#         "li_digik@uol.com.br inbox 011000230 size 001032646",
#         "yyfdinny@uol.com.br inbox 000005000 size 011134606",
#         "sihdtelu@uol.com.br inbox 000000020 size 001033573",
#         "vx.qka@uol.com.br inbox 001042150 size 011113043",
#         "abc123@uol.com.br inbox 000000001 size 000000001",
#         "def456@uol.com.br inbox 000000002 size 000000002",
#         "ghi789@uol.com.br inbox 000000003 size 000000003",
#         "jkl012@uol.com.br inbox 000000004 size 000000004",
#         "mno345@uol.com.br inbox 000000005 size 000000005",
#         "pqr678@uol.com.br inbox 000000006 size 000000006",
#         "stu901@uol.com.br inbox 000000007 size 000000007",
#         "vwx234@uol.com.br inbox 000000008 size 000000008",
#         "yz1234@uol.com.br inbox 000000009 size 000000009",
#         "abcd567@uol.com.br inbox 000000010 size 000000010",
#         "efgh890@uol.com.br inbox 000000011 size 000000011",
#         "ijkl123@uol.com.br inbox 000000012 size 000000012",
#         "mnop456@uol.com.br inbox 000000013 size 000000013",
#         "qrst789@uol.com.br inbox 000000014 size 000000014",
#         "uvwx012@uol.com.br inbox 000000015 size 000000015",
#         "yzab345@uol.com.br inbox 000000016 size 000000016",
#         "cdef678@uol.com.br inbox 000000017 size 000000017",
#         "ghij901@uol.com.br inbox 000000018 size 000000018",
#         "klmn234@uol.com.br inbox 000000019 size 000000019",
#         "opqr567@uol.com.br inbox 000000020 size 000000020",
#         "stuv890@uol.com.br inbox 000000021 size 000000021",
#         "wxyz123@uol.com.br inbox 000000022 size 000000022",
#         "abcd456@uol.com.br inbox 000000023 size 000000023",
#         "efgh789@uol.com.br inbox 000000024 size 000000024",
#         "ijkl012@uol.com.br inbox 000000025 size 000000025",
#         "mnop345@uol.com.br inbox 000000026 size 000000026",
#         "qrst678@uol.com.br inbox 000000027 size 000000027",
#         "uvwx901@uol.com.br inbox 000000028 size 000000028",
#         "yzab234@uol.com.br inbox 000000029 size 000000029",
#         "cdef567@uol.com.br inbox 000000030 size 000000030",
#     ]

#     expected_result = [
#         {"username": "abc123@uol.com.br", "folder": "inbox", "numberMessages": 1, "size": 1},
#         {"username": "abcd456@uol.com.br", "folder": "inbox", "numberMessages": 23, "size": 23},
#         {"username": "abcd567@uol.com.br", "folder": "inbox", "numberMessages": 10, "size": 10},
#         {"username": "cdef567@uol.com.br", "folder": "inbox", "numberMessages": 30, "size": 30},
#         {"username": "cdef678@uol.com.br", "folder": "inbox", "numberMessages": 17, "size": 17},
#         {"username": "damejoxo@uol.com.br", "folder": "inbox", "numberMessages": 13, "size": 2142222},
#         {"username": "def456@uol.com.br", "folder": "inbox", "numberMessages": 2, "size": 2},
#         {"username": "efgh789@uol.com.br", "folder": "inbox", "numberMessages": 24, "size": 24},
#         {"username": "efgh890@uol.com.br", "folder": "inbox", "numberMessages": 11, "size": 11},
#         {"username": "ghi789@uol.com.br", "folder": "inbox", "numberMessages": 3, "size": 3}
#     ]

#     with patch("app.settings.settings.settings.PATH_FILES", mock_path_files), \
#         patch("app.settings.settings.settings.PATH_SCRIPTS", mock_path_scripts), \
#          patch("app.modules.users.users_module.handle_users_array_to_dict") as mock_handle_users, \
#          patch("subprocess.run") as mock_run:

#         # Simula saída do script
#         mock_run.return_value = MagicMock(stdout="\n".join(mock_users_array), returncode=0)
#         # Simula retorno do processador de array
#         mock_handle_users.return_value = expected_result

#         # Executa a função sob teste
#         response = await users_module.get_users_by_name(filename, username, order, offset, limit)

#         # Verificações
#         assert response.status_code == status.HTTP_200_OK

#         response_data = json.loads(response.body)
#         assert response_data["users"] == expected_result
#         assert response_data["total"] == len(expected_result)
#         assert response_data["page"] == 1  # offset=0 com PER_PAGE=10


@pytest.mark.asyncio
async def test_get_users_by_name_script_error():
    filename = "test_file.txt"
    username = "test_user"
    order = "asc"
    offset = 0
    limit = 10

    # Mock settings
    mock_path_files = "/mock/path/files"
    mock_path_scripts = "/mock/path/scripts"

    with patch("app.settings.settings.settings.PATH_FILES", mock_path_files), \
         patch("app.settings.settings.settings.PATH_SCRIPTS", mock_path_scripts), \
         patch("subprocess.run") as mock_run:

        # Simula erro no script
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd="mocked_cmd", stderr="Script error"
        )

        # Executa a função sob teste e verifica a exceção
        with pytest.raises(HTTPException) as exc_info:
            await users_module.get_users_by_name(filename, username, order, offset, limit)

        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert "Script error" in exc_info.value.detail


@pytest.mark.asyncio
async def test_get_user_by_size_max_success(create_test_file):
    filename = "test_file"

    order = "max"

    expected_result = UserSchema(**{"username": "rainbow.colors@pride.com", "folder": "inbox", "numberMessages": 3456, "size": 900888888})  # noqa

    # Executa a função
    response = await users_module.get_user_by_size(filename, order)

    assert response == expected_result


@pytest.mark.asyncio
async def test_get_user_by_size_min_success(create_test_file):
    filename = "test_file"

    order = "min"

    expected_result = UserSchema(**{"username": "tiny.human@bigworld.org", "folder": "inbox", "numberMessages": 3333, "size": 111222})  # noqa

    response = await users_module.get_user_by_size(filename, order)

    assert response == expected_result


@pytest.mark.asyncio
async def test_get_user_by_size_not_found(create_test_empty_file):
    filename = "test_file"

    order = "max"

    with pytest.raises(HTTPException) as exc_info:
        await users_module.get_user_by_size(filename, order)

        assert str(exc_info) == "404: Usuário não encontrado."
        assert exc_info.value.status_code == 404


@pytest.mark.asyncio
async def test_get_users_by_messages(create_test_file):
    filename = "test_file"

    username = ""
    offset = 0
    limit = 10
    min_messages = 111
    max_messages = 678

    expected_result = [UserSchema(**result) for result in [
        {"username": "jane.doe@example.com", "folder": "inbox", "numberMessages": 123, "size": 124567},
        {"username": "random.user1@test.com", "folder": "inbox", "numberMessages": 456, "size": 222333},
        {"username": "test.email+alex@foo.com", "folder": "inbox", "numberMessages": 111, "size": 123321},
        {"username": "cool.guy@random.net", "folder": "inbox", "numberMessages": 678, "size": 345678}
    ]]  # noqa

    # Executa a função
    users = await users_module.get_users_by_messages(
        filename, '', min_messages, max_messages, offset, limit
    )  # noqa

    assert users.status_code == 200
    assert isinstance(users.users, list)
    assert isinstance(users.users[0], UserSchema)
    assert users.users == expected_result
