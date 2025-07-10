# 💳 Creditability Analysis Project

This project performs a comprehensive **exploratory data analysis (EDA)** and builds **machine learning models** on the German Credit dataset to assess applicants' **creditworthiness**. The goal is to understand patterns in applicant features and predict whether an individual is likely to repay credit obligations.

---

## 📊 Dataset Overview

- **Source**: `german.csv`
- **Entries**: 1000
- **Features**: 21
- **Target Variable**: `Creditability` (1 = creditworthy, 0 = not creditworthy)

The dataset includes both **numerical** and **categorical** features related to demographics, financial history, and credit details.

---

## 📁 Dataset Columns

```

🕒 Duration_of_Credit_monthly  
    → Number of months for which the credit is granted.

🏦 Account_Balance  
    → Status of the applicant's existing checking account (e.g., no account, negative balance).

💳 Payment_Status_of_Previous_Credit  
    → Payment behavior on previous credit (e.g., delays, complete payments).

🎯 Purpose  
    → Reason for the credit request (e.g., radio/TV, education, car, furniture).

💰 Credit_Amount  
    → Total amount of credit granted in Deutschmarks.

📈 Value_Savings_Stocks  
    → Value or status of the applicant’s savings or stocks (e.g., little, moderate, rich).

👷‍♂️ Length_of_current_employment  
    → Duration in years the applicant has been employed in the current job.

📉 Instalment_per_cent  
    → Percentage of income that will go toward installment repayment.

👫 Sex_Marital_Status  
    → Combined information about gender and marital status.

🤝 Guarantors  
    → Whether the applicant has a guarantor or co-signer.

🏠 Duration_in_Current_address  
    → Number of years the applicant has lived at their current address.

💎 Most_valuable_available_asset  
    → The most valuable asset the applicant owns (e.g., real estate, car, savings).

🎂 Age_years  
    → Age of the applicant in years.

💼 Concurrent_Credits  
    → Any other concurrent loans or credits the applicant is responsible for.

🏘️ Type_of_apartment  
    → The type of apartment where the applicant resides (e.g., own, rented, for free).

🏦 No_of_Credits_at_this_Bank  
    → Total number of credits the applicant has taken from this bank.

👨‍💼 Occupation  
    → Applicant’s occupation category based on skill or education level.

👨‍👩‍👧 No_of_dependents  
    → Number of people financially dependent on the applicant.

📞 Telephone  
    → Indicates whether the applicant owns a telephone.

🌍 Foreign_Worker  
    → Specifies if the applicant is a foreign worker in Germany.

✅ Creditability (Target Variable)  
    → Indicates whether the applicant is creditworthy (1) or not (0).


```

---

## 📂 Project Structure

```
creditability-analysis/
│
├── german.csv                # Dataset file
├── credit_analysis.ipynb     # Main notebook: EDA, modeling, and evaluation
├── credit_model.pkl          # Serialized model for prediction (via joblib)
├── requirements.txt          # Project dependencies
├── .gitignore
└── README.md
```

## 🔎 Exploratory Data Analysis (EDA)

 1. Summary statistics 

 2. Data types and null checks

 3. Unique values in each feature

 4. Visualizations :

    Histograms & density plots for numerical features (e.g., Age_years, Credit_Amount)

    Categorical value counts (e.g., Account_Balance, Purpose)

## 🧠 Feature Engineering

  Encoding categorical variables using One-Hot Encoding

  Handling class imbalance (Over Sampling)

  Normalizing / scaling numerical features

## 🤖 Model Building

Multiple machine learning models were trained to predict creditability:

  ✅ Logistic Regression
  ✅ SVC
  ✅ Naive Bayes
  ✅ Decision Tree
  ✅ K-nearest neighbour


## 📈 Model Evaluation
Evaluated using the following metrics:

Accuracy,   

Precision, 

Recall, 

F1-Score, 

ROC-AUC Curve.

## 🚀 Deployment
The best-performing model was saved using joblib into a .pkl file (credit_model.pkl), ready for use in downstream applications or APIs.

🧪 How to Run
Install dependencies:

bash
```
pip install -r requirements.txt
```
Download dataset:
Ensure german.csv is in the project directory.

Run the notebook:

bash
```
jupyter notebook credit_analysis.ipynb
```
⚠️ Note: You must be using Python 3.11.x or later for full compatibility.


## 👤 Author
Youssef Yacoub
Data Science Enthusiast | Machine Learning Engineer
