import pytest

from app.routers import router_users


@pytest.mark.asyncio
async def test_get_users_by_name():
    users = await router_users.get_users_by_name(
        'filename', 'username', 'asc', 0, 10
    )

    assert isinstance(users, dict)
    assert isinstance(users['users'], list)
    assert isinstance(users['users'][0], dict)
    assert users['status'] == 'success'
    assert users['status_code'] == 200


@pytest.mark.asyncio
async def test_get_user_by_size():
    user = await router_users.get_user_by_size('filename', 'asc')

    assert isinstance(user, dict)
    assert user['username'] == 'username'
    assert user['folder'] == 'INBOX'
    assert user['numberMessages'] == 10
    assert user['size'] == 1500


@pytest.mark.asyncio
async def test_get_user_by_size_desc():
    user = await router_users.get_user_by_size('filename', 'desc')

    assert isinstance(user, dict)
    assert user['username'] == 'username'
    assert user['folder'] == 'INBOX'
    assert user['numberMessages'] == 10
    assert user['size'] == 1500


@pytest.mark.asyncio
async def test_get_users_by_messages():
    users = await router_users.get_users_by_messages('filename', '', 10, 20, 0, 10)

    assert isinstance(users, dict)
    assert isinstance(users['users'], list)
    assert isinstance(users['users'][0], dict)
    assert users['status'] == 'success'
    assert users['status_code'] == 200