from sqlalchemy import Column, String, Integer
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base

#konfiguracja odowłań do tabel w bazie danych
base = declarative_base() 
class Water(base):
    __tablename__ = 'water_4326' 
    gid = Column(Integer, primary_key = True)
    name = Column(String())
    fclass = Column(String())
    geom = Column(Geometry('MULITPOLYGON',4326))
    __table_args__ = {'schema': 'app'}

class Roads(base):
    __tablename__ = 'roads_4326' 
    gid = Column(Integer, primary_key = True)
    name = Column(String())
    fclass = Column(String())
    geom = Column(Geometry('MULILINESTRING',4326))
    __table_args__ = {'schema': 'app'}
 
