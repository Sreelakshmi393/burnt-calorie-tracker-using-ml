from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gym_management.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Member(db.Model):
    uname = db.Column(db.String(50), primary_key=True)  # Primary Key
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)  # Height in cm
    weight = db.Column(db.Integer, nullable=False)  # Weight in kg
    kind = db.Column(db.String(20), nullable=False)  # Could represent membership type or other info


# Define the Workouts model
class Workout(db.Model):
    workout_id = db.Column(db.Integer, primary_key=True)  # Primary Key
    uname = db.Column(db.String(50), db.ForeignKey('member.uname'), nullable=False)  # Foreign Key referencing Members
    date = db.Column(db.Date, nullable=False, default=date.today)  # Date of the workout
    calorie = db.Column(db.Integer, nullable=False)  # Calories burnt


class Remark(db.Model):
    remark_id = db.Column(db.Integer, primary_key=True)  # Primary Key
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.workout_id'), nullable=False)  # Foreign Key referencing Workouts
    uname = db.Column(db.String(50), db.ForeignKey('member.uname'), nullable=False)  # Foreign Key referencing Members
    feedback = db.Column(db.Text, nullable=False)  # Feedback text

# Create the database tables
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        username = request.form['username']
        password = request.form['password']
        # Authenticate user logic
        return redirect(url_for('home'))
    return render_template('login.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        # Add the user to the database (not implemented)
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
