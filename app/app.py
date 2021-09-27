import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load(open('pipple_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Flower Class should \
     be {}'.format(output))


@app.route('/results', methods=['POST'])
def results():

    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    prediction = model.predict(df)

    output = prediction[0]
    return jsonify(output.tolist())


if __name__ == "__main__":
    app.run(host='0.0.0.0')
