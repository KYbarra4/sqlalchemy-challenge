import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

base=automap_base()

base.prepare(autoload_with=engine)

measure=base.classes.measurement
station=base.classes.station

app= Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Hawaii Climate<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<start><br/>"
        f"/api/v1.0/start_date end_date <start> <end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(measure.date,measure.prcp).\
                filter(measure.date > '2016-08-23').\
                order_by(measure.date).all()
    session.close()
    all_perc = list(np.ravel(results))
    return jsonify(all_perc)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results =session.query(measure.station, func.count(measure.id)).\
        group_by(measure.station).order_by(func.count(measure.id).desc()).all()
    session.close()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results =session.query(measure.date,measure.tobs).\
                filter(measure.date > '2016-08-23').\
                filter(measure.date <= '2017-08-23').\
                filter(measure.station=='USC00519281').\
                order_by(measure.date.desc()).all()
    session.close()
    all_tobs = list(np.ravel(results))
    return jsonify(all_tobs)

@app.route("/api/v1.0/start_date/<start>")
def start_date(start):
    session = Session(engine)
    d1 = dt.datetime.strptime(start,'%y%m%d') 
    results =session.query(
                # measure.date,
                func.min(measure.tobs),
                func.max(measure.tobs),
                func.avg(measure.tobs)).filter(measure.date>=d1).all()
                # order_by(measure.date.desc()).all()
    session.close()
    # all_start = list(np.ravel(results))
    all_start = []
    for result in results:
        start_dict = {}
        # start_dict["date"]= result[0]
        start_dict["min"] = result[0]
        start_dict["max"] = result[1]
        start_dict["avg"] = result[2]
        all_start.append(start_dict)
    return jsonify(all_start)

@app.route("/api/v1.0/start_date end_date/<start> <end>")
def start_end_date(start, end):
    session = Session(engine)
    d1 = dt.datetime.strptime(start,'%y%m%d') 
    d2 = dt.datetime.strptime(end,'%y%m%d')
    results =session.query(
                # measure.date,
                func.min(measure.tobs),
                func.max(measure.tobs),
                func.avg(measure.tobs)).\
                filter(measure.date >d1).\
                filter(measure.date <= d2).all()
                # order_by(measure.date.desc()).all()
    session.close()

    all_start_end = []
    for result in results:
        start_end_dict = {}
        start_end_dict["min"] = result[0]
        start_end_dict["max"] = result[1]
        start_end_dict["avg"] = result[2]
        all_start_end.append(start_end_dict)
    return jsonify(all_start_end)

    # all_start_end = list(np.ravel(results))
    # return jsonify(all_start_end)


if __name__ == '__main__':
    app.run(debug=True)