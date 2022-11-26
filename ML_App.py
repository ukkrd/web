import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Trained_Model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('LnB.html')

@app.route('/prediction',methods=['POST'])
def prediction():
    int_f = [int(x) for x in request.form.values()]
    final_f = [np.array(int_f)]
    p = model.predict(final_f)
    op = round(p[0], 2)
    return render_template('LnB.html', prediction_text='Expected Salary should be INR {}'.format(op))

@app.route('/prediction_api',methods=['POST'])
def prediction_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
