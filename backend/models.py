from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=func.current_timestamp())
    alert_type = Column(String(50), nullable=False)
    data = Column(JSON)

class GenderDistribution(Base):
    __tablename__ = 'gender_distribution'
    id = Column(Integer, primary_key=True, autoincrement=True)
    male_count = Column(Integer, nullable=False)
    female_count = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=func.current_timestamp())

class WeatherInfo(Base):
    __tablename__ = 'weather_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Integer, nullable=False)
    condition = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=func.current_timestamp())
