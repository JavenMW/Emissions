To see functionality, head on over to: https://co2buddy.streamlit.app/

(If the app has gone inactive, expect a cold start period of 1-2 minutes. After this period, predictions should work instantly.)

# Project Outline

This project will be outlined using IBM's John Rollins's data science methodology.

## Business Understanding
For this project's problem statement, ChatGPT will be used to generate a problem statement based on the dataset.

### Project Statement
The government or a research organization wants to predict the CO2 emissions of vehicles based on their attributes (e.g., engine size, weight, fuel type, model year). This information could help policymakers create regulations to reduce CO2 emissions, or consumers could use it to select vehicles with lower emissions.

### Expected Outcome
- A model that accurately predicts CO2 emissions based on vehicle features.
- Insights into which vehicle attributes (engine size, fuel type, weight, etc.) are the most important predictors.

## Analytic Approach
Since our client wants to know what will happen based on vehicle traits, predictive analysis will be our best approach to solving this problem.

### Predictive Analysis
- Since our dependent variable is numerical, we are going to use different types of regression models.
    1. XGBoost - specifically xgbregressor for its performance.

## Data Requirements
Identify any confounding errors and the necessary and relevant features

Confounding errors: Commercial, cargo vehicles
- Vehicles such as buses, dump trucks, and 18-wheelers will likely have higher emissions

Relevant features seen within our dataset
- Engine size - typically, the bigger the engine, the more gas it  uses, leading to more emissions.
- gas type - dirty gas types can cause vehicles to perform less efficiently, leading to lower vehicle emissions.
- vehicle type - different types of vehicles-sizes and uses can lead to lighter or heavier use, which can cause more emissions.
- MPG rating - Low MPG ratings mean more gas is being used per gallon, which can lead to higher emissions. 

## Data Collection
No API's, no databases, we are just going to be using a simple kaggle dataset.

Kaggle dataset: path = kagglehub.dataset_download("debajyotipodder/co2-emission-by-vehicles")

Why this dataset?
- This is a clean dataset with no missing values or data errors. EDA will be easy starting out.
- This dataset is based in Canada, so it will have a regional bias. 
- Data represents most cars seen on the road today


## Data Understanding
Understand relationships, visualize outliers, identify bad data, and form your story. Exploratory Data Analysis will take place here before cleaning begins in the data preparation stage.

Types of Exploratory Data Analysis:
- Note relations between C02 emissions and other variables (and any correlations between independent variables)
- Identify unique values within make, model, vehicle class, and transmission
- Identify skewness with histograms
- Make assumptions about my data to formulate a story



## Data Preparation
Clean the data per the identified bad data. Select and engineer features.

Clean the data
- Determine the standard for filling in missing values
- Any punctuation errors seen in strings

Preprocess the data:
- Feature Engineering
    - Combine engine size and fuel consumption to obtain a sort of efficiency rating. The higher the rating, the more efficient the vehicle is.
    - Same thing with Cylinders and fuel consumption

- Feature Selection
    - Sequential feature selection


## Modeling
Begin modeling data following the methods outlined in the analytical approach. Does our model meet our business requirements?

Looking at our data we decided to start with 3 of the 5 mentioned models.
1. XGBoost - for its performance. It provides us with high performance, while maintaining some readability.

## Evaluation
This is how we plan to test our model's effectiveness at answering the initial question when new data is introduced.

Regression Evaluation Metrics:
- RMSE - tells us the distance between our predictions and actual results. The lower the better.
- R2 - This will tell us how much of our dependent variable can be explained by our independent variables


## Deployment
This is where we hand our model to key business stakeholders to test the performance of our product.

The goal here is to create a simple py script that hooks up to our model through an api, allowing the API to be accessed through the py script.
- Create an .ipynb notebook to explore our data and create our model
- Create .py script to feed data into the model, which outputs results
- Put files into a Docker container
- Utilize Streamlit to guide user interaction with the model.

## Feedback
Receive feedback from your client to determine if the model needs to be adjusted. IE, too many confounding errors.

Implement a way to leave comments in a text file. 

Or

Add my email address
