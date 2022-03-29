from datetime import datetime  # noqa:  TC002

from pydantic import BaseModel, HttpUrl  # noqa:  TC002


class ClientBase(BaseModel):
    ip: str
    lat: float | None
    lon: float | None
    isp: str | None
    isprating: str | None
    rating: str | None
    ispdlavg: str | None
    ispulavg: str | None
    loggedin: str | None
    country: str | None  # 'BE'


class Client(ClientBase):
    id: int
    results: list = []

    class Config:
        orm_mode = True


class ClientCreate(ClientBase):
    pass


class ServerBase(BaseModel):
    url: HttpUrl
    lat: float
    lon: float
    name: str
    country: str
    cc: str  # 'BE'
    sponsor: str
    uid: str
    host: str  # 'speedtest.edpnet.net:8080'
    d: float  # 19.316292953314182
    latency: float


class Server(ServerBase):
    id: int
    results: list = []

    class Config:
        orm_mode = True


class ServerCreate(ServerBase):
    pass


class ResultBase(BaseModel):
    download: float
    upload: float
    ping: float
    timestamp: datetime  # 2022-03-16T12:25:24.433971Z
    bytes_sent: int
    bytes_received: int
    share: None


class Result(ResultBase):
    id: int
    client_id: int
    server_id: int

    class Config:
        orm_mode = True


class ResultCreate(ResultBase):
    pass
