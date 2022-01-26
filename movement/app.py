from flask import Blueprint, request, Response
from flask import Flask
# from cv2 import VideoCapture, imencode
# import base64
app = Flask(__name__)
import marc0brain

bp = Blueprint("movement", __name__, url_prefix="/")

# Camera stuff
# cam = VideoCapture(0)

# TODO : Expose movement routes here, integrate with bryan

movementFunctions = {
    'forward' : marc0brain.forward,
    'back' : marc0brain.reverse,
    'left' : marc0brain.turnLeft,
    'right' : marc0brain.turnRight,
}

@bp.route("/move", methods=['POST'])
def determineMovement():
    print('move to', request.form['orientation'])
    return Response(status=marc0brain.generalMove(movementFunctions[request.form['orientation']]))

@bp.route("/rotate", methods=['POST'])
def rotateCam():
    print('rotate to', request.form['rotate'])
    return Response(status=marc0brain.rotateCamera(request.form['rotate']))

# @bp.route("/image")
# def getImage():
#     # Setup camera
#     s, img = cam.read()
#     s, buf = imencode('.jpg', img)
#     jpg_as_text = base64.b64encode(buf)
    
#     # Send to main
#     return jpg_as_text
    
# This app should run on port 8001
app.register_blueprint(bp)
