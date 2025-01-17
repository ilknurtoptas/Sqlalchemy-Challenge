# Sqlalchemy-Challenge
This project consists of two parts:

1-Climate Analysis and Data Exploration: Using Python and SQLAlchemy to analyze and explore climate data stored in an SQLite database.

2-Designing a Flask API: Developing an API based on the results of the climate analysis.

Part 1: Analyze and Explore the Climate Data

Requirements

Use the provided files (climate_starter.ipynb and hawaii.sqlite) for climate analysis and data exploration.

Tools: SQLAlchemy ORM queries, Pandas, and Matplotlib.

Steps

1. Database Connection

Use the create_engine() function from SQLAlchemy to connect to the SQLite database.

Reflect the database tables into SQLAlchemy ORM classes using automap_base().

Save references to the classes as station and measurement.

Link Python to the database by creating a SQLAlchemy session.

Important: Close the session at the end of your notebook.

2. Precipitation Analysis

Find the most recent date in the dataset.

Retrieve the previous 12 months of precipitation data using a query that selects only the "date" and "prcp" values.

Load the query results into a Pandas DataFrame and explicitly set the column names.

Sort the DataFrame values by "date".

Plot the results using the Pandas DataFrame plot method.

Print the summary statistics for the precipitation data using Pandas.

3. Station Analysis

Total Number of Stations: Design a query to calculate the total number of stations in the dataset.

Most-Active Stations:

List the stations and observation counts in descending order.

Identify the station ID with the greatest number of observations.

Temperature Statistics:

For the most-active station ID, calculate the lowest, highest, and average temperatures.

Retrieve the previous 12 months of temperature observation (TOBS) data for this station.

Plot the results as a histogram with bins=12.

4. Close the Session

Ensure the SQLAlchemy session is closed at the end of the notebook.

Part 2: Design Your Climate App

Using the results of your climate analysis, create a Flask API with the following routes:

Routes

1. /

Description: Home page that lists all available routes in the API.

2. /api/v1.0/precipitation

Description: Return the last 12 months of precipitation data as a JSON dictionary.

Key: Date.

Value: Precipitation (prcp).

3. /api/v1.0/stations

Description: Return a JSON list of all stations from the dataset.

4. /api/v1.0/tobs

Description: Return the dates and temperature observations (TOBS) for the most-active station for the last year.

Output: JSON list of temperature observations.

5. /api/v1.0/<start>

Description: Return a JSON list of the minimum, average, and maximum temperatures for all dates greater than or equal to the specified start date.

6. /api/v1.0/<start>/<end>

Description: Return a JSON list of the minimum, average, and maximum temperatures for the date range between start and end (inclusive).
