from flask import Blueprint, jsonify, request, render_template
from src.services import calcular_rescisao

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')  # Garante que o Flask renderize o HTML correto

@bp.route('/calcular-rescisao', methods=['POST'])
def calcular():
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({"erro": "Nenhum dado foi enviado!"}), 400
        
        resultado = calcular_rescisao(dados)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400