import pandas as pd
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
obesity = Base.metadata.tables['obesity_table']
session = Session(engine)

obesity_df.to_sql(name='obesity_table',con=engine, if_exists='append',index=False)

#======================================================
# Flask app
#======================================================
app = Flask(__name__)

@app.route("/")
def Home():
    print("Server received request for 'Home' page...")
    return("<div ><p><h1> Welcome to the Climate App!</h1></p>"
  "</ol><li><strong font color ='blue'>Obesity study for 500 cities in the US: </strong><font color='orange'> /api/v1.0/500Cities</font></li>"
  "<li><strong>List of station:</strong><font color='orange'> /api/v1.0/bygender</font></li></ol></div>")

#===================================================
@app.route("/api/v1.0/500Cities")
def main():
    obesity_df =session.query(obesity)
    obesity_df = pd.read_sql(obesity_df.statement, obesity_df.session.bind)
    obesity_df = pd.DataFrame(obesity_df.loc[obesity_df["obesitypercentage"] >=45, :]) 
    obesity_df = obesity_df.to_dict()
    return jsonify(obesity_df)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    app.run(debug=True)
