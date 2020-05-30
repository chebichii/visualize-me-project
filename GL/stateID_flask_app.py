import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func ,inspect,Table, Column, ForeignKey
from flask import Flask, jsonify

#=======================================================
census_df = pd.read_csv('population_df_clean.csv')
census_df =pd.DataFrame(census_df)
#print (census_df)
#=======================================================

rds_connection_string = "postgres:postgres@localhost:5432/Obesity_data"
engine = create_engine(f'postgresql://{rds_connection_string}')
#https://github.com/cid-harvard/pandas-to-postgres/issues/8
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

census_data = Base.metadata.tables['census_data']
session = Session(engine)

census_df.to_sql(name='census_data',con=engine, if_exists='replace',index=False)

#======================================================
# Flask app
#======================================================
app = Flask(__name__)

@app.route("/")
def Home():
    print("Server received request for 'Home' page...")
    return("<div ><p><h1> Welcome to Obesity Study Api!</h1></p>"
  "</ol><li><strong font color ='blue'>Obesity study for 500 cities in the US: </strong><font color='orange'> /api/v1.0/population</font></li>"
  "<li><strong>List of station:</strong><font color='orange'> /api/v1.0/bygender</font></li></ol></div>")

#===================================================
@app.route("/api/v1.0/population")
def population():
    states = session.query(census_data)
    states = pd.read_sql('select * from census_data', con=engine)
    states = pd.DataFrame(states, columns=['state', 'population_est_2014'])
    states = states.to_dict()
    return jsonify(states)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    app.run(debug=True)
