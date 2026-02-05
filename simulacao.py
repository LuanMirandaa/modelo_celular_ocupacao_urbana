import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.colors import ListedColormap

# -----------------------------
# CONFIGURAÇÕES DA SIMULAÇÃO
# -----------------------------
TAMANHO_MAPA = 30
PROPORCAO_PESSOAS = 0.3
TEMPO_FRAME_MS = 300
TOTAL_FRAMES = 100

# Obstáculos fixos (ex: árvores, bancos, postes)
POSICOES_BLOQUEADAS = [(5, 5), (10, 15), (20, 20), (15, 8)]

# Estados possíveis da célula
VAZIO = 0
PESSOA = 1
OBSTACULO = 2

# -----------------------------
# INICIALIZAÇÃO DO MAPA
# -----------------------------
mapa = np.random.choice(
    [VAZIO, PESSOA],
    size=(TAMANHO_MAPA, TAMANHO_MAPA),
    p=[1 - PROPORCAO_PESSOAS, PROPORCAO_PESSOAS]
)

for linha, coluna in POSICOES_BLOQUEADAS:
    mapa[linha, coluna] = OBSTACULO

# Cores do mapa
paleta_cores = ListedColormap(['white', 'red', 'green'])

# -----------------------------
# FUNÇÃO DE EVOLUÇÃO DO SISTEMA
# -----------------------------
def evoluir_sistema(frame, imagem, estado_atual):
    proximo_estado = estado_atual.copy()

    for i in range(TAMANHO_MAPA):
        for j in range(TAMANHO_MAPA):

            # Obstáculos não participam da dinâmica
            if estado_atual[i, j] == OBSTACULO:
                continue

            # Conta vizinhos do tipo pessoa
            vizinhos = np.sum(
                estado_atual[
                    max(i - 1, 0):min(i + 2, TAMANHO_MAPA),
                    max(j - 1, 0):min(j + 2, TAMANHO_MAPA)
                ] == PESSOA
            )

            if estado_atual[i, j] == PESSOA:
                vizinhos -= 1  # remove a própria célula da contagem

                if vizinhos < 2 or vizinhos > 3:
                    proximo_estado[i, j] = VAZIO

            else:
                if vizinhos == 3:
                    proximo_estado[i, j] = PESSOA

    imagem.set_data(proximo_estado)
    estado_atual[:] = proximo_estado[:]
    return imagem

# -----------------------------
# VISUALIZAÇÃO E ANIMAÇÃO
# -----------------------------
figura, eixo = plt.subplots()
imagem = eixo.imshow(mapa, interpolation='nearest', cmap=paleta_cores)

eixo.set_title("Simulação de ocupação em espaço público com obstáculos")
eixo.axis("off")

animacao = anim.FuncAnimation(
    figura,
    evoluir_sistema,
    fargs=(imagem, mapa),
    frames=TOTAL_FRAMES,
    interval=TEMPO_FRAME_MS,
    save_count=50
)

# Salva o resultado
animacao.save(
    "simulacao_ocupacao_praca.gif",
    writer="pillow"
)

print("GIF gerado com sucesso: simulacao_ocupacao_praca.gif")
plt.show()
