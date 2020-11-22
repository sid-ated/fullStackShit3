import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle

'''
data_grid = pd.read_csv('training_data.csv')
cols_total = data_grid.columns
cols_total = cols_total[2:]
'''

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
    
 
@app.route('/get_symptoms', methods=['GET'])
def get_symptoms():       
	return "working"
	

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
