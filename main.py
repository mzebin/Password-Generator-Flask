from flask import (
    Flask,
    render_template,
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/generate/", methods=["GET", "POST"])
def generate():
    return "Generate"


@app.route("/copy/")
def copy():
    return "Copy"


if __name__ == "__main__":
    app.run(debug=True)
