import pytest
import app.services.users_service as services
import app.schemas.users_schemas as schemas


@pytest.mark.asyncio
async def test_get_users_by_name(create_test_file):
    users = await services.get_users_by_name(
        'test_file', '', 'asc', 0, 10
    )

    assert isinstance(users, schemas.GetUsersResponse)
    assert isinstance(users.users, list)
    assert isinstance(users.users[0], schemas.UserSchema)
    assert users.status == 'success'
    assert users.status_code == 200


@pytest.mark.asyncio
async def test_get_users_by_size(create_test_file):
    user = await services.get_user_by_size('test_file', 'asc')

    assert isinstance(user, schemas.UserSchema)


@pytest.mark.asyncio
async def test_get_users_by_size_min(create_test_file):
    user = await services.get_user_by_size('test_file', 'min')

    assert isinstance(user, schemas.UserSchema)


@pytest.mark.asyncio
async def test_get_users_by_size_error():
    with pytest.raises(Exception) as e:
        await services.get_user_by_size('test_file', 'min')

    assert str(e.value) == "500: Error executing script: Command '['/http/app/scripts/max-min-size.sh', '/http/app/tmp/files/test_file', '-min']' returned non-zero exit status 1."  # noqa


@pytest.mark.asyncio
async def test_get_users_by_messages(create_test_file):
    users = await services.get_users_by_messages('test_file', '', 10, 20, 0, 10)

    assert isinstance(users, schemas.GetUsersResponse)
    assert isinstance(users.users, list)
    assert isinstance(users.users[0], schemas.UserSchema)
    assert users.status == 'success'


@pytest.mark.asyncio
async def test_get_users_by_messages_with_username(create_test_file):
    users = await services.get_users_by_messages('test_file', 'damejoxo', 10, 20, 0, 10)

    assert isinstance(users, schemas.GetUsersResponse)
    assert isinstance(users.users, list)
    assert isinstance(users.users[0], schemas.UserSchema)
    assert len(users.users) == 1
    assert users.status == 'success'
