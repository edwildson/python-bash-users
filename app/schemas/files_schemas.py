from typing import List
from pydantic import BaseModel


class FileSchema(BaseModel):
    filename: str
    size: int


class GetFilesResponse(BaseModel):
    files: List[FileSchema]
    status: str
    status_code: int


class PutFileResponse(BaseModel):
    message: str
    status: str
    status_code: int


MOCK_FILE_CONTENT = b"""\
damejoxo@uol.com.br inbox 000000013 size 002142222
li_digik@uol.com.br inbox 011000230 size 001032646
yyfdinny@uol.com.br inbox 000005000 size 011134606
sihdtelu@uol.com.br inbox 000000020 size 001033573
vx.qka@uol.com.br inbox 001042150 size 011113043
"""
