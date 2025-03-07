from datetime import datetime  # Importamos datetime para manipular datas.

def calcular_rescisao(dados):
    try:
        # 1. Validar campos obrigatórios
        campos_obrigatorios = [
            "salario", "data_admissao", "data_saida", "motivo_saida",
            "saldo_ferias", "decimo_terceiro", "aviso_previo", "horas_pendentes"
        ]
        
        for campo in campos_obrigatorios:
            if campo not in dados:
                return {"erro": f"O campo '{campo}' é obrigatório"}
            
        # 2. Validar tipos de dados
        if not isinstance(dados["salario"], (int, float)) or dados["salario"] <= 0:
            return {"erro": "O salário deve ser um número positivo."}
        
        if not isinstance(dados["saldo_ferias"], int) or dados["saldo_ferias"] < 0:
            return {"erro": "O saldo de férias deve ser um número inteiro positivo."}

        if not isinstance(dados["decimo_terceiro"], (int, float)) or dados["decimo_terceiro"] < 0:
            return {"erro": "O 13º salário deve ser um número positivo."}

        if not isinstance(dados["horas_pendentes"], bool):
            return {"erro": "O campo 'horas_pendentes' deve ser True ou False."}
        
         # ✅ 3. Validar Formato das Datas
        try:
            data_admissao = datetime.strptime(dados["data_admissao"], "%Y-%m-%d")
            data_saida = datetime.strptime(dados["data_saida"], "%Y-%m-%d")
        except ValueError:
            return {"erro": "As datas devem estar no formato YYYY-MM-DD."}

        # ✅ 4. Garantir que a Data de Saída não seja Antes da Admissão
        if data_saida < data_admissao:
            return {"erro": "A data de saída não pode ser anterior à data de admissão."}

        # ✅ 5. Validar Motivo da Saída
        motivos_validos = ["pedido_demissao", "demissao_sem_justa_causa", "demissao_com_justa_causa"]
        if dados["motivo_saida"] not in motivos_validos:
            return {"erro": "O motivo de saída deve ser um dos seguintes: pedido_demissao, demissao_sem_justa_causa, demissao_com_justa_causa."}

        # ✅ 6. Validar Aviso Prévio
        if dados["aviso_previo"] not in ["trabalhado", "indenizado"]:
            return {"erro": "O aviso prévio deve ser 'trabalhado' ou 'indenizado'."}

        # ✅ 7. Validar Adicionais (Opcional)
        adicionais = float(dados.get("adicionais", 0.0))
        if adicionais < 0:
            return {"erro": "Os adicionais não podem ser negativos."}

        # ✅ Se todas as validações passaram, segue para o cálculo
        return calcular_rescisao_logica(dados, data_admissao, data_saida, adicionais)

    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}

def calcular_rescisao_logica(dados, data_admissao, data_saida, adicionais):
    """
    Lógica de cálculo da rescisão, separada para manter o código organizado.
    """

    salario = float(dados["salario"])
    dias_trabalhados = (data_saida - data_saida.replace(day=1)).days + 1
    saldo_salario = (salario / 30) * dias_trabalhados

    aviso_previo = salario if dados["aviso_previo"] == "indenizado" else 0

    ferias_vencidas = (salario / 12) * dados["saldo_ferias"]
    terco_constitucional = ferias_vencidas / 3

    meses_trabalhados = (data_saida.month - data_admissao.month) + (data_saida.year - data_admissao.year) * 12
    decimo_terceiro = (salario / 12) * meses_trabalhados

    multa_fgts = salario * 0.40 if dados["motivo_saida"] == "demissao_sem_justa_causa" else 0

    total_rescisao = saldo_salario + aviso_previo + ferias_vencidas + terco_constitucional + decimo_terceiro + multa_fgts + adicionais

    return {
        "saldo_salario": round(saldo_salario, 2),
        "aviso_previo": round(aviso_previo, 2),
        "ferias_vencidas": round(ferias_vencidas, 2),
        "terco_constitucional": round(terco_constitucional, 2),
        "decimo_terceiro": round(decimo_terceiro, 2),
        "multa_fgts": round(multa_fgts, 2),
        "adicionais": round(adicionais, 2),
        "total_rescisao": round(total_rescisao, 2)
    }