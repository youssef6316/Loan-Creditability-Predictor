# Creditability Analysis Project
**Overview**
This Jupyter Notebook contains an exploratory data analysis (EDA) of the German credit dataset. The project aims to analyze various features related to credit applicants and assess their creditworthiness. The dataset includes 21 features and 1000 entries, with the target variable being "Creditability," which indicates whether an applicant is creditworthy (1) or not (0).

**Dataset Description**
The dataset (german.csv) contains the following columns:

Duration_of_Credit_monthly

Account_Balance

Payment_Status_of_Previous_Credit

Purpose

Credit_Amount

Value_Savings_Stocks

Length_of_current_employment

Instalment_per_cent

Sex_Marital_Status

Guarantors

Duration_in_Current_address

Most_valuable_available_asset

Age_years

Concurrent_Credits

Type_of_apartment

No_of_Credits_at_this_Bank

Occupation

No_of_dependents

Telephone

Creditability (Target Variable)

Foreign_Worker

Project Structure
**Data Loading:** The dataset is loaded into a pandas DataFrame for analysis.

**Exploratory Data Analysis (EDA):**

Basic statistics of each column (df.describe()).

Data content and types (df.info()).

Unique values in each column (df.nunique()).

Extraction of unique values for categorical and numerical columns.

Visualization of numerical columns (Age_years, Duration_of_Credit_monthly, Credit_Amount) using histograms and density plots.

Key Findings
The dataset contains a mix of numerical and categorical features.

The target variable "Creditability" is binary, with 70% of applicants classified as creditworthy.

Numerical features such as Credit_Amount and Age_years show varied distributions, which are visualized using histograms.

Categorical features like Account_Balance and Purpose have distinct unique values, indicating potential patterns in creditworthiness.

**Feature Engineering:** Transform categorical variables into numerical representations (e.g., one-hot encoding).

**Model Building:** Train machine learning models (e.g., logistic regression, Random forest) to predict creditability.

**Model Evaluation:** Assess model performance using metrics like accuracy, precision, recall, and ROC-AUC.

Deployment: by the help of joblib library and creation of a .pkl file for predicting

How to Run
Ensure all dependencies are installed (pip install pandas numpy seaborn matplotlib).

Download the dataset (german.csv) and place it in the same directory as the notebook.

Open the Jupyter Notebook and run all cells to reproduce the analysis.

Author
Youssef Yacoub
