# ========================================
#  Funções Financeiras
# ========================================

def calcular_juros(valor, taxa, meses):
    """
    Calcula o valor final de um investimento com juros simples.

    Parâmetros:
        valor (float): Valor inicial aplicado.
        taxa (float): Taxa de juros mensal em porcentagem.
        meses (int): Quantidade de meses da aplicação.

    Retorna:
        float: Valor total após a aplicação dos juros simples.
    """
    return valor + (valor * (taxa / 100) * meses)
