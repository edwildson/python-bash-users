import pytest

from app.routers import router_users

from app.schemas import users_schemas as schemas


@pytest.mark.asyncio
async def test_get_read_users(create_test_file):
    users = await router_users.read_users(
        filename='test_file',
        username='',
        order='asc',
        page=1
    )

    assert isinstance(users, schemas.GetUsersResponse)
    assert isinstance(users.users, list)
    assert isinstance(users.users[0], schemas.UserSchema)
    assert users.status == 'success'
    assert users.status_code == 200


@pytest.mark.asyncio
async def test_read_user_by_size(create_test_file):
    user = await router_users.read_user_by_size(
        filename='test_file',
        order='asc'
    )

    assert isinstance(user, schemas.UserSchema)
    assert user.username == 'rainbow.colors@pride.com'
    assert user.folder == 'inbox'
    assert user.numberMessages == 3456
    assert user.size == 900888888


@pytest.mark.asyncio
async def test_read_user_by_size_desc(create_test_file):
    user = await router_users.get_user_by_size(
        filename='test_file',
        order='min'
    )

    assert isinstance(user, schemas.UserSchema)
    assert user.username == 'tiny.human@bigworld.org'
    assert user.folder == 'inbox'
    assert user.numberMessages == 3333
    assert user.size == 111222


@pytest.mark.asyncio
async def test_get_read_users_by_messages(create_test_file):
    users = await router_users.read_users_by_messages(
        filename='test_file', 
        username='',
        min_messages=10,
        max_messages=20,
        page=1,
    )

    assert isinstance(users, schemas.GetUsersResponse)
    assert isinstance(users.users, list)
    assert isinstance(users.users[0], schemas.UserSchema)
    assert users.status == 'success'
    assert users.status_code == 200
