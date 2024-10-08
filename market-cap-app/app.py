from flask import Flask, url_for, render_template, request
import numpy as np
import pickle  # Using pickle to load your model

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Load your trained model (make sure to specify the correct path)
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route("/")
def home():
    return render_template('index.html', current_page='home')

@app.route('/analysis')
def analysis():
    return render_template('about.html', current_page='analysis')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # Gather input from the form
        age = float(request.form['age'])
        state_code = float(request.form['state-code'])
        city_code = float(request.form['city-code'])
        duration = float(request.form['duration'])
        pdays = float(request.form['pdays'])
        postal_code = 0  # Assuming you are not using this value; adjust if needed
        employment_indicator = float(request.form['employment-indicator'])
        consumer_index = float(request.form['consumer-index'])
        economic_sentiment = float(request.form['economic-sentiment'])
        interest_rate_impact = float(request.form['interest-rate-impact'])
        job_blue_collar = float(request.form['job-blue-collar'])
        
        # Encode marital status
        marital_married = 1 if request.form['marital-status'] == 'married' else 0
        marital_single = 1 if request.form['marital-status'] == 'single' else 0
        
        # Encode education
        education_high_school = 1 if request.form['education'] == 'high-school' else 0
        education_university = 1 if request.form['education'] == 'university-degree' else 0
        
        housing_yes = int(request.form['housing-yes'])  # Assuming it's 'yes' or 'no'
        contact_telephone = 0  # Assuming you are not using this value; adjust if needed
        month_may = 1 if request.form['month'].lower() == 'may' else 0
        
        # Encode poutcome
        poutcome_nonexistent = 1 if request.form['poutcome'] == 'nonexistent' else 0
        poutcome_success = 1 if request.form['poutcome'] == 'success' else 0
        
        # Create the input array in the specified order
        input_data = np.array([
            age,
            state_code,
            city_code,
            duration,
            pdays,
            postal_code,
            employment_indicator,
            consumer_index,
            economic_sentiment,
            interest_rate_impact,
            job_blue_collar,
            marital_married,
            marital_single,
            education_high_school,
            education_university,
            housing_yes,
            contact_telephone,
            month_may,
            poutcome_nonexistent,
            poutcome_success
        ]).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(input_data)

        if prediction[0] == 1:  # Assuming 1 means "leave" and 0 means "stay"
            classification = "Churn"
            explanation = "The customer is likely to leave due to factors such as high duration, low economic sentiment, or other risk indicators."
        else:
            classification = "Retention"
            explanation = "The customer is likely to stay, indicating a positive customer experience and satisfaction."

        # Render the result
        return render_template('result.html', current_page='prediction', classification=classification, explanation=explanation)

    return render_template('prediction.html', current_page='prediction')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
