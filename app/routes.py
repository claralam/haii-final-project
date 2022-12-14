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
        print(text)
        prediction = model.predict(text)
        prediction_prob = model.predict_proba(text)

        print(prediction)
        return render_template('index.html', prediction_text=f'{prediction} and {prediction_prob}')
