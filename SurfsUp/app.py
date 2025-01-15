# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the last 12 months of precipitation data."""
    # Find the most recent date in the dataset
    most_recent_date = session.query(func.max(measurement.date)).scalar()
    one_year_ago = (np.datetime64(most_recent_date) - np.timedelta64(365, 'D')).astype(str)

    # Query precipitation data
    precipitation_data = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= one_year_ago).all()

    # Convert to dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations."""
    results = session.query(measurement.station).all()
    stations_list = [station[0] for station in results]
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the dates and temperature observations of the most active station for the last year."""
    # Find the most active station
    most_active_station = session.query(measurement.station).\
        group_by(measurement.station).\
        order_by(func.count(measurement.station).desc()).first()[0]

    # Find the most recent date
    most_recent_date = session.query(func.max(measurement.date)).scalar()
    one_year_ago = (np.datetime64(most_recent_date) - np.timedelta64(365, 'D')).astype(str)

    # Query the temperature observations
    tobs_data = session.query(measurement.date, measurement.tobs).\
        filter(measurement.station == most_active_station).\
        filter(measurement.date >= one_year_ago).all()

    tobs_list = [tobs for date, tobs in tobs_data]
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start, end=None):
    """Return TMIN, TAVG, and TMAX for a specified date range."""
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]

    if not end:
        results = session.query(*sel).filter(measurement.date >= start).all()
    else:
        results = session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()

    temp_stats = list(results[0])
    return jsonify(temp_stats)


if __name__ == "__main__":
    app.run(debug=True)