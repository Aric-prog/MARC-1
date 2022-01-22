from flask import Blueprint, request
from flask import Flask
app = Flask(__name__)
# import marc0brain

bp = Blueprint("movement", __name__, url_prefix="/")

# TODO : Expose movement routes here, integrate with bryan

# movementFunctions = {
#     'forward' : marc0brain.forward,
#     'back' : marc0brain.reverse,
#     'left' : marc0brain.turnLeft,
#     'right' : marc0brain.turnRight,
# }

@bp.route("/move", methods=['POST'])
def determineMovement():
    print('move to', request.form['orientation'])
    # return marc0brain.generalMove(movementFunctions[request.form['orientation']])
    return 'succ'
    
app.register_blueprint(bp)
app.run(port=8001, host='localhost')
