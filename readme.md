
README file for  Zillow Project

Provides insight for goals of project and how to reproduce.

Project Goal
Identify the key drivers from the Zillow data set and how they effect home prices.


Data Dictionary

Feature	Data Type	Description
parcelid	int64	Unique parcel identifier
bed	float64	count of bedrooms
bath	float64	count of bathrooms
sqrft	float64	Total livable square footage
county # 6037	float64	Los Angeles
county # 6059	float64	Orange
county # 6111	float64	Ventura
year_built	float64	year home was built
taxval	float64	total value of home established by taxing authority
taxamt	float64	The most recent year property taxes were assessed
propertylandusetypeid # 260	float64	property type - Residential General
propertylandusetypeid # 261	float64	property type - Single Family Residential
propertylandusetypeid # 263	float64	property type - Mobile Home
propertylandusetypeid # 264	float64	property type - Townhouse
tax_rate	float64	This is property tax / tax_assessed_value

Initial Hypotheses
Hypothesis 1 - I rejected the Null Hypothesis; there is a difference.
alpha = .05
$H_o$: There is no association between number of bedrooms and tax value.
$H_a$: There is an association between number of bedrooms and tax value.
Hypothesis 2 - I rejected the Null Hypothesis; there is a difference.
alpha = .05
$H_o$: There is no association between square foot of home and tax value.
$H_a$: There is an association between square foot of home and tax value.

Executive Summary - Conclusions & Next Steps

Recommendations & next steps:


Pipeline Stages Breakdown:

Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver

 Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
 Acquire data from the SQL Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
 Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
 Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
 Establish a baseline accuracy and document well.
 Train three different regression models.
 Evaluate models on train and validate datasets.
 Choose the model with that performs the best and evaluate that single model on the test dataset.
 Create csv file with the customer id, the probability of churn, and the model's predictions.
 Document conclusions, takeaways, and next steps in the Final Report Notebook.
Acquire
Store functions that are needed to acquire data that will be used for the Zillow Regression Project
The final function will return a pandas DataFrame
Prepare
Store functions needed to prepare the Zillow data
Import the prepare functions created by using .prepare.py
Explore
Answer key questions, my hypotheseses, and figure out the features that can be used in a regression model to best predict driver for churn
Model
Establish a baseline accuracy to determine if having a model is better than no model and train for at least 3 different models
Deliver
Deliver my findings in the presention.
Reproduce My Project
You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

 How to recreate:
 Download the aquire.py,
  prepare.py, 
  and final_report.ipynb files into your working directory
 Add your own env file to your directory. 
 (user, password, host)
 Run the final_report.ipynb notebook