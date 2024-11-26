import pytest
import app.services.users_service as services
import app.schemas.users_schemas as schemas


@pytest.mark.asyncio
async def test_get_users_by_name():
    users = await services.get_users_by_name(
        'filename', 'username', 'asc', 0, 10
    )

    assert isinstance(users, schemas.GetUsersResponse)
    assert isinstance(users.users, list)
    assert isinstance(users.users[0], schemas.UserSchema)
    assert users.status == 'success'


@pytest.mark.asyncio
async def test_get_users_by_size():
    user = await services.get_user_by_size('filename', 'asc')

    assert isinstance(user, schemas.UserSchema)
    assert user.username == 'username'
    assert user.folder == 'INBOX'
    assert user.numberMessages == 10
    assert user.size == 1500


@pytest.mark.asyncio
async def test_get_users_by_size():
    user = await services.get_user_by_size('filename', 'desc')

    assert isinstance(user, schemas.UserSchema)
    assert user.username == 'username'
    assert user.folder == 'INBOX'
    assert user.numberMessages == 10
    assert user.size == 1500


@pytest.mark.asyncio
async def test_get_users_by_messages():
    users = await services.get_users_by_messages('filename', '', 10, 20, 0, 10)

    assert isinstance(users, schemas.GetUsersResponse)
    assert isinstance(users.users, list)
    assert isinstance(users.users[0], schemas.UserSchema)
    assert users.status == 'success'


@pytest.mark.asyncio
async def test_get_users_by_messages_with_username():
    users = await services.get_users_by_messages('filename', 'username', 10, 20, 0, 10)

    assert isinstance(users, schemas.GetUsersResponse)
    assert isinstance(users.users, list)
    assert isinstance(users.users[0], schemas.UserSchema)
    assert users.status == 'success'
