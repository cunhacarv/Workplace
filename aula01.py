import pygame
import random
import sys

# Inicialização do pygame
pygame.init()

# Configurações da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Configurações da cobra
tamanho_bloco = 20
velocidade = 15

# Função para desenhar a cobra
def desenhar_cobra(tamanho, lista):
    for x in lista:
        pygame.draw.rect(tela, VERDE, [x[0], x[1], tamanho_bloco, tamanho_bloco])

# Função principal
def jogo():
    x = largura // 2
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0

    corpo_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco

    relogio = pygame.time.Clock()
    fim_de_jogo = False

    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_mudanca == 0:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT and x_mudanca == 0:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP and y_mudanca == 0:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN and y_mudanca == 0:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        x += x_mudanca
        y += y_mudanca

        # Verifica colisão com as bordas
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_de_jogo = True

        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = [x, y]
        corpo_cobra.append(cabeca)
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        # Verifica colisão com o próprio corpo
        for parte in corpo_cobra[:-1]:
            if parte == cabeca:
                fim_de_jogo = True

        desenhar_cobra(tamanho_bloco, corpo_cobra)
        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            comprimento_cobra += 1
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco

        relogio.tick(velocidade)

    # Mensagem de fim de jogo
    fonte = pygame.font.SysFont(None, 50)
    texto = fonte.render('Game Over', True, BRANCO)
    tela.blit(texto, [largura // 2 - 100, altura // 2 - 25])
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    jogo()