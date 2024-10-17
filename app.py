from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calorie Burn Prediction System!!!"

@app.route('/about')
def about():
    return "This is about page"

if __name__ == '__main__':
    app.run(debug=True)
