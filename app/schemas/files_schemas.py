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


MOCK_FILE_CONTENT = """\
damejoxo@uol.com.br inbox 000000013 size 002142222
li_digik@uol.com.br inbox 011000230 size 001032646
yyfdinny@uol.com.br inbox 000005000 size 011134606
sihdtelu@uol.com.br inbox 000000020 size 001033573
vx.qka@uol.com.br inbox 001042150 size 011113043
jane.doe@example.com inbox 000000123 size 000124567
john.smith@gmail.com inbox 000004567 size 001223344
alice.wonderland@yahoo.com inbox 000003210 size 000987654
bob.builder@hotmail.com inbox 000001234 size 000567890
charlie.brown@outlook.com inbox 000002345 size 001111222
random.user1@test.com inbox 000000456 size 000222333
random.user2@test.com inbox 000007890 size 001444555
user123@domain.com inbox 000000999 size 000555666
test.email+alex@foo.com inbox 000000111 size 000123321
cool.guy@random.net inbox 000000678 size 000345678
galaxy.star@space.org inbox 000005678 size 001111999
rainbow.colors@pride.com inbox 000003456 size 900888888
mountain.high@travel.co inbox 000000789 size 000123456
valley.low@earth.net inbox 000004321 size 000654321
green.planet@eco.org inbox 000001111 size 000444555
blue.ocean@marine.life inbox 000002222 size 000987123
tiny.human@bigworld.org inbox 000003333 size 000111222
robotic.future@ai.tech inbox 000004444 size 001000001
programmer@code.dev inbox 000005555 size 001234567
gamer@play.fun inbox 000006666 size 001111333
music.lover@notes.com inbox 000007777 size 001000222
movie.fan@cinema.com inbox 000008888 size 001222111
"""
