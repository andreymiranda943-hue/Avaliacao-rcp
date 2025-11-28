# ========================================
#  Arquivo Principal do Projeto
# ========================================

from conversores import conversor_temperatura
from financeiro import calcular_juros
from agenda import agenda
from dieta import calorias_por_refeicao
from musica import tempo_playlist, Playlist


def main():
    """
    Executa testes e demonstra o funcionamento
    de todas as funções do projeto.
    """
    print("\n=== TESTES DO SISTEMA ===\n")

    print("Temperatura convertida:", conversor_temperatura(30), "°F")

    print("Valor com juros:", calcular_juros(1000, 2, 6))

    print(agenda("João", "99999-9999"))

    print("Calorias:", calorias_por_refeicao("frango", 3))

    print("Tempo playlist:", tempo_playlist([3.5, 4, 60]))

    p = Playlist()
    p.adicionar(3.5)
    p.adicionar(4)
    p.adicionar(60)
    print("Playlist:", p)


if __name__ == "__main__":
    main()
