--create the table for the data.gov data
DROP TABLE IF EXISTS obesity_table;
CREATE TABLE obesity_table(
	"year" VARCHAR   NOT NULL,
    "stateabbr" VARCHAR   NOT NULL,
    "statename" VARCHAR   NOT NULL,
    "cityname" VARCHAR   NOT NULL,
    "obesitypercentage" VARCHAR  NOT NULL,
	"Population2010" VARCHAR   NOT NULL,
    "latitude" FLOAT  NOT NULL,
    "longitude" FLOAT  NOT NULL
);

--create the table for the cdc data
DROP TABLE IF EXISTS cdc_data;
CREATE TABLE cdc_data(
	"stateid" VARCHAR,
	"percentage(obese)" FLOAT,
	"gender" VARCHAR
);	

--create the table for the census population data
DROP TABLE IF EXISTS census_data;
CREATE TABLE census_data(
	"state" VARCHAR primary key,
	"totalpopulation(census 2010)" INT,
	"population(est 2014)" INT
);		