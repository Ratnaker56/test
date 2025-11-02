from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! This pipeline works!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
