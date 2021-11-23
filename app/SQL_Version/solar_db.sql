CREATE TABLE electricity (
    Year INT,
    State VARCHAR,
    Industry_Sector_Category VARCHAR,
    Residential FLOAT
);

CREATE TABLE zipcodes (
    zip INT,
    type VARCHAR,
    decommissioned INT,
    primary_city VARCHAR,
    acceptable_cities VARCHAR,
    unacceptable_cities VARCHAR,
    state VARCHAR,
    county VARCHAR,
    timezone VARCHAR,
    area_codes VARCHAR,
    world_region VARCHAR,
    country VARCHAR,
    latitude FLOAT,
    longitude FLOAT,
    irs_estimated_population INT
);

CREATE TABLE solar (
    sc_gid INT,
    capacity_factor DECIMAL,
    global_horizontal_irradiance DECIMAL,
    capacity_mw DECIMAL,
    area_sq_km DECIMAL,
    latitude DECIMAL,
    longitude DECIMAL,
    distance_to_transmission_km DECIMAL
);

COPY electricity FROM '/Users/jacobzebker/Public/avgprice_annual.csv' DELIMITER ',' CSV HEADER;
COPY solar FROM '/Users/jacobzebker/Public/pv_open_2020.csv' DELIMITER ',' CSV HEADER;
COPY zipcodes FROM '/Users/jacobzebker/Public/zip_code_database.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE zips_electric AS (
SELECT z.zip as ZIP,z.state,z.county,z.latitude,z.longitude,e.residential as rate FROM zipcodes z
INNER JOIN electricity e ON e.state=z.state
WHERE e.industry_sector_category='Total Electric Industry' AND e.year=2020
	)