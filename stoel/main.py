import logging
from datetime import datetime, timezone
from importlib.metadata import version

from fastapi import Depends, FastAPI
from speedtest import Speedtest
from sqlalchemy.orm import Session  # noqa: TC002

from stoel import crud, schemas
from stoel.crud import create_client, create_result, create_server
from stoel.database import SessionLocal, engine
from stoel.model import Base
from stoel.schemas import ClientCreate, ResultCreate, ServerCreate

logging.basicConfig(
    format="{asctime} {levelname:>8s} | {message}", style="{", level=logging.DEBUG
)


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/results/", response_model=list[schemas.Result])
def read_results(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)  # noqa: B008
):  # noqa: ANN201
    results = crud.get_results(db, skip=skip, limit=limit)
    return results


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
    r = s.results.dict()
    return r


def main() -> None:
    logging.info(
        f"Starting stoel backend {version('stoel')} at {datetime.now(timezone.utc)}."
    )
    r = netspeed(Speedtest())
    logging.info(f"Result: {r}.")
    save(r)


def save(r: dict) -> None:
    client = ClientCreate(**r["client"])
    logging.info(f"Client: {client}.")
    db_client = create_client(SessionLocal(), client)
    logging.info(f"Database Client: {db_client}.")

    # cleanup of the id on the server section
    r["server"]["uid"] = r["server"].pop("id")
    server = ServerCreate(**r["server"])
    logging.info(f"Server: {server}.")
    db_server = create_server(SessionLocal(), server)
    logging.info(f"Database Server: {db_server}.")

    result = ResultCreate(**r)
    db_result = create_result(SessionLocal(), result, db_client, db_server)
    logging.info(f"Database Result: {db_result}.")


if __name__ == "__main__":
    main()
