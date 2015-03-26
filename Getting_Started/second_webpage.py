from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
<!DOCTYPE HTML>

<html>

	<head>
		<title>My First Webpage!</title>
	</head>

	<body>
		<h1>Hello world!</h1>
	</body>

</html>
"""

app.run()
