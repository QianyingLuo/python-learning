from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/countries')
def getAllCountries():
    return "Hola País!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)