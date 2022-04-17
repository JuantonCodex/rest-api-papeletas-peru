from flask import Flask
from functions import getPapeletas


app = Flask(__name__)


@app.route("/papeletas/<string:_dni>", methods=["GET"])
def papeletas(_dni):
    papeletas = getPapeletas(_dni)
    return papeletas

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
