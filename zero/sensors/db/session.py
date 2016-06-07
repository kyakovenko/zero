__import__ = ['session', ]

from .models import RoomMetrics, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.query(RoomMetrics).all()

