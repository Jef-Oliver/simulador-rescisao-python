from datetime import datetime  # Importamos datetime para manipular datas.

def calcular_rescisao(dados):
    """
    Função que calcula os valores devidos na rescisão do funcionário.
    Recebe um dicionário com os seguintes campos:
        - salario (float): salário do funcionário.
        - data_admissao (string YYYY-MM-DD): data em que foi contratado.
        - data_saida (string YYYY-MM-DD): data de saída da empresa.
        - motivo_saida (string): "pedido_demissao", "demissao_sem_justa_causa" ou "demissao_com_justa_causa".
        - saldo_ferias (int): quantidade de dias de férias vencidas.
        - decimo_terceiro (float): valor do 13º salário a receber.
        - aviso_previo (string): "trabalhado" ou "indenizado".
        - horas_pendentes (boolean): True se houver horas extras pendentes, False caso contrário.
        - adicionais (float, opcional): valores extras como insalubridade, periculosidade, etc.
    Retorna um dicionário com os cálculos realizados.
    """
    try:
        # Convertendo as datas informadas para o formato datetime
        data_admissao = datetime.strptime(dados["data_admissao"], "%Y-%m-%d")
        data_saida = datetime.strptime(dados["data_saida"], "%Y-%m-%d")

        # Pegamos o salário e garantimos que seja um número (float)
        salario = float(dados["salario"])

        # ✅ Cálculo do saldo de salário (dias trabalhados no mês da saída)
        dias_trabalhados = (data_saida - data_saida.replace(day=1)).days + 1  # Conta os dias do mês até a data de saída
        saldo_salario = (salario / 30) * dias_trabalhados  # Calculamos proporcionalmente

        # ✅ Cálculo do aviso prévio (se for indenizado, recebe um salário extra)
        aviso_previo = salario if dados["aviso_previo"] == "indenizado" else 0

        # ✅ Cálculo das férias vencidas + 1/3 constitucional
        ferias_vencidas = (salario / 12) * dados["saldo_ferias"]
        terco_constitucional = ferias_vencidas / 3  # 1/3 das férias vencidas

        # ✅ Cálculo do 13º salário proporcional
        meses_trabalhados = (data_saida.month - data_admissao.month) + (data_saida.year - data_admissao.year) * 12
        decimo_terceiro = (salario / 12) * meses_trabalhados

        # ✅ Cálculo da multa de 40% sobre FGTS (apenas se for demissão sem justa causa)
        multa_fgts = salario * 0.40 if dados["motivo_saida"] == "demissao_sem_justa_causa" else 0

        # ✅ Verificamos se há adicionais como insalubridade, periculosidade, etc.
        adicionais = float(dados.get("adicionais", 0.0))  # Se não for informado, assume 0.

        # ✅ Calculamos o total a receber
        total_rescisao = saldo_salario + aviso_previo + ferias_vencidas + terco_constitucional + decimo_terceiro + multa_fgts + adicionais

        # ✅ Retornamos os valores arredondados para duas casas decimais
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

    except Exception as e:
        return {"erro": f"Erro no cálculo: {str(e)}"}
