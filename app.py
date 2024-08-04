from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load The Model
with open('classifier.pkl', 'rb') as f:
    clf = pickle.load(f)

# Base URL
@app.route('/ping', methods=['GET'])
def ping():
    return 'Pinging Model Application!'

# Prediction Endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Print the incoming request data for debugging
        print(request.data)

        # Get JSON data from request
        loan_req = request.get_json()

        # Print parsed JSON data for debugging
        print(loan_req)

        # Parse and validate input data
        gender = 0 if loan_req.get('gender') == 'Male' else 1
        marital_status = 0 if loan_req.get('married') == 'unmarried' else 1
        credit_history = 0 if loan_req.get('credit_history') == 'Unclear Debts' else 1
        applicant_income = float(loan_req.get('applicant_income', 0))
        loan_amount = float(loan_req.get('loan_amount', 0))

        # Prediction
        result = clf.predict([[gender, marital_status, credit_history, applicant_income, loan_amount]])

        # Interpret result
        pred = 'Rejected' if result[0] == 0 else 'Approved'

        return jsonify({'loan_approval_status': pred})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
