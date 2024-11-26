from fastapi import APIRouter, Query

from app.settings.settings import settings

from app.services.users_service import (
    get_users_by_name,
    get_user_by_size,
    get_users_by_messages,
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


PER_PAGE = settings.PER_PAGE


@router.get(
    "",
    description="Retorna uma lista de usuários baseado em um arquivo.",
    summary="Lista de usuários",
)
async def read_users(
    filename: str = Query(description="Nome do arquivo"),
    username: str = Query('', description="Nome do usuário"),
    order: str = Query("asc", description="Ordenação dos usuários"),
    page: int = Query(1, description="Número da página", gt=0),
):
    """
    This is a simple function that returns a list of users based on a file.
    """
    offset = PER_PAGE * page - PER_PAGE

    return await get_users_by_name(
        filename=filename,
        username=username,
        order=order,
        offset=offset,
        limit=PER_PAGE
    )


@router.get(
    "/by_size",
    description="Retorna o usuário com maior ou menor size baseado \
        em um arquivo.",
    summary="Usuário com maior ou menor size",
)
async def read_user_by_size(
    filename: str = Query(description="Nome do arquivo"),
    order: str = Query("max", description="Ordenação do size"),
):
    """
    This is a simple function that returns the user with the largest or \
        smallest size based on a file.
    """
    user = await get_user_by_size(filename=filename, order=order)

    return user


@router.get(
    "/by_messages",
    description="Retorna uma lista de usuários que estejam em uma \
        faixa de quantidade de mensagens na posta INBOX.",
    summary="Lista de usuários por quantidade de mensagens",
)
async def read_users_by_messages(
    filename: str = Query(description="Nome do arquivo"),
    username: str = Query('', description="Nome do usuário"),
    min_messages: int = Query(description="Quantidade mínima de mensagens"),
    max_messages: int = Query(description="Quantidade máxima de mensagens"),
    page: int = Query(1, description="Número da página", gt=0),
):
    """
    This is a simple function that returns a list of users that are in a \
        range of quantity of messages in the INBOX post.
    """
    offset = PER_PAGE * page - PER_PAGE

    users = await get_users_by_messages(
        filename=filename,
        username=username,
        min_messages=min_messages,
        max_messages=max_messages,
        offset=offset,
        limit=PER_PAGE,
    )

    return users
