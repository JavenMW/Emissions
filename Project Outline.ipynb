{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project Outline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This project will be outlined using the Data Science methodology that was coined by IBM's John Rollins. This process is meant to be highly interative."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Business Understanding\n",
    "For this project's problem statement, ChatGPT will be used to generate a problem statement based off of the dataset."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Project Statement\n",
    "The government or a research organization wants to predict the CO2 emissions of vehicles based on their attributes (e.g., engine size, weight, fuel type, model year). This could help policymakers create regulations for reducing CO2 emissions, or consumers could use this information to select vehicles with lower emissions.\n",
    "\n",
    "### Expected Outcome\n",
    "- A model that accurately predicts CO2 emissions based on vehicle features.\n",
    "- Insights into which vehicle attributes (engine size, fuel type, weight, etc.) are the most important predictors."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Analytic Approach\n",
    "Since our client is wanting to know what will happen based on vehicle traits, predictive analysis will be our best approach to solving this problem."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Predicitive Analysis\n",
    "- Since our dependent variable is numerical, we are going to use different types of regression models.\n",
    "    1. Multinomial Logit Regression - for simplicity\n",
    "    2. Decision Trees Regressor - for readability\n",
    "    3. Random Forests Regressor - for high-dimensionality\n",
    "    4. Gradince Boosted Machines (GBM) - high performance\n",
    "    5. Nearal Networks - if we find ourselves with alot of data."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Requirements\n",
    "Identify any confounding errors and the necessary and relevant features"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Confounding errors: Commercial, luxury, cargo vehicles\n",
    "- vehicles such as busses, dump trucks, high end sports and luxury cars, and 18 wheelers will likely have higher emissions\n",
    "\n",
    "Relevant features seen within our dataset\n",
    "- Engine size - typically the bigger the engine the more gas uses, leading to more emissions.\n",
    "- gas type - dirty gas types can cause vehicles to perform less efficiently leading to lower vehicle emissions.\n",
    "- vehicle type - different types of vehicles size and uses can lead to lighter or heavier use which can cause more emissions.\n",
    "- MPG rating - low mpg ratings means more gas is being used per gallon, which can lead to higher emissions. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Collection\n",
    "No API's, no databases, we are just going to be using a simple kaggle dataset."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Kaggle dataset: path = kagglehub.dataset_download(\"debajyotipodder/co2-emission-by-vehicles\")\n",
    "\n",
    "Why this dataset?\n",
    "- This is a clean dataset with no missing values or data errors. EDA will be easy starting out.\n",
    "- This dataset is based out of Canada so it will have a region bias. \n",
    "- Data represents most cars seen on the road today\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Understanding\n",
    "Understand relationships, visualize outliers, identify bad data, and form your story. Exploratory Data Analysis will take place here before cleaning begins in the data preparation stage."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Types of Exploratory Data Analysis:\n",
    "- Note relations between C02 emissions and other variables (and any correlations between independent variables)\n",
    "- Identify unique values within make, model, vehicle class, and transmission\n",
    "- Visualize outliers with box and whisker plots\n",
    "- Identify skewness with histograms\n",
    "- Make assumptions about my data to formulate a story\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Prepartation\n",
    "Clean data in accordance with the indentified bad data. Select and engineer features."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Clean the data\n",
    "- Determine standard for filling in missing values\n",
    "- Remove skewness through winsorization or trimmed mean methods\n",
    "- Any punctuation errors seen in strings\n",
    "\n",
    "Preprocess the data:\n",
    "- Feature Engineering\n",
    "    - Combine engine size and fuel consumption to obtain a sort of efficiency rating. The higher the rating, the more efficient the vehicle is.\n",
    "    - Same thing with Cylinders and fuel consumption\n",
    "\n",
    "- Feature Selection\n",
    "    - Utilize stepwise correlation to identify useful variables\n",
    "    - Forward selection\n",
    "    - Correlation Matrix to identify highly correlated features\n",
    "\n",
    "- One hot encoding for our categorical variables\n",
    "- Feature scaling / MinMax Scaling for model readability\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Modeling\n",
    "Begin modeling data in accordance with the methods outlined in the analytical approach. Does our model meet our business requirements?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Looking at our data we decided to start with 3 of the 5 mentioned models.\n",
    "1. Multinomial Logit Regression - for simplicity. If you can have a model that is efficient, low cost, and delivers good accuracy then we will use it. As this will gives us the most efficient way of predicting results.\n",
    "\n",
    "2. Random Forest Regressor - for high dimensionality. Our \"Model\" variable contains many unique values and could overfit the model, but it would still be nice to have this data represented within our dataset. All of this while still being able to note feature importance with the use of SHAP LIME or .feature_importances_ from sci-kit learn.\n",
    "\n",
    "3. KNN Regression - for finding unseen relationships. Lets see if our model can find any groupings of data based off of their characteristics. Assigning a label to records seen with like characteristics."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Evaluation\n",
    "This is how we plan to test our models effectiveness at answering the inital question when new data is introduced."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Regression Evaluation Metrics:\n",
    "- OLS Regression Results - over interprability of model variables. \n",
    "- RMSE - tells us the the distance between our predictions and actual results. The lower the better.\n",
    "- R2 - this will tell us how much of our dependent variable can be explained by our independent variables\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Deployment\n",
    "This is where we hand our model to key business stakeholders to test the performance of our product."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The goal here is to create a simple py script that hooks up to our model through an api, allowing the API to be accessed through the py script.\n",
    "- Create .ipynb notebook to explore our data\n",
    "- Create .ipynb input new data from client and to output clean data for our model\n",
    "- Create .py script to feed data into model which outputs results\n",
    "- Create .py script to read results data and output insights\n",
    "- Tie it last four steps together in one script for ease of use."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Feedback\n",
    "Receive feed back from your client to determine if the model needs to be adjusted. IE too many confounding errors."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Implement either a way to leave comments in a text file. \n",
    "\n",
    "Or\n",
    "\n",
    "Add my email address"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
