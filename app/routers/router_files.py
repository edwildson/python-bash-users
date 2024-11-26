from fastapi import APIRouter, Query, File, UploadFile, Response

from app.services import files_service


router = APIRouter(
    prefix="/files",
    tags=["files"],
)


PER_PAGE = 10


@router.get(
    "",
    description="Retorna uma lista de arquivos.",
    summary="Lista de arquivos",
)
async def read_files(
    page: int = Query(1, description="Número da página", gt=0),
):
    """
    This is a simple function that returns a list of files.
    """
    offset = PER_PAGE * page - PER_PAGE
    return await files_service.get_files(offset, PER_PAGE)


@router.put(
    "",
    description="Cria um arquivo caso ele não exista ou atualiza um \
        arquivo caso ele exista.",
    summary="Cria ou atualiza um arquivo",
)
async def create_or_update_file(
    file: UploadFile = File(),
) -> Response:
    """
    This is a simple function that creates a file if it does not exist \
        or updates a file if it exists.
    """
    return await files_service.create_or_update_file(file)
