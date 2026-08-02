from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Student table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    student_class = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        student = Student.query.filter_by(
            email=email,
            password=password
        ).first()

        if student:
            return redirect(url_for("dashboard"))
        else:
            return "Invalid email or password!"

    return render_template("login.html")
@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]
        new_password = request.form["new_password"]
        confirm_password = request.form["confirm_password"]

        # Check if both passwords match
        if new_password != confirm_password:
            return "Passwords do not match!"

        student = Student.query.filter_by(email=email).first()

        if student:

            student.password = new_password
            db.session.commit()

            return redirect(url_for("login"))

        else:

            return "Email not found!"

    return render_template("forgot_password.html")
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        student_class = request.form["student_class"]
        password = request.form["password"]

        student = Student(
            fullname=fullname,
            email=email,
            student_class=student_class,
            password=password
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Create the database
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)