# ========================================
#  Controle de Calorias
# ========================================

def calorias_por_refeicao(prato, quantidade):
    """
    Calcula o total de calorias baseado no prato e na quantidade de porções.

    Parâmetros:
        prato (str): Nome do prato.
        quantidade (int): Número de porções consumidas.

    Retorna:
        int ou str: Calorias totais ou mensagem de erro caso
                    o prato não exista na tabela.
    """
    tabela = {
        "arroz": 130,
        "feijao": 110,
        "frango": 160,
        "cuscuz": 120,
        "ovo": 70,
        "batata doce": 90,
    }

    prato = prato.lower()

    if prato not in tabela:
        return "Prato não encontrado."

    return tabela[prato] * quantidade
