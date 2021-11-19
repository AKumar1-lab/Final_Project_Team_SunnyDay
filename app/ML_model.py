# Importing dependencies
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def predict_ghi(zipcode,monthly_bill):
    # Read in data - SQL/Postgrsql
    #engine = create_engine("postgresql://postgres:<password>@localhost:5432/<db-name>")
    #df=pd.read_sql("SELECT * FROM solar;", engine)
    #zips=pd.read_sql("SELECT * FROM zips_electric;", engine)

    # Read in data - Pandas
    df=pd.read_csv('pv_open_2020.csv')
    zips=pd.read_csv('zipcodes_electric.csv')

    # Get lat,lng and elec_rate from zipcode
    coords=zips.loc[zips['zip']==int(zipcode)][['latitude','longitude']].values
    #elec_rate=zips.loc[zips['zip']==int(zipcode)][['rate']].values #name for sql table
    elec_rate=zips.loc[zips['zip']==int(zipcode)][['residential_electric_rate_(cents/kWh)']].values
    elec_rate=elec_rate/100

    # Get County, State
    county_state=zips.loc[zips['zip']==int(zipcode)][['county','state']].values
    
    # Calculate yearly bill from user input monthly bill
    yearly_bill=monthly_bill*12
    yearly_elec_use=yearly_bill/elec_rate

    # Choose model features
    X = df[['latitude','longitude']].values
    y = df['global_horizontal_irradiance'].values

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

    # Fit to model
    regressor = RandomForestRegressor(n_estimators=10)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)

    # Return predictions and metrics
    r2 = r2_score(y_test, y_pred)
    ghi = regressor.predict(coords)
    return ghi,coords,r2,yearly_elec_use,yearly_bill,county_state