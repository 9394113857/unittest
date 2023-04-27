# app.py

from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)
calculator = Calculator()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operation = request.form['operation']
    if operation == 'addition':
        result = calculator.add(num1, num2)
    elif operation == 'subtraction':
        result = calculator.subtract(num1, num2)
    elif operation == 'multiplication':
        result = calculator.multiply(num1, num2)
    elif operation == 'division':
        try:
            result = calculator.divide(num1, num2)
        except ValueError as e:
            result = str(e)
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
