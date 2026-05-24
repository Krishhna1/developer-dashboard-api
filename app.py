from flask import Flask, render_template , request, redirect , session
import requests

from models import db, User , Task

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SECRET_KEY'] = 'krishna_secret'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():

    github_username = "octocat"

    github_url = f"https://api.github.com/users/{github_username}"

    response = requests.get(github_url)

    github_data = response.json()

    quote_response = requests.get("https://zenquotes.io/api/random")

    quote_data = quote_response.json()

    quote = quote_data[0]['q']

    return render_template(
        "index.html",
        github=github_data,
        quote=quote
    )


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")

        password = request.form.get("password")

        github_username = request.form.get("github")

        new_user = User(
            username=username,
            password=password,
            github_username=github_username
        )

        db.session.add(new_user)

        db.session.commit()

        return redirect("/dashboard")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")

        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:

            session["user"] = username

            return redirect("/dashboard")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    user_tasks = Task.query.filter_by(
        user=session["user"]
    ).all()
    
    current_user = User.query.filter_by(
        username=session["user"]
    ).first()
    github_url = f"https://api.github.com/users/{current_user.github_username}"
    response = requests.get(github_url)
    github_data = response.json()

    return render_template(
        "dashboard.html",
        user=session["user"],
        tasks=user_tasks,
        github=github_data
    )
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")

@app.route("/add-task", methods=["POST"])
def add_task():

    if "user" not in session:
        return redirect("/login")

    task_title = request.form.get("task")

    new_task = Task(
        title=task_title,
        user=session["user"]
    )

    db.session.add(new_task)

    db.session.commit()

    return redirect("/dashboard")

@app.route("/complete-task/<int:task_id>")
def complete_task(task_id):

    task = Task.query.get(task_id)

    task.completed = not task.completed

    db.session.commit()

    return redirect("/dashboard")

@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):

    task = Task.query.get(task_id)

    db.session.delete(task)

    db.session.commit()

    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)