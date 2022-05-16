from sqlalchemy import Column, String, Integer
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base() 
class Water(base):
    __tablename__ = 'water_4326' 
    gid = Column(Integer, primary_key = True)
    nazwa = Column(String())
    typ = Column(String())
    geom = Column(Geometry('MULITPOLYGON',4326))
    __table_args__ = {'schema': 'kornik'}

class Roads(base):
    __tablename__ = 'road_4326' 
    gid = Column(Integer, primary_key = True)
    nazwa = Column(String())
    typ = Column(String())
    geom = Column(Geometry('MULILINESTRING',4326))
    __table_args__ = {'schema': 'kornik'}
 
