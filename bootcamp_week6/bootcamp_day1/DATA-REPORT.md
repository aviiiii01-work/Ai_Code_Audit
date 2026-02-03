# EDA Report

## Shape and Columns
(383, 13)

['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']

## Missing Values
{'Loan_ID': 0, 'Gender': 0, 'Married': 0, 'Dependents': 0, 'Education': 0, 'Self_Employed': 0, 'ApplicantIncome': 0, 'CoapplicantIncome': 0, 'LoanAmount': 0, 'Loan_Amount_Term': 0, 'Credit_History': 0, 'Property_Area': 0, 'Loan_Status': 0}

## Target Distribution
{1: 313, 0: 70}

## Correlation Matrix
{'ApplicantIncome': {'ApplicantIncome': 1.0, 'CoapplicantIncome': -0.28360137834528615, 'LoanAmount': 0.4669335360543596, 'Loan_Amount_Term': nan, 'Credit_History': nan, 'Loan_Status': -0.05725231691710273}, 'CoapplicantIncome': {'ApplicantIncome': -0.28360137834528615, 'CoapplicantIncome': 1.0, 'LoanAmount': 0.2793165916533107, 'Loan_Amount_Term': nan, 'Credit_History': nan, 'Loan_Status': 0.10219436891962472}, 'LoanAmount': {'ApplicantIncome': 0.4669335360543596, 'CoapplicantIncome': 0.2793165916533107, 'LoanAmount': 1.0, 'Loan_Amount_Term': nan, 'Credit_History': nan, 'Loan_Status': -0.0316931301094801}, 'Loan_Amount_Term': {'ApplicantIncome': nan, 'CoapplicantIncome': nan, 'LoanAmount': nan, 'Loan_Amount_Term': nan, 'Credit_History': nan, 'Loan_Status': nan}, 'Credit_History': {'ApplicantIncome': nan, 'CoapplicantIncome': nan, 'LoanAmount': nan, 'Loan_Amount_Term': nan, 'Credit_History': nan, 'Loan_Status': nan}, 'Loan_Status': {'ApplicantIncome': -0.05725231691710273, 'CoapplicantIncome': 0.10219436891962472, 'LoanAmount': -0.0316931301094801, 'Loan_Amount_Term': nan, 'Credit_History': nan, 'Loan_Status': 1.0}}

