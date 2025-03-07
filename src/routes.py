from flask import Blueprint, jsonify, request
from src.services import calcular_rescisao

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "Servidor Flask rodando!"})

@bp.route('/calcular-rescisao', methods=['POST'])  # Apenas método POST
def calcular():
    try:
        dados = request.get_json()  # Obtém os dados enviados pelo usuário
        if not dados:
            return jsonify({"erro": "Nenhum dado foi enviado!"}), 400
        
        resultado = calcular_rescisao(dados)  # Chama a função para calcular a rescisão
        return jsonify(resultado), 200  # Retorna o JSON com o cálculo
    except Exception as e:
        return jsonify({"erro": str(e)}), 400  # Retorna erro se algo der errado
