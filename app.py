from flask import Flask
from functions import getPapeletas


app = Flask(__name__)


@app.route("/papeletas/<string:_dni>", methods=["GET"])
def papeletas(_dni):
    papeletas = getPapeletas(_dni)
    return papeletas

app.run(debug=False, port=5000)
