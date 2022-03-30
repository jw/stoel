from sqlalchemy.orm import Session  # noqa:  TC002

from stoel import model, schemas  # noqa:  TC002


def get_result(db: Session, result_id: int) -> model.Result:
    return db.query(model.Result).filter(model.Result.id == result_id).first()


def get_results(db: Session, skip: int = 0, limit: int = 100) -> list[model.Result]:
    return db.query(model.Result).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.ClientCreate) -> model.Client:
    db_client = model.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def create_server(db: Session, server: schemas.ServerCreate) -> model.Server:
    db_server = model.Server(**server.dict())
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server


def create_result(
    db: Session,
    result: schemas.ResultCreate,
    client: model.Client,
    server: model.Server,
) -> model.Result:
    db_result = model.Result(**result.dict(), client_id=client.id, server_id=server.id)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result
