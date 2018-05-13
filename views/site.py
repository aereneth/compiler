from flask import Blueprint, render_template

from core import compiler

bp = Blueprint('site', __name__)

@bp.route('/')
def index():
    return render_template('index.html')