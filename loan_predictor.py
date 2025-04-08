import joblib
import pandas as pd
def predict_loan_eligibility(
    Age_years, Account_Balance, Credit_Amount, Duration_of_Credit_monthly,
    Instalment_per_cent, Guarantors = int(1), No_of_dependents = int(1),
    Payment_Status_of_Previous_Credit = int(3), Purpose = int(2), Value_Savings_Stocks = int(1),
    Length_of_current_employment = int(3), Sex_Marital_Status = int(3), Duration_in_Current_address = int(3),
    Most_valuable_available_asset = int(2), Concurrent_Credits = int(1), Type_of_apartment = int(2),
    No_of_Credits_at_this_Bank = int(1), Occupation = int(3), Telephone = int(2), Foreign_Worker = int(1)
):
    # Create a DataFrame from user inputs
    user_data = pd.DataFrame({
        'Duration_of_Credit_monthly': [Duration_of_Credit_monthly],
        'Account_Balance': [Account_Balance],
        'Payment_Status_of_Previous_Credit': [Payment_Status_of_Previous_Credit],
        'Purpose': [Purpose],
        'Credit_Amount': [Credit_Amount],
        'Value_Savings_Stocks': [Value_Savings_Stocks],
        'Length_of_current_employment': [Length_of_current_employment],
        'Instalment_per_cent': [Instalment_per_cent],
        'Sex_Marital_Status': [Sex_Marital_Status],
        'Guarantors': [Guarantors],
        'Duration_in_Current_address': [Duration_in_Current_address],
        'Most_valuable_available_asset': [Most_valuable_available_asset],
        'Age_years': [Age_years],
        'Concurrent_Credits': [Concurrent_Credits],
        'Type_of_apartment': [Type_of_apartment],
        'No_of_Credits_at_this_Bank': [No_of_Credits_at_this_Bank],
        'Occupation': [Occupation],
        'No_of_dependents': [No_of_dependents],
        'Telephone': [Telephone],
        'Foreign_Worker': [Foreign_Worker]
    })

    # Make prediction
    prediction = model.predict(user_data)
    prediction_proba = model.predict_proba(user_data)

    # Return result
    if prediction[0] == 1:
        return "Eligible for loan", prediction_proba[0][1]
    else:
        return "Not eligible for loan", prediction_proba[0][0]

# Load the trained model
model = joblib.load('Creditability.pkl')

# Get user inputs
Age_years = int(input("Enter your Age_years: "))
Account_Balance = int(input("Enter your Account_Balance: "
                            "\t \nNo Account: 1"
                            "\t \naccount with 0 balance: 2"
                            "\t \naccount with some balance: 3 \t"))
Credit_Amount = int(input("Enter the loan  you demand: "))
Duration_of_Credit_monthly = int(input("Enter your Duration of Credit return in no. of months: "))
Guarantors = int(input("Enter no. of Guarantors: "
                       "\t \nmin. = 1"
                       "\t \nmax. = 3\t"))
Length_of_current_employment = int(input("state your employment length in years: \n"
                    "\t \n0 - 1: 1"
                    "\t \n1 - 3: 2"
                    "\t \n4 - 7: 3"
                    "\t \n+7: 4 \t"))
Sex_Marital_Status = int(input("state your marital status: \n"
                    "\t \nsingle man: 1"
                    "\t \nmarried man: 2"
                    "\t \nfemale: 3  \t"))


result, probability = predict_loan_eligibility(
    Age_years, Account_Balance, Credit_Amount, Duration_of_Credit_monthly, Guarantors,
    Length_of_current_employment, Sex_Marital_Status)

print(f"Result: {result}, Probability: {probability:.2f}")

# add guidelines for encoded values in data set
