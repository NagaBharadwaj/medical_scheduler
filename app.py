from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduler.db'
db = SQLAlchemy(app)

# Import models after initializing db to avoid circular import
from models import User, Appointment, Patient

@app.route('/')
def index():
    return render_template('index.html')

@app.route ('/login', methods=['GET', 'POST'] )
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    appointments = Appointment.query.all()
    return render_template('dashboard.html', appointments=appointments)

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        date = request.form['date']
        time = request.form['time']
        new_appointment = Appointment(patient_id=patient_id, date=date, time=time)
        db.session.add(new_appointment)
        db.session.commit()
        return redirect(url_for('dashboard'))
    patients = Patient.query.all()
    return render_template('appointment.html', patients=patients)

@app.route('/patient', methods=['GET', 'POST'])
def patient():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        contact = request.form['contact']
        new_patient = Patient(name=name, age=age, contact=contact)
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('patient.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
