from sqlalchemy.orm import Session
from app import models, schemas

# CRUD для Satellite
def get_satellites(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Satellite).offset(skip).limit(limit).all()

def create_satellite(db: Session, satellite: schemas.SatelliteCreate):
    db_satellite = models.Satellite(**satellite.dict())
    db.add(db_satellite)
    db.commit()
    db.refresh(db_satellite)
    return db_satellite

# CRUD для TVChannel
def get_tv_channels(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TVChannel).offset(skip).limit(limit).all()

def create_tv_channel(db: Session, tv_channel: schemas.TVChannelCreate):
    db_tv_channel = models.TVChannel(**tv_channel.dict())
    db.add(db_tv_channel)
    db.commit()
    db.refresh(db_tv_channel)
    return db_tv_channel

# CRUD для Broadcast
def get_broadcasts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Broadcast).offset(skip).limit(limit).all()

def create_broadcast(db: Session, broadcast: schemas.BroadcastCreate):
    db_broadcast = models.Broadcast(**broadcast.dict())
    db.add(db_broadcast)
    db.commit()
    db.refresh(db_broadcast)
    return db_broadcast
