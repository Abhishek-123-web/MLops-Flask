from flask import Flask, request
import pickle

#app

app = Flask(__name__)

print(__name__)

# Load The Model

with open('classifier.pkl', 'rb') as f:
    clf = pickle.load(f)

# Base URL

@app.route('/ping', methods = ['GET'])
def ping():
    return 'Pinging Model Application!'

# http://127.0.0.1:5000/ping

@app.route('/predict', methods = ['POST'])

def predict():
    """
    Returns the loan approved or  not
    """
    loan_req = request.get_json()

    if loan_req['gender'] == 'Male':
        gender = 0
    else:
        gender = 1

    if loan_req['married'] == 'unmarried':
        marital_status = 0
    else:
        marital_status = 1

    if loan_req['credit_history'] == 'Unclear Debts':
        credit_history = 0
    else:
        credit_history = 1

    applicant_income = loan_req['applicant_income']
    loan_amount = loan_req['loan_amount']

    result = clf.predict([[gender, marital_status, credit_history, applicant_income, loan_amount]])

    if result == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'

    return {'loan_approval_status': pred}       
