# Import the dependencies.
from flask import Flask
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import func, create_engine
from sqlalchemy.ext.automap import automap_base

#################################################
# Database Setup
#################################################
engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
M = Base.classes.measurement
S = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    return '''
        <h2>Available routes:</h2>
        <ol>
            <li>/api/v1.0/precipitation</li>    
            <li>/api/v1.0/stations</li>    
            <li>/api/v1.0/tobs</li>    
            <li>/api/v1.0/[start]</li>    
            <li>/api/v1.0/[start]/[end]</li>   
        </ol> 
    '''

@app.route('/api/v1.0/precipitation')
def precipitation():
    results = session.query(M.date,M.prcp).filter(M.date>='2016-08-23').all()

    return [ {d:p} for d,p in results]
    
@app.route('/api/v1.0/stations')
def station ():
    results = session.query(S.station,S.name).all()

    return [ {id:loc} for id,loc in results]   

@app.route('/api/v1.0/tobs')
def station ():
    results = session.query(S.name, S.tobs).filter(station == 'USC00519281').all()

    return[{name:tobs} for name,tobs in results]   