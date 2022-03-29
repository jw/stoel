from typing import Any

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base: Any = declarative_base()


class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True, index=True)
    download = Column(Float)
    upload = Column(Float)
    ping = Column(Float)
    server_id = Column(Integer, ForeignKey("server.id"))
    timestamp = Column(DateTime)  # 2022-03-16T12:25:24.433971Z
    bytes_sent = Column(Integer)
    bytes_received = Column(Integer)
    share = Column(String)  # TODO(jw): kick this out?
    client_id = Column(Integer, ForeignKey("client.id"))


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)  # IPvAnyAddress
    lat = Column(Float)
    lon = Column(Float)
    isp = Column(String)
    isprating = Column(String)
    rating = Column(String)
    ispdlavg = Column(String)
    ispulavg = Column(String)
    loggedin = Column(String)
    country = Column(String)  # 'BE'
    results = relationship("Result")


class Server(Base):
    __tablename__ = "server"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)  # HttpUrl
    lat = Column(Float)
    lon = Column(Float)
    name = Column(String)
    country = Column(String)
    cc = Column(String)  # 'BE'
    sponsor = Column(String)
    uid = Column(String)
    host = Column(String)  # 'speedtest.edpnet.net:8080'
    d = Column(Float)  # 19.316292953314182
    latency = Column(Float)
    results = relationship("Result")
