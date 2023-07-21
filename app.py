# Import the Flask class from the flask module
from flask import Flask, render_template, request
from joblib import load
import pandas as pd

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its corresponding view function
@app.route('/')
def enterdata():
    return render_template('index.html')

@app.route('/predictagain')
def predictagain():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Retrieve form values
        weight = int(request.form.get('weight'))
        vlength = float(request.form.get('vlength'))
        dlength = float(request.form.get('dlength'))
        clength = float(request.form.get('clength'))
        height = float(request.form.get('height'))
        width = float(request.form.get('width'))

        data = {
            'Weight': weight,
            'Length1': vlength,
            'Length2': dlength,
            'Length3': clength,
            'Height': height,
            'Width': width
        }

        # Create the DataFrame with a single row and set the index to 0
        x_input = pd.DataFrame(data, index=[0])

        model = load('svm_model.pkl')
        prediction = model.predict(x_input)

        fish_names = ['Bream', 'Roach', 'Whitefish', 'Parkki', 'Perch', 'Pike', 'Smelt']
        fish_name_predicted = fish_names[prediction[0]]  # prediction is an array, so access the first element

        return render_template('main.html', result=fish_name_predicted)


# Run the application if this script is executed
if __name__ == '__main__':
    app.run()
