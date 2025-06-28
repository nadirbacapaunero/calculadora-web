from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('calculadora'))

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacion = request.form['operacion']
        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero"
    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True) 