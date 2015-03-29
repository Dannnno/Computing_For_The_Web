from flask import Flask, render_template

app = Flask(__name__)


phone_numbers = {'Dan': '123-456-7890',
                 'John': '098-765-431',
                 'Mary': '783-123-3489'
                 }

@app.route('/')
def index():
    return render_template('iteration.html', numbers=phone_numbers)

app.run()
