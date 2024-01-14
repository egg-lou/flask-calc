from flask import Flask, render_template, request
from Helpers.ohms_calculator import OhmsCalculator

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    print(request.method)
    if request.method == 'GET':
        return render_template('main.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    print(request.method)
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

            calculator = OhmsCalculator(voltage=voltage, current=current, resistance=resistance, power=power)

            result_voltage = calculator.calculate_voltage()
            result_current = calculator.calculate_current()
            result_resistance = calculator.calculate_resistance()
            result_power = calculator.calculate_power()

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
            return f"Invalid input: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
