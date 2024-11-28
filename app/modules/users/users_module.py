"""
This module contains the functions to manage the users.
"""
from fastapi import HTTPException, status, Response
import subprocess
import json

from app.settings.settings import settings
from app.utils.utils import handle_users_array_to_dict
from app.schemas.users_schemas import GetUsersResponse, UserSchema


async def get_users_by_name(
    filename: str,
    username: str,
    order: str,
    offset: int,
    limit: int
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

    file_path = f"{settings.PATH_FILES}/{filename}"
    script_path = f"{settings.PATH_SCRIPTS}/order-by-username.sh"

    try:
        cmd = [script_path, file_path, f"-{order}" if order == "desc" else ""]

        
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,  # Captura a saída padrão
            stderr=subprocess.PIPE,  # Captura erros, se houver
            text=True,               # Interpreta a saída como texto (string)
            check=True               # Lança exceção em caso de erro
        )

        users_array = result.stdout.splitlines()
        users = handle_users_array_to_dict(
            users=users_array, username=username, offset=offset, limit=limit
        )

        return GetUsersResponse(
            users=users,
            status='success',
            status_code=status.HTTP_200_OK,
            total=len(users),
            page=int((offset + settings.PER_PAGE) / settings.PER_PAGE)
        )
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error executing script: {str(e)}"
        )


async def get_user_by_size(filename: str, order: str) -> UserSchema:
    """
    This function returns the user with the largest or smallest size \
        based on a file.

    :param filename: Name of the file.
    :param order: Order of the size.
    :return: User with the largest or smallest size.
    """
    file_path = f"{settings.PATH_FILES}/{filename}"
    script_path = f"{settings.PATH_SCRIPTS}/max-min-size.sh"

    try:
        cmd = [script_path, file_path, f"-{order}" if order == "min" else ""]

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,  # Captura a saída padrão
            stderr=subprocess.PIPE,  # Captura erros, se houver
            text=True,               # Interpreta a saída como texto (string)
            check=True               # Lança exceção em caso de erro
        )
        users_array = result.stdout.splitlines()

        users = handle_users_array_to_dict(
            users=users_array, offset=0, limit=1
        )

        if not users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado."
            )

        return UserSchema(
            **users[0]
        )
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error executing script: {str(e)}"
        )


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
    file_path = f"{settings.PATH_FILES}/{filename}"
    script_path = f"{settings.PATH_SCRIPTS}/between-msgs.sh"

    try:
        cmd = [script_path, file_path, str(min_messages), str(max_messages)]

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,  # Captura a saída padrão
            stderr=subprocess.PIPE,  # Captura erros, se houver
            text=True,               # Interpreta a saída como texto (string)
            check=True               # Lança exceção em caso de erro
        )
        users_array = result.stdout.splitlines()

        users = handle_users_array_to_dict(
            users=users_array, username=username, offset=offset, limit=limit
        )

        return GetUsersResponse(
            users=users,
            status='success',
            status_code=status.HTTP_200_OK,
            total=len(users),
            page=int((offset + settings.PER_PAGE) / settings.PER_PAGE),
        )
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error executing script: {str(e)}"
        )
