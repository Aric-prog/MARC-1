from flask import Blueprint, request
from flask import Flask

app = Flask(__name__)

bp = Blueprint("movement", __name__, url_prefix="/move")

# TODO : Expose movement routes here, integrate with bryan
orientationFunction = {
    'reverse' : 
}
@bp.route("/move")
def determineMovement():
    print(request.json()['orientation'])
    return ""

if(__name__ == '__main__'):
    app.register_blueprint(bp)
    app.run(port=8001, host='localhost')
