import os
import joblib
import pickle

from flask import Flask, request, render_template

def configure_routes(app):

    # this_dir = os.path.dirname(__file__)
    # model_path = os.path.join(this_dir, "model.pkl")
    # model = joblib.load("model.pkl")
    model = pickle.load(open('model.pkl', 'rb'))

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/predict', methods=['POST'])
    def predict():

        def processText(features):
            text = ''
            for feature in features:
                text += feature + ' '
            return [text]

        features = [x for x in request.form.values()]
        text = processText(features)
        prediction = model.predict(text)
        prediction_prob = model.predict_proba(text)

        return_text = ''
        if prediction[0] == 0:
            return_text = f'This job posting is predicted to be real. The predicted probabilities are {prediction_prob}, where the first number is the likelihood of the job posting to be real and the second is the likelihood of the job posting to be fraudulent.'
        else:
            return_text = f'This job posting is predicted to be fraudulent. The predicted probabilities are {prediction_prob}, where the first number is the likelihood of the job posting to be real and the second is the likelihood of the job posting to be fraudulent.'



        print(prediction)
        return render_template('index.html', prediction_text=return_text)
