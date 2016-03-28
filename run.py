from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/democontent', methods=['POST'])
def democontent():
    return render_template('democontent.html')


if __name__ == '__main__':
    app.run()
