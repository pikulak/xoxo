from flask import Flask, render_template
from middlewares import GameGraphicsMiddleware
app = Flask(__name__)
app.secret_key = "some_secret"

@app.route('/', methods=["GET", "POST"])
def main():
	return render_template("main.html", title="Heheh")

app.run()