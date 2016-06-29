# -*- coding: utf-8 -*-
__author__ = 'Kirill Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'
__import__ = ['session', ]

from .models import RoomMetrics, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.query(RoomMetrics).all()

