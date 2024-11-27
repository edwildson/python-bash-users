"""
This module contains the service layer for the users module.
"""

from fastapi import HTTPException, status, Response
from app.modules.users import users_module
from app.schemas.users_schemas import GetUsersResponse, UserSchema


async def get_users_by_name(
    filename: str, username: str, order: str, offset: int, limit: int
) -> GetUsersResponse:
    """
    This function returns a list of users based on a file.

    :param filename: Name of the file.
    :param username: Name of the user.
    :param order: Order of the users.
    :param offset: Offset of the users.
    :param limit: Limit of the users.
    :return: List of users.
    """
    return await users_module.get_users_by_name(
        filename, username, order, offset, limit
    )


async def get_user_by_size(filename: str, order: str) -> UserSchema:
    """
    This function returns the user with the largest or smallest size \
        based on a file.

    :param filename: Name of the file.
    :param order: Order of the size.
    :return: User with the largest or smallest size.
    """
    return await users_module.get_user_by_size(filename, order)


async def get_users_by_messages(
    filename: str,
    username: str,
    min_messages: int,
    max_messages: int,
    offset: int,
    limit: int
) -> GetUsersResponse:
    """
    This function returns a list of users that are in a range of quantity \
        of messages in the INBOX post.

    :param filename: Name of the file.
    :param min_messages: Minimum quantity of messages.
    :param max_messages: Maximum quantity of messages.
    :param offset: Offset of the users.
    :param limit: Limit of the users.
    :return: List of users.
    """
    return await users_module.get_users_by_messages(
        filename, username, min_messages, max_messages, offset, limit
    )
