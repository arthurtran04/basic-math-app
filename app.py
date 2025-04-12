'''
This is a simple Flask application that performs basic arithmetic operations.
It includes routes for addition, subtraction, multiplication, division, and modulus.
The application uses a custom module 'Maths' to perform the calculations.
The application is structured to handle requests for each operation and return the result.
The application is designed to be run in debug mode for development purposes.
'''
from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication, division, modulus

app = Flask(__name__)

@app.route("/sum")
def sum_route():
    '''
    This route handles the addition of two numbers.
    It retrieves the numbers from the request arguments,
    performs the addition using the summation function,
    and returns the result as a string.
    '''
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1, num2)
    return str(result)

@app.route("/sub")
def sub_route():
    '''
    This route handles the subtraction of two numbers.
    It retrieves the numbers from the request arguments,
    performs the subtraction using the subtraction function,
    and returns the result as a string.
    '''
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    return str(result)

@app.route("/mul")
def mul_route():
    '''
    This route handles the multiplication of two numbers.
    It retrieves the numbers from the request arguments,
    performs the multiplication using the multiplication function,
    and returns the result as a string.
    '''
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1, num2)
    return str(result)

@app.route("/div")
def div_route():
    '''
    This route handles the division of two numbers.
    It retrieves the numbers from the request arguments,
    performs the division using the division function,
    and returns the result as a string.
    '''
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = division(num1, num2)
    return str(result)

@app.route("/mod")
def mod_route():
    '''
    This route handles the modulus of two numbers.
    It retrieves the numbers from the request arguments,
    performs the modulus using the modulus function,
    and returns the result as a string.
    '''
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = modulus(num1, num2)
    return str(result)

@app.route("/")
def render_index_page():
    '''
    This route renders the index page of the application.
    It serves the main HTML template for the application.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
