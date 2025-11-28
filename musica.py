# ========================================
#  Funções de Música e Playlist
# ========================================

def tempo_playlist(musicas):
    """
    Calcula o tempo total da playlist, valida os valores
    e retorna o resultado formatado em horas e minutos.

    Parâmetros:
        musicas (list): Lista contendo números (int ou float)
                        representando as durações das músicas.

    Retorna:
        str: Tempo total no formato 'Xh Ym' ou apenas 'Ym'.

    Levanta:
        ValueError: Caso algum valor não seja número ou seja negativo.
    """
    for t in musicas:
        if not isinstance(t, (int, float)) or t < 0:
            raise ValueError("Duração inválida.")

    total = sum(musicas)
    h, m = total // 60, total % 60
    return f"{int(h)}h {int(m)}min" if h else f"{int(m)}min"


class Playlist:
    """
    Classe que representa uma playlist musical contendo
    durações de músicas em minutos.

    Métodos:
        adicionar(tempo): Adiciona uma música com validação.
        total(): Retorna o tempo total da playlist formatado.
    """

    def __init__(self):
        """
        Inicializa a playlist com uma lista vazia.
        """
        self.musicas = []

    def adicionar(self, tempo):
        """
        Adiciona uma música à playlist após validar o tempo.

        Parâmetros:
            tempo (float ou int): Duração da música em minutos.

        Levanta:
            ValueError: Caso o tempo seja inválido.
        """
        if not isinstance(tempo, (int, float)) or tempo <= 0:
            raise ValueError("Duração inválida.")
        self.musicas.append(tempo)

    def total(self):
        """
        Retorna o tempo total da playlist formatado em horas e minutos.

        Retorna:
            str: Tempo formatado (Ex.: '1h 12min' ou '45min').
        """
        total = sum(self.musicas)
        h, m = total // 60, total % 60
        return f"{int(h)}h {int(m)}min" if h else f"{int(m)}min"

    def __str__(self):
        """
        Retorna uma representação amigável da playlist.

        Retorna:
            str: Ex.: '3 músicas — 1h 12min'
        """
        return f"{len(self.musicas)} músicas — {self.total()}"
