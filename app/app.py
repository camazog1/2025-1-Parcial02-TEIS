from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/factorial', methods=['POST'])
def factorial():
    num = int(request.form['num'])
    result = 1
    for i in range(2, num + 1):
        result *= i
    return f"El factorial de {num} es {result}"

if __name__ == '__main__':
    app.run()