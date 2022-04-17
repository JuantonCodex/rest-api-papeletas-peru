import os
from flask import Flask
from functions import getPapeletas


app = Flask(__name__)
# print(os.environ['ANTICAPTCHA_TOKEN'])

@app.route("/papeletas/<string:_dni>", methods=["GET"])
def papeletas(_dni):
    papeletas = getPapeletas(_dni)
    return papeletas

if __name__ == "__main__":
    app.run()
