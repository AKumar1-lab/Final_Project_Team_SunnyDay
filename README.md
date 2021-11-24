### Team_SunnyDay_Analysis

Final Project

<img width="700" alt="Capture Solar Panel" src="https://user-images.githubusercontent.com/85860367/142750175-5b573739-ce7b-4ffc-a5bc-c17afdbc526f.PNG">


##### Team Members: 
[Jake Zebker](https://github.com/jzebker)

[Kellen Schmitz](https://github.com/KellenSchmitz)

[Chung In "Angel" Ngan](https://github.com/angelnga)

[Angela Kumar](https://github.com/AKumar1-lab)

### Presentation

[Google Presentation](https://docs.google.com/presentation/d/1NlID66oew1rf0fiu6xpsiVMICq4d7zu0/edit?usp=sharing&ouid=105447566363535601541&rtpof=true&sd=true)

#### Selected topic: 

Analysis of solar energy potential based on the zip code in the Contiguous United States has the potential cost savings on electricity and the machine learning prediction does zip code qualify based on the number of sunny days or global horizontal irradiance(GHI) in that location, if so, how much will be the system installation and how many years will it take to breakeven.

The definition of Global Horizontal Irradiance measures the intensity of the sun in a given location around the globe.  However for the purpose of this project, we have focused only on the Contiguous United States (excluding Alaska and Hawaii).

#### Purpose and Why the topic was selected :

Create a simple tool to help people estimate how much it would cost to install rooftop solar on their home.

Key Inputs: 

- Sun intensity by location (measured in GHI)
- Current electricity usage
- Electricity cost

Key Outputs:

- Size of solar system needed
- Upfront system cost
- Number of years for system to pay for itself (payback period)


The topic was selected due many factors: 

 * Climate change and global warming
 * Power outages, wildfires, and other natural disasters 
 * Increased greenhouse gas emissions
 * Increased interest in renewable energy specifically rooftop solar and energy storage.
 * Cost savings on electric

#### Overview

Analysis on how much it would cost to install rooftop solar on their home and what will be the return on investment after the number of years after the solar system installation.

#### Questions we hope to answer with the data

When the user enters variables such as zip code and current electric bill does the global horizontal irradiance predict accurately for the zip code entered?

Based on the zip code,average electric rates the state incurs per kWh along with average cost of the the solar system installation, how many years does it take to breakeven on the cost?

How many years does it take to breakeven on the cost?

What size of solar system is needed to cover electricity usage?

#### Description of the Data Exploration phase of the project

Through the data exploration pre-processing steps, the team examined how the databases interconnected  Additionally field values were unlocked and mapped to their column names. Columns with an overwhelming amount of null data were accessed for their feasibility in the data examination. The challenge of collecting data sets that had current data was hard to find; most data was historical, already 3-5 years old.  Once the dataset was selected, there were numerous variables that would be applicable to the topic.

#### Description of the source of data 

Most data was related to electric prices, GHI, latitude, longitude, zipcodes or states.  For the Tableau data visualization the data source included Carbon Dioxide (CO2), Nitrogen Oxide(NOx), and Sulfur Oxide(SO2) emissions by state. The datasets were from governmental sources that were free or required an API.

**Resources:**

Source: U.S Energy Information Adminstration (EIA)
Electricity Rates by State -

https://www.eia.gov/electricity/state/
https://www.eia.gov/electricity/data/state/avgprice_annual.xlsx

Source:  U.S Zipcodes/Postal Code Data
US Zipcode Database - 

https://www.unitedstateszipcodes.org/zip-code-database/

Source: National Renewable Energy Laboratory
Solar PV Supply Data -
https://www.nrel.gov/gis/index.html
https://www.nrel.gov/gis/solar-supply-curves.html
https://developer.nrel.gov/docs/solar/nsrdb/ = GHI based on longitude and latitude

References: Sengupta, M., Y. Xie, A. Lopez, A. Habte, G. Maclaurin, and J. Shelby. 2018. "The National Solar Radiation Data Base (NSRDB)." Renewable and Sustainable Energy Reviews  89 (June): 51-60.

Additional sources include: Department of Energy, NOAA.gov, NASA, trade groups, US Census Data

**Data:** 

pv_open_2020.csv; zip_codes_electic.csv;avg_price_annual; elecrates_pickle.ipynb;model.pkl;

**Data Tools:**

ML_model.ipynb;app.py

**Languages and Technologies:** 

To read the data into Jupyter Notebooks for analysis: Used Excel and CSV files

To query, manipulate, clean the data in Jupyter Notebooks:  Python, Pandas;

To visualize the data: used Tableau to present the maps of GHI, Electric Rates, Emissions

For Machine Learning, used Pandas, Scikit-Learn Libraries, Google Colaboratory, TensorFlow

To ensure that the Machine Learning app works and available for user input:  Pickle file, JavaScript, Flask app.py, html; VSCode; MapBox; Github Pages.

To ensure that the Machine Learning connected to a data storage SQLAlchemy was used to connect to PostgreSQL.  PgAdmin4 was used to verify that the data was read into the table as ordered.

For the presentation used Google Sheets, Google Slides and for the live presentation used Zoom

#### GitHub

Each link takes the user to the individual team member's repository for prospective employers, team, colleagues to show their portfolio.
In the Final_Project_Team_SunnyDay repository each member has their own branch.

#### Description of the Analysis Phase of the project

To find the cost of a solar system, we need to first identify the variables that go into the calculation.
These variables can be grouped into two buckets:

1)Those that determine system size; and,

2)Those that determine the cost of the system components + installation/overhead

To calculate system size, we needed to know the sun intensity (GHI) in the user’s area and their monthly electricity usage.
* The user inputs their zip code for location and their monthly electricity bill for electricity usage.
* Location is the main determinant of the sun’s intensity (GHI)
* How big of system you need will depend on how intense the sun is in your area and how much electricity you consume.

For example, you can see that the GHI for Seattle is much lower than for Phoenix, and even with the same electricity consumption, the system you need in Phoenix is ~40% smaller than the one you need in Seattle

The actual cost of installation was easy to find. Using a market study from NREL we were able to get estimates for the cost of system components and installation costs on a  per watt basis. Then all we had to do was multiply that value by the system size.

Then with both the system size and system cost, we could then calculate the the payback period, which is a function of local electricity prices and initial system cost.

So, for Seattle it will take roughly 20 years for the savings from solar to repay the initial cost and only 10 years in Phoenix.

<img width="582" alt="Data Analysis on systems" src="https://user-images.githubusercontent.com/85860367/143195770-274db85f-cc7e-49b2-b128-f217d6527b40.PNG">

#### Machine Learning Model

Machine Learning Goal: Predict amount of time to pay back solar installation price from savings on electric bill.

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

<img width="837" alt="image of solar roi" src="https://user-images.githubusercontent.com/85860367/143205617-d668379a-af95-4368-b289-c5880f346fd8.PNG">

<img width="837" alt="image of solar roi part 2" src="https://user-images.githubusercontent.com/85860367/143205353-97a5a808-9817-4a79-b5d4-6bc07354235f.PNG">


#### Database Integration

PostgreSQL was used to store the data as the Machine learning Model connected via SQLAlchemy

<img width= "359" alt="QuickDBD-export FINAL" src="https://user-images.githubusercontent.com/85860367/143191496-6611cf21-f283-444f-9627-3ef99c2eed0e.png">

<img width="500" alt="SQL to ML Model screenshot" src="https://user-images.githubusercontent.com/85860367/142750454-df90466d-ddaa-4321-9cdc-7946d1740904.PNG">

#### Dashboard and Storyboard

Visualization: Tableau and enable it on webpage with html, the screenshot is found in the Machine Learning section.

Use lat and long to create map and include corresponding elements to present data by state, create layout with graph and description in dashboard, and then add dashboards into a story.

Enable Tableau to webpage with html code, so user can interact with the graph in live. Edit website layout so that the Tableau is on a separate page from the main, navigation bar was included for better user experience.

![Why Go Solar Energy electric rates](https://user-images.githubusercontent.com/85860367/142751069-a899f099-425f-4899-b4f7-be0fcf095a93.png)

![Why Go Solar Energy power outages](https://user-images.githubusercontent.com/85860367/142751076-3e947361-3a1c-4f11-9326-b1e026273359.png)

![Why Go Solar Energy emissions](https://user-images.githubusercontent.com/85860367/142751089-319338eb-3515-41ba-9b52-21ac9352ab34.png)

![Why Go Solar Energy ghi](https://user-images.githubusercontent.com/85860367/142751105-94af2a39-b382-408c-824b-07e3c345d1e0.png)


#### Summary of Team Findings

Summary Findings by the team:  Increase trend of renewable energy such solar such as rooftop solar; electric prices are increasing per year so investing in solar reduces the electric cost over the life of the installation. It is forecasted that climate change will worsen over time such as drought, wildfire and greenhouse gas emissions.  There is a push to decarbonize the environment.    

#### Result of the analysis



#### Recommendation for future analysis

There was a search conducted on unrelated datasets on US Census Datasets in the areas of the following:

    *population, 
    *income disparity, 
    *labor, and 
    *congressional districts.  
    
 This further analysis would give us more insight on who and where the solar adopters are.

* Suggestions for future statistical analysis
     - Look deeper into electric power
        • how is the electricity being generated
        • look at prices on a finer scale
     - Look at alternative forms of energy that may be prevalent in given regions
        • geothermal, higher ground temperatures or might not need to dig as deep into the ground in some areas
        • wind, windier in some areas and construction costs vary
        • hydroelectric, river locations and cleanliness of water
     - Look at specific energy needs in different regions (ex: less need for heating in Southern California than in Minnesota)


#### Anything the team would have done differently




#### Conclusion

Data can be made to forge a relationship with unrelated data to gain more insight, perspectives, or have better outcomes with Python, Pandas, PostgreSQL.
We learned new technologies to present our findings with Tableau, Plotly, and Javascript
It is how we are able to use data to communicate our ideas, persuade another to make key decisions. 
Data is used to review trends and patterns and can train the computer to make predictions or test assumptions using supervised and unsupervised machine learning.



 



