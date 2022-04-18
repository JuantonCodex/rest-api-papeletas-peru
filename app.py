import os
from flask import Flask
from flask_cors import CORS, cross_origin
from functions import getPapeletas


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/papeletas/<string:_dni>", methods=["GET"])
@cross_origin()
def papeletas(_dni):
    papeletas = getPapeletas(_dni)
    return papeletas

if __name__ == "__main__":
    app.run(debug=True)
