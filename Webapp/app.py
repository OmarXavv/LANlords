from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/dashboard')
def dashboard():
    timenow = datetime.now().strftime("%I:%M:%S %p")
    temperature = "24°C"
    lights_active = "12/20"
    energy_usage = "75 kWh"
    return render_template('Dashboard.html', time=timenow, temperature=temperature, lights_active=lights_active, energy_usage=energy_usage)

@app.route('/entertainment')
def entertainment():
    current_time = datetime.now().strftime('%H:%M:%S') 
    return render_template('entertainment.html', time=current_time)

@app.route('/trash')
def trash():
    current_time = datetime.now().strftime('%H:%M:%S') 
    return render_template('trash.html', time=current_time)



if __name__ == "__main__":
    app.run(debug=True)
