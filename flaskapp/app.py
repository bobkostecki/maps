from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import geoalchemy2.functions as geofunc
from models import  Roads, Water
import json
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db_string = "postgresql://postgres:beata@localhost:5432/wielkopolska"
db = create_engine(db_string)  
Session = sessionmaker(db)  
session = Session()


@app.route("/geojson-water", methods=['GET'])
def handle_drogi():
    features = session.query(geofunc.ST_AsGeoJSON(Water)).all()   
    return ({
        "type": "FeatureCollection",
        "features": [json.loads(mytuple[0]) for mytuple in features] 
        })

@app.route("/geojson-roads", methods=['GET'])
def handle_roads():
    features = session.query(geofunc.ST_AsGeoJSON(Roads)).all()   
    return ({
        "type": "FeatureCollection",
        "features": [json.loads(mytuple[0]) for mytuple in features] 
        })
    
@app.route('/')
def main():
    return render_template('main.html')

app.run()
