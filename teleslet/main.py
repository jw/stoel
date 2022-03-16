import logging
from datetime import datetime, timezone
from importlib.metadata import version

from pydantic import BaseModel, HttpUrl, IPvAnyAddress  # noqa: TC002
from speedtest import Speedtest

logging.basicConfig(
    format="{asctime} {levelname:>8s} | {message}", style="{", level=logging.DEBUG
)


class Client(BaseModel):
    ip: IPvAnyAddress
    lat: float
    lon: float
    isp: str
    isprating: str
    rating: int
    ispdlavg: int
    ispulavg: int
    loggedin: int
    country: str  # 'BE'


class Server(BaseModel):
    url: HttpUrl
    lat: float
    lon: float
    name: str
    country: str
    cc: str  # 'BE'
    sponsor: str
    id: str
    host: str  # 'speedtest.edpnet.net:8080'
    d: float  # 19.316292953314182
    latency: float


class Result(BaseModel):
    download: float
    upload: float
    ping: float
    server: Server
    timestamp: datetime  # 2022-03-16T12:25:24.433971Z
    bytes_sent: int
    bytes_received: int
    share: None
    client: Client


def netspeed(s: Speedtest, servers: list = None, threads: int = None) -> dict:
    if not servers:
        servers = []
    servers = s.get_servers(servers)
    logging.debug(f"Using these servers: {servers}.")
    server = s.get_best_server()
    logging.debug(f"Best server is: {server}.")
    logging.debug("Getting download speed...")
    download = s.download(threads=threads)
    logging.debug(f"Download speed is {download}.")
    logging.debug("Getting upload speed...")
    upload = s.upload(threads=threads)
    logging.debug(f"Upload speed is {upload}.")
    logging.debug(f"Ping is {s.results.ping}.")
    return s.results.dict()


def main() -> None:
    logging.info(
        f"Starting teleslet backend {version('teleslet')} at {datetime.now(timezone.utc)}."
    )
    r = netspeed(Speedtest())
    r["client"] = Client(**r["client"])
    r["server"] = Server(**r["server"])
    result = Result(**r)
    logging.info(f"Result: {result}.")


if __name__ == "__main__":
    main()
