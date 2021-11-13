# Importing dependencies
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def predict_ghi(latitude,longitude):
    # Read in data
    df=pd.read_csv('pv_open_2020.csv')

    # Choose model feaatures
    X = df[['latitude','longitude']].values
    y = df['global_horizontal_irradiance'].values

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

    # Fit to model
    regressor = RandomForestRegressor(n_estimators=10)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)

    # Create model
    pickle.dump(regressor, open('model.pkl','wb'))
    model = pickle.load( open('model.pkl','rb'))

    # Return predictions
    ghi = model.predict([[latitude,longitude]])
    return ghi