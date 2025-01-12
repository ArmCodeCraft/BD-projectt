from pydantic import BaseModel
from typing import Optional

# Satellite Schemas
class SatelliteBase(BaseModel):
    name: str
    country: str
    lifespan: float
    orbit_radius: float

class SatelliteCreate(SatelliteBase):
    pass

class Satellite(SatelliteBase):
    id: int

    class Config:
        orm_mode = True

# TVChannel Schemas
class TVChannelBase(BaseModel):
    name: str
    language: str
    country: str
    company: str
    specialty: str

class TVChannelCreate(TVChannelBase):
    pass

class TVChannel(TVChannelBase):
    id: int

    class Config:
        orm_mode = True

# Broadcast Schemas
class BroadcastBase(BaseModel):
    frequency: float
    belt_from: float
    belt_to: float
    satellite_id: int
    tv_channel_id: int

class BroadcastCreate(BroadcastBase):
    pass

class Broadcast(BroadcastBase):
    id: int

    class Config:
        orm_mode = True
