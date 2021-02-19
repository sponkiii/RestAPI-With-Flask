from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello boi World<h1>'


# another route
@app.route('/<name>')
def print_name(name):
    return 'Hi {}, musta ka jan pre? kaen muna.'.format(name)


# for auto restart every changes you make
if __name__ == '__main__':
    app.run(debug=True)