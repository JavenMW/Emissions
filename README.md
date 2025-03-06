under construction
# Project Outline

This project will be outlined using the Data Science methodology that was coined by IBM's John Rollins. This process is meant to be highly interative.

## Business Understanding
For this project's problem statement, ChatGPT will be used to generate a problem statement based off of the dataset.

### Project Statement
The government or a research organization wants to predict the CO2 emissions of vehicles based on their attributes (e.g., engine size, weight, fuel type, model year). This could help policymakers create regulations for reducing CO2 emissions, or consumers could use this information to select vehicles with lower emissions.

### Expected Outcome
- A model that accurately predicts CO2 emissions based on vehicle features.
- Insights into which vehicle attributes (engine size, fuel type, weight, etc.) are the most important predictors.

## Analytic Approach
Since our client is wanting to know what will happen based on vehicle traits, predictive analysis will be our best approach to solving this problem.

### Predicitive Analysis
- Since our dependent variable is numerical, we are going to use different types of regression models.
    1. XGBoost - specifically xgbregressor for its performance.

## Data Requirements
Identify any confounding errors and the necessary and relevant features

Confounding errors: Commercial, cargo vehicles
- vehicles such as busses, dump trucks, and 18 wheelers will likely have higher emissions

Relevant features seen within our dataset
- Engine size - typically the bigger the engine the more gas uses, leading to more emissions.
- gas type - dirty gas types can cause vehicles to perform less efficiently leading to lower vehicle emissions.
- vehicle type - different types of vehicles size and uses can lead to lighter or heavier use which can cause more emissions.
- MPG rating - low mpg ratings means more gas is being used per gallon, which can lead to higher emissions. 

## Data Collection
No API's, no databases, we are just going to be using a simple kaggle dataset.

Kaggle dataset: path = kagglehub.dataset_download("debajyotipodder/co2-emission-by-vehicles")

Why this dataset?
- This is a clean dataset with no missing values or data errors. EDA will be easy starting out.
- This dataset is based out of Canada so it will have a region bias. 
- Data represents most cars seen on the road today


## Data Understanding
Understand relationships, visualize outliers, identify bad data, and form your story. Exploratory Data Analysis will take place here before cleaning begins in the data preparation stage.

Types of Exploratory Data Analysis:
- Note relations between C02 emissions and other variables (and any correlations between independent variables)
- Identify unique values within make, model, vehicle class, and transmission
- Identify skewness with histograms
- Make assumptions about my data to formulate a story



## Data Prepartation
Clean data in accordance with the indentified bad data. Select and engineer features.

Clean the data
- Determine standard for filling in missing values
- Any punctuation errors seen in strings

Preprocess the data:
- Feature Engineering
    - Combine engine size and fuel consumption to obtain a sort of efficiency rating. The higher the rating, the more efficient the vehicle is.
    - Same thing with Cylinders and fuel consumption

- Feature Selection
    - Sequential feature selection


## Modeling
Begin modeling data in accordance with the methods outlined in the analytical approach. Does our model meet our business requirements?

Looking at our data we decided to start with 3 of the 5 mentioned models.
1. XGBoost - for its performance. It provides us with high performance, while maintaining some readability.

## Evaluation
This is how we plan to test our models effectiveness at answering the inital question when new data is introduced.

Regression Evaluation Metrics:
- RMSE - tells us the the distance between our predictions and actual results. The lower the better.
- R2 - this will tell us how much of our dependent variable can be explained by our independent variables


## Deployment
This is where we hand our model to key business stakeholders to test the performance of our product.

The goal here is to create a simple py script that hooks up to our model through an api, allowing the API to be accessed through the py script.
- Create .ipynb notebook to explore our data and create our model
- Create .py script to feed data into model which outputs results
- Put files into a docker container
- Utilize streamlit to guide user interaction with the model.

## Feedback
Receive feed back from your client to determine if the model needs to be adjusted. IE too many confounding errors.

Implement either a way to leave comments in a text file. 

Or

Add my email address
