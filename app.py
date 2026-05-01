print("App starting...")
from flask import Flask, render_template, request
import pickle, pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = pd.DataFrame([{
        'gender': int(request.form['gender']),
        'race/ethnicity': int(request.form['race']),
        'parental level of education': int(request.form['parent_edu']),
        'lunch': int(request.form['lunch']),
        'test preparation course': int(request.form['test_prep']),
        'reading score': int(request.form['reading_score']),
        'writing score': int(request.form['writing_score'])
    }])
    result = model.predict(data)[0]
    return render_template('index.html', prediction=round(result, 1))

if __name__ == '__main__':
    app.run(debug=True)