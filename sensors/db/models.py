from sqlalchemy import Column
from sqlalchemy import types 
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
 
class RoomMetrics(Base):
    __tablename__ = 'temperature'
    id = Column(types.Integer, primary_key=True)
    temperature = Column(types.Numeric(2, 2), nullable=False)
    humidity = Column(types.Numeric(2, 2), nullable=False)
    appended = Column(types.DateTime, default=func.now())

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.create_all(engine)
