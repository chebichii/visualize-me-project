import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func ,inspect,Table, Column, ForeignKey
from flask import Flask, jsonify

#=======================================================
obesity_df = pd.read_csv('data_proj2.csv')
obesity_df = obesity_df.dropna()
obesity_df =pd.DataFrame(obesity_df)
#=======================================================

rds_connection_string = "postgres:postgres@localhost:5432/Proj2_db"
engine = create_engine(f'postgresql://{rds_connection_string}')
#https://github.com/cid-harvard/pandas-to-postgres/issues/8
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
obesity = Base.metadata.tables['obesity_study']
cdc_data = Base.metadata.tables['cdc_data']
cdc_data = Base.metadata.tables['census_data']
session = Session(engine)

obesity_df.to_sql(name='obesity_study',con=engine, if_exists='replace',index=False)

#======================================================
# Flask app
#======================================================
app = Flask(__name__)

@app.route("/")
def Home():
    print("Server received request for 'Home' page...")
    return("<div ><p><h1> Welcome to Obesity Study Api!</h1></p>"
  "</ol><li><strong font color ='blue'>Obesity study for 500 cities in the US: </strong><font color='orange'> /api/v1.0/over45percent</font></li>"
  "<li><strong>List of station:</strong><font color='orange'> /api/v1.0/bygender</font></li></ol></div>")

#===================================================
@app.route("/api/v1.0/over45percent")
def main():
    obesity_query =session.query(obesity)
    obesity_query = pd.read_sql(obesity_query.statement, obesity_query.session.bind)
    obesity_query = pd.DataFrame(obesity_query.loc[obesity_query["obesitypercentage"] >=45, :]) 
    obesity_query = obesity_query.to_dict()
    return jsonify(obesity_query)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    app.run(debug=True)
