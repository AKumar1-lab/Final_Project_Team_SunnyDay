

## Final_Project_Team_SunnyDay

* Final Project - Second Segment: Build the Pieces

Refined the topic further based on dataset found and interest
Github with branches created for each members, but also referencing their own repository for prospective career opportunities.
Google slide presentation shared among all collaborators
Machine Learning component has been been completed, will need to refine and embed into presentation and tableau or github pages.
Data visualization still to complete with additional graphs , we have a partial storyboard.

* Final Project - First Segment: Sketch It Out 
Selected a topic
Discussion on datasets, data visualization, and technologies.

##### Team Members: 
* Jake Zebker https://github.com/jzebker
* Kellen Schmitz https://github.com/KellenSchmitz
* Chung In "Angel" Ngan https://github.com/angelnga
* Angela Kumar https://github.com/AKumar1-lab

##### Selected topic: 

Analysis of solar energy potential for a given location (in US) to save on electricity and does one qualify based on the number of sunny days or global horizontal irradiance(GHI) that your state incurs.  

Global Horizontal Irradiance measures the brightness of the sun in a given location around the globe.  However for the purpose of this project, we have focused only on the United States.

### Purpose

Climate change is real, and renewable energy such as solar power is becoming the choice to save on electricity costs.
The topic was selected due many factors: 

 * Climate change and global warming
 * Power outages, wildfires, and other natural disasters 
 * Increased greenhouse gas emissions
 * Increased interest in renewable energy specifically rooftop solar and energy storage.
 * Cost savings on electric


### Overview

Machine Learning: 
Predicting the amount of time to pay back solar installation costs from savings on electric bill from user input zipcode and monthly bill

 * Data was pretty clean to begin with so not much preprocessing was necessary
     - Chose to include most recent electric rate data (2020)
     - Chose residential electric rates because likely user is a home owner looking to install solar
     - Added electric rates to zipcode database for simplicity
 * Feature engineering 
     - Issue to be solved: did not have GHI values for every zip code in the contiguous US, GHI is measured at different locations throughout the country
     - Solution: use the values we have (latitude and longitude) to predict values we don't have (GHI)
 * Randomly chose 1/3 of data to be test set
 * Model choice, RandomForestRegression
     - Benefits: works well on large dataset, works well on continuous data like we have
     - Limitations: cannot predict values outside of our dataset
 * Changes to model
     - Initially tried to estimate by matching latitude and longitude values to nearby points that we had values for (within .1 degrees)
     - Switched to ML model because it worked faster and is more accurate
     - Looked at incorporating weather data but deemed unneccessary for ML model because measured GHI value should account for any changes in cloud cover
 * Model accuracy
     - R2 score is very high
     - Very few outliers in general and neighboring measured values show little change from point to point (GHI is similar in neighboring zip codes)
 * Suggestions for future statistical analysis
     - Look deeper into electric power
        • how is the electricity being generated
        • look at prices on a finer scale
     - Look at alternative forms of energy that may be prevalent in given regions
        • geothermal, higher ground temperatures or might not need to dig as deep into the ground in some areas
        • wind, windier in some areas and construction costs vary
        • hydroelectric, river locations and cleanliness of water
     - Look at specific energy needs in different regions (ex: less need for heating in Southern California than in Minnesota)

Visualization:  Mapping the number of sunny days that a location receives on average. Graph of solar potential over a year (showing seasonal variability) for the location. 
Graph of historical average electricity price for given area. Etc.

Story telling: Mapbox/JS/Plotly or Tableau story board 

### Description of their source of data 

Resources:

https://www.eia.gov/electricity/state/

https://www.nrel.gov/gis/index.html

https://www.nrel.gov/gis/solar-supply-curves.html

https://developer.nrel.gov/docs/solar/nsrdb/ = There is an API for some weather data, based on longitude and latitude

References: Sengupta, M., Y. Xie, A. Lopez, A. Habte, G. Maclaurin, and J. Shelby. 2018. "The National Solar Radiation Data Base (NSRDB)." Renewable and Sustainable Energy Reviews  89 (June): 51-60.

Additional likely sources include: WeatherData, Department of Energy, NOAA.gov, NASA, trade groups

Technologies:  Python, Pickle, JavaScript, SQLAlchemy, Google Colaboratory, Google Sheets, Google Slides.


### Questions they hope to answer with the data

When including variables such as zip code, latitude and longitude does the global horizontal irradiance predict accurately for the zip code entered?

Does the zip code entered fall into a bright zone or dark zone? Meaning farther from the sun, or in a location that has extreme weather? (i.e. rain, snow, fog, or other vulnerabilities)



 



