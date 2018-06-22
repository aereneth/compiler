from flask import Blueprint, request, jsonify

from core import compiler

bp = Blueprint('api', __name__)

@bp.route('/compile', methods=['POST'])
def compile():
    code = request.form.get('input')
    data = {}
    data['output'] = compiler.compile(code)

    return jsonify(data), 200