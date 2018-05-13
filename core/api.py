from flask import Blueprint, request, jsonify

from core import compiler

bp = Blueprint('api', __name__)

@bp.route('/compile', methods=['POST'])
def compile():
    data = {}
    data['output'] = compiler.compile(request.form.get('input'))
    return jsonify(data), 200