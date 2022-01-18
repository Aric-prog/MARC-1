from flask import Blueprint

bp = Blueprint("index", __name__, url_prefix="/")

# TODO : Expose movement routes here, 
@bp.route("/")
def index():
    return ""

