### Team_SunnyDay_Analysis

Final Project

<img width="700" alt="Capture Solar Panel" src="https://user-images.githubusercontent.com/85860367/142750175-5b573739-ce7b-4ffc-a5bc-c17afdbc526f.PNG">


##### Team Members: 
[Jake Zebker](https://github.com/jzebker)

[Kellen Schmitz](https://github.com/KellenSchmitz)

[Chung In "Angel" Ngan](https://github.com/angelnga)

[Angela Kumar](https://github.com/AKumar1-lab)

### Presentation

Google Presentation(link to google slides)

#### Selected topic: 

Global Horizontal Irradiance measures the brightness of the sun in a given location around the globe.  However for the purpose of this project, we have focused only on the Contiguous United States (excluding Alaska and Hawaii).

Analysis of solar energy potential based on the zip code in the Contiguous United States has the potential cost savings on electricity and the machine learning prediction does zip code qualify based on the number of sunny days or global horizontal irradiance(GHI) in that location, if so, how much will be the system installation and how many years will it take to breakeven.

#### Purpose or Why the topic was selected :

Climate change is real, and renewable energy such as solar power is becoming the choice to save on electricity costs.
The topic was selected due many factors: 

 * Climate change and global warming
 * Power outages, wildfires, and other natural disasters 
 * Increased greenhouse gas emissions
 * Increased interest in renewable energy specifically rooftop solar and energy storage.
 * Cost savings on electric

#### Overview

Machine Learning Goal: Predict amount of time to pay back solar installation price from savings on electric bill.

Visualization:  Mapping the number of sunny days that a location receives on average. Mapping the Greenhouse Emissions,  
Graph average electricity price for given area

Story telling: Mapbox/JS/Plotly or Tableau story board 

#### Description of their source of data 

**Resources:**

Electricity Rates by State -

https://www.eia.gov/electricity/state/
https://www.eia.gov/electricity/data/state/avgprice_annual.xlsx

US Zipcode Database - 

https://www.unitedstateszipcodes.org/zip-code-database/

Solar PV Supply Data -
https://www.nrel.gov/gis/index.html
https://www.nrel.gov/gis/solar-supply-curves.html
https://developer.nrel.gov/docs/solar/nsrdb/ = GHI based on longitude and latitude

References: Sengupta, M., Y. Xie, A. Lopez, A. Habte, G. Maclaurin, and J. Shelby. 2018. "The National Solar Radiation Data Base (NSRDB)." Renewable and Sustainable Energy Reviews  89 (June): 51-60.

Additional sources include: Department of Energy, NOAA.gov, NASA, trade groups

**Data:** 

pv_open_2020.csv; zip_code_database.csv; avgprice_annual.csv

**Data Tools:**

ML_model.ipynb;

**Languages and Technologies:** 

To read the data into Jupyter Notebooks: Used Excel and CSV files

To query, manipulate, clean the data in Jupyter Notebooks:  Python, Pandas;

To visualize the data: used Tableau to present the maps of GHI, Electric Rates, Emissions

For Machine Learning, used Pandas, SkiLearn Libraries, Google Colaboratory

To ensure that the Machine Learning app works and available for user input:  Pickle file, JavaScript, Flask app.py, html; VSCode; MapBox; Github Pages.

To ensure that the Machine Learning connected to a data storage SQLAlchemy was used to connect to PostgreSQL.  PgAdmin4 was used to verify that the data was read into the table as ordered.

For the presentation used Google Sheets, Google Slides and for the live presentation used Zoom

#### Questions we hope to answer with the data

When the user enters variables such as zip code and current electric bill does the global horizontal irradiance predict accurately for the zip code entered?

Based on the zip code,average electric rates the state incurs per kwh along with average cost of the the solar system installation, how many years does it take to breakeven on the cost?

#### GitHub

Each link takes the user to the individual team member's repository for prospective employers, team, colleagues to show their portfolio.
In the Final_Project_Team_SunnyDay repository each member has their own branch.


#### Machine Learning Model

<img width="362" alt="Flask app screenshot" src="https://user-images.githubusercontent.com/85860367/142750812-f257a1b0-0720-41c4-8871-5fdceb4393a6.PNG">


#### Database Integration

PostgreSQL was used to store the data as the Machine learning Model connected via SQLAlchemy

<img width="359" alt="SQL to ML Model screenshot" src="https://user-images.githubusercontent.com/85860367/142750454-df90466d-ddaa-4321-9cdc-7946d1740904.PNG">

#### Dashboard

![Why Go Solar Energy electric rates](https://user-images.githubusercontent.com/85860367/142751069-a899f099-425f-4899-b4f7-be0fcf095a93.png)

![Why Go Solar Energy power outages](https://user-images.githubusercontent.com/85860367/142751076-3e947361-3a1c-4f11-9326-b1e026273359.png)

![Why Go Solar Energy emissions](https://user-images.githubusercontent.com/85860367/142751089-319338eb-3515-41ba-9b52-21ac9352ab34.png)

![Why Go Solar Energy ghi](https://user-images.githubusercontent.com/85860367/142751105-94af2a39-b382-408c-824b-07e3c345d1e0.png)


#### First Segment: Sketch It Out 

Selection of a topic

Discussion on datasets, data visualization, and technologies.


#### Second Segment: Build the Pieces

Refined the topic further based on dataset found and interest
Github with branches created for each members, but also referencing their own repository for prospective career opportunities.
Google slide presentation shared among all collaborators
Machine Learning component has been been completed, will need to refine and embed into presentation and tableau or github pages.
Data visualization still to complete with additional graphs , we have a partial storyboard.

#### Third Segment - Plug It In



#### Fourth Segment - Putting It All Together




#### Summary of Team Findings


#### Conclusion



 



