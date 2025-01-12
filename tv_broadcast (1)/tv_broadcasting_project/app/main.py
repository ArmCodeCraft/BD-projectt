from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the TV Broadcasting API"}

# Satellite endpoints
@app.get("/satellites/", response_model=list[schemas.Satellite])
def read_satellites(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_satellites(db, skip=skip, limit=limit)

@app.post("/satellites/", response_model=schemas.Satellite)
def create_satellite(satellite: schemas.SatelliteCreate, db: Session = Depends(get_db)):
    return crud.create_satellite(db, satellite=satellite)

# TVChannel endpoints
@app.get("/tv_channels/", response_model=list[schemas.TVChannel])
def read_tv_channels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tv_channels(db, skip=skip, limit=limit)

@app.post("/tv_channels/", response_model=schemas.TVChannel)
def create_tv_channel(tv_channel: schemas.TVChannelCreate, db: Session = Depends(get_db)):
    return crud.create_tv_channel(db, tv_channel=tv_channel)

# Broadcast endpoints
@app.get("/broadcasts/", response_model=list[schemas.Broadcast])
def read_broadcasts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_broadcasts(db, skip=skip, limit=limit)

@app.post("/broadcasts/", response_model=schemas.Broadcast)
def create_broadcast(broadcast: schemas.BroadcastCreate, db: Session = Depends(get_db)):
    return crud.create_broadcast(db, broadcast=broadcast)
