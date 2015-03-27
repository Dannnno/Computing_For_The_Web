from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        "first_template.html", python_variable="")

app.run()
