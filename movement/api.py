from flask import Blueprint
from flask import Flask

app = Flask(__name__)

bp = Blueprint("movement", __name__, url_prefix="/move")

# TODO : Expose movement routes here, integrate with bryan
@bp.route("/")
def index():
    return ""

if(__name__ == '__main__'):
    app.register_blueprint(bp)
    app.run(port=8001, host='localhost')
