from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Satellite(Base):
    __tablename__ = "satellites"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    lifespan = Column(Float, nullable=False)  # Срок эксплуатации
    orbit_radius = Column(Float, nullable=False)

    broadcasts = relationship("Broadcast", back_populates="satellite")


class TVChannel(Base):
    __tablename__ = "tv_channels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    language = Column(String, nullable=False)
    country = Column(String, nullable=False)
    company = Column(String, nullable=False)
    specialty = Column(String, nullable=False)

    broadcasts = relationship("Broadcast", back_populates="tv_channel")


class Broadcast(Base):
    __tablename__ = "broadcasts"
    id = Column(Integer, primary_key=True, index=True)
    frequency = Column(Float, nullable=False)
    belt_from = Column(Float, nullable=False)  # Охват поясов от
    belt_to = Column(Float, nullable=False)    # Охват поясов до

    satellite_id = Column(Integer, ForeignKey("satellites.id"), nullable=False)
    tv_channel_id = Column(Integer, ForeignKey("tv_channels.id"), nullable=False)

    satellite = relationship("Satellite", back_populates="broadcasts")
    tv_channel = relationship("TVChannel", back_populates="broadcasts")
