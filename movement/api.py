from flask import Blueprint, request
from flask import Flask
app = Flask(__name__)
import marc0brain

bp = Blueprint("movement", __name__, url_prefix="/move")

# TODO : Expose movement routes here, integrate with bryan
# orientationFunction = {
#     'reverse' : youthing.moveBack 
# }

movementFunctions = {
    'forward' : marc0brain.forward,
    'back' : marc0brain.reverse,
    'left' : marc0brain.turnLeft,
    'right' : marc0brain.turnRight,
}

@bp.route("/move")
def determineMovement():
    return marc0brain.generalMove(movementFunctions[request.json()['orientation']])
    
if(__name__ == '__main__'):
    app.register_blueprint(bp)
    app.run(port=8001, host='localhost')
