from flask import Flask, render_template, request
from Helpers.ohms_calculator import OhmsCalculator

# Initialize Flask application
app = Flask(__name__, template_folder='templates')

# Route for the home page
@app.route('/', methods=['GET'])
def index():
    # Print the request method for debugging purposes
    print(request.method)
    # If the request method is GET, render the main page
    if request.method == 'GET':
        return render_template('main.html')

# Route for the calculation page
@app.route('/calculate', methods=['POST'])
def calculate():
    # Print the request method for debugging purposes
    print(request.method)
    # If the request method is POST, perform the calculation
    if request.method == 'POST':
        try:
            # Initialize values to None
            voltage = current = resistance = power = None

            # Attempt to convert form values to float, if present and not empty
            if 'voltage' in request.form and request.form['voltage'].strip():
                voltage = float(request.form['voltage'])
            if 'current' in request.form and request.form['current'].strip():
                current = float(request.form['current'])
            if 'resistance' in request.form and request.form['resistance'].strip():
                resistance = float(request.form['resistance'])
            if 'power' in request.form and request.form['power'].strip():
                power = float(request.form['power'])

            # Initialize OhmsCalculator with the provided values
            calculator = OhmsCalculator(voltage=voltage, current=current, resistance=resistance, power=power)

            # Calculate the missing values
            result_voltage = calculator.calculate_voltage()
            result_current = calculator.calculate_current()
            result_resistance = calculator.calculate_resistance()
            result_power = calculator.calculate_power()

            # Render the main page with the results
            return render_template('main.html',
                                   result_voltage=result_voltage,
                                   result_current=result_current,
                                   result_resistance=result_resistance,
                                   result_power=result_power,
                                   voltage=voltage,
                                   current=current,
                                   resistance=resistance,
                                   power=power)

        except ValueError as e:
            # If an error occurred during the conversion of the form values, return an error message
            return f"Invalid input: {str(e)}"

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)