import logging
from datetime import datetime, timezone
from importlib.metadata import version

from speedtest import Speedtest

logging.basicConfig(format="{asctime} {levelname:>8s} | {message}", style="{", level=logging.DEBUG)


def netspeed(s: Speedtest, servers: list = None, threads=None) -> dict:
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


def main():
    logging.info(f"Starting teleslet backend {version('teleslet')} at {datetime.now(timezone.utc)}.")
    logging.info(f"First result: {netspeed(Speedtest())}.")


if __name__ == '__main__':
    main()
