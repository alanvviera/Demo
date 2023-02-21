from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "HELLO"


@app.route("/bye")
def adios():
    return "bayy"

# para correr
# flask --app -nombreapp- run
# \venv/Scripts/activate.bats
